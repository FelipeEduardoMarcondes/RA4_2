# compilar.py
# FELIPE EDUARDO MARCONDES
# GRUPO 2
# Compilador completo: Fases 1-4 (Léxico + Sintático + Semântico + TAC + Otimização + Assembly)
# VERSÃO CORRIGIDA COM IMPRESSÃO SERIAL

import sys
import json
import io
import os

# Importa configurações
try:
    from config import get_config
    config = get_config()
except ImportError:
    print("AVISO: arquivo config.py não encontrado, usando configurações padrão")
    config = {
        'porta_serial': 'COM4',
        'baud_upload': 115200,
        'auto_upload': False,
        'output_dir': 'analises',
        'verbose': 1
    }

from leitor import lerTokens
from parser import parsear, construirGramatica, calcularFirst, calcularFollow, construirTabelaLL1
from semantico import (
    inicializarTabelaSimbolos,
    definirGramaticaAtributos,
    analisarSemantica,
    gerarArvoreAtribuida,
    gerarRelatorioTipos,
    gerarRelatorioErros
)
from tac_generator import TACGenerator, salvarTAC
from otimizador import TACOptimizer, salvarTACOtimizado, gerarRelatorioOtimizacoes
from assembly_generator import (
    AVRAssemblyGenerator, 
    salvarAssembly, 
    gerarHex,
    gerarRelatorioAssembly,
    uploadHex
)


def imprimirArvore(node, indent=0, prefix=""):
    """Imprime árvore sintática de forma hierárquica."""
    if node is None:
        return
    
    tipo_info = ""
    if 'tipo_inferido' in node and node['tipo_inferido']:
        tipo_info = f" : {node['tipo_inferido']}"
    
    print("  " * indent + prefix + node['type'] + tipo_info, end="")

    if node['value'] is not None:
        print(f" = {node['value']}")
    else:
        print()

    for i, child in enumerate(node.get('children', [])):
        is_last = (i == len(node['children']) - 1)
        child_prefix = "└─ " if is_last else "├─ "
        imprimirArvore(child, indent + 1, child_prefix)


def gerarGramaticaAtributosMd(gramatica_atributos, filename):
    """Gera documentação da gramática de atributos."""
    descricao = gramatica_atributos.get('descricao', "Gramática de Atributos RPN")
    regras = gramatica_atributos.get('regras_tipo', {})

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Gramática de Atributos - Linguagem RPN\n\n")
        f.write("**Gerado automaticamente pelo compilador (Versão Completa)**\n\n")
        
        f.write("## 1. Atributos\n\n")
        f.write(descricao)
        f.write("\n\n")
        
        f.write("## 2. Regras de Produção com Atributos\n\n")
        f.write("Para cada nó da árvore, calculamos os seguintes atributos **sintetizados**:\n")
        f.write("- **tipo**: {int, real, booleano}\n")
        f.write("- **valor**: Valor computado (se aplicável)\n")
        
        f.write("\n---\n\n")
        
        f.write("### 2.1 Literais (EXPR -> num)\n\n")
        f.write("- **Regra:** `Γ ⊢ num : int` (se `num` é inteiro); `Γ ⊢ num : real` (se `num` tem ponto decimal)\n")
        f.write("- **RPN:** `(5)` -> `tipo: int` | `(5.0)` -> `tipo: real`\n")
        f.write("- **Sintetizado:** `EXPR.tipo` = `int` ou `real`\n")

        f.write("\n---\n\n")

        f.write("### 2.2 Identificadores (EXPR -> id)\n\n")
        f.write("- **Regra:** `Γ(x) = T, Γ(x).inicializada = true ──────────── Γ ⊢ x : T`\n")
        f.write("- **RPN:** `(X)` -> `tipo: Γ(X).tipo`\n")
        f.write("- **Sintetizado:** `EXPR.tipo` = `TabelaSimbolos[id.nome].tipo`\n")
        f.write("- **Restrição:** ERRO se `id.nome` não inicializado.\n")

        f.write("\n---\n\n")
        
        f.write("### 2.3 Operações Aritméticas\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂ ──────────── Γ ⊢ (e₁ e₂ op) : promover_tipo(T₁, T₂)`\n")


def main():
    if len(sys.argv) != 2:
        print("=" * 60)
        print("COMPILADOR RPN - Fases 1-4 (VERSÃO CORRIGIDA)")
        print("=" * 60)
        print("\nUso: python compilar.py <arquivo.txt>")
        print("\nExemplo: python compilar.py teste_print.txt")
        print("=" * 60)
        sys.exit(1)
    
    filename = sys.argv[1]
    
    output_dir = config.get('output_dir', 'analises')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    base_name = os.path.splitext(os.path.basename(filename))[0]
    
    # Arquivos de saída
    gramatica_file = os.path.join(output_dir, 'gramatica_atributos_gerada.md')
    relatorio_tipos_file = os.path.join(output_dir, f"{base_name}_julgamento_tipos.md")
    relatorio_erros_file = os.path.join(output_dir, f"{base_name}_erros_semanticos.md")
    arvore_json_file = os.path.join(output_dir, f"{base_name}_arvore_atribuida.json")
    arvore_md_file = os.path.join(output_dir, f"{base_name}_arvore_sintatica.md")
    tac_file = os.path.join(output_dir, f"{base_name}_tac.txt")
    tac_otimizado_file = os.path.join(output_dir, f"{base_name}_tac_otimizado.txt")
    otimizacoes_file = os.path.join(output_dir, f"{base_name}_otimizacoes.md")
    asm_file = os.path.join(output_dir, f"{base_name}.s")
    hex_file = os.path.join(output_dir, f"{base_name}.hex")
    relatorio_asm_file = os.path.join(output_dir, f"{base_name}_assembly.md")
    
    try:
        print("=" * 60)
        print(f"COMPILANDO: {filename}")
        print("=" * 60)
        
        # FASE 1: ANÁLISE LÉXICA
        print("\n[FASE 1] Análise Léxica...")
        tokens = lerTokens(filename)
        num_tokens = len([t for t in tokens if t['type'] != 'eof'])
        print(f"✓ {num_tokens} token(s) identificado(s)")
        
        # FASE 2: ANÁLISE SINTÁTICA
        print("\n[FASE 2] Análise Sintática...")
        gramatica = construirGramatica()
        first = calcularFirst(gramatica)
        follow = calcularFollow(gramatica, first)
        tabela_ll1 = construirTabelaLL1(gramatica, first, follow)
        
        ast_list, erros_sintaticos = parsear(tokens, tabela_ll1)
        
        if erros_sintaticos:
            print(f"✗ {len(erros_sintaticos)} erro(s) sintático(s) encontrado(s):")
            for erro in erros_sintaticos:
                print(f"  - {erro}")
            print("\n⛔ Compilação interrompida devido a erros sintáticos.")
            sys.exit(1)
        
        print(f"✓ {len(ast_list)} expressão(ões) válida(s)")
        
        # FASE 3: ANÁLISE SEMÂNTICA
        print("\n[FASE 3] Análise Semântica...")
        
        gramatica_atributos = definirGramaticaAtributos()
        tabela_simbolos = inicializarTabelaSimbolos() 
        arvore_anotada, erros_semanticos = analisarSemantica(ast_list, tabela_simbolos)
        
        if erros_semanticos:
            print(f"⚠ {len(erros_semanticos)} erro(s) semântico(s) encontrado(s)")
        else:
            print("✓ Nenhum erro semântico detectado")
        
        arvore_atribuida_final = gerarArvoreAtribuida(arvore_anotada)
        
        # FASE 4: GERAÇÃO DE TAC
        print("\n[FASE 4] Geração de Código Intermediário (TAC)...")
        tac_generator = TACGenerator()
        tac_instructions = tac_generator.gerarTAC(arvore_anotada)
        print(f"✓ {len(tac_instructions)} instruções TAC geradas")
        
        # FASE 4.1: OTIMIZAÇÃO
        print("\n[FASE 4.1] Otimizando código TAC...")
        optimizer = TACOptimizer()
        tac_otimizado = optimizer.otimizarTAC(tac_instructions)
        stats = optimizer.get_optimization_stats()
        
        total_opts = sum(stats.values())
        print(f"✓ {total_opts} otimizações aplicadas:")
        for opt_name, count in stats.items():
            if count > 0:
                print(f"  - {opt_name.replace('_', ' ').title()}: {count}")
        
        reducao = len(tac_instructions) - len(tac_otimizado)
        if reducao > 0:
            print(f"✓ Redução: {reducao} instruções ({100 * reducao / len(tac_instructions):.1f}%)")
        
        # FASE 4.2: GERAÇÃO DE ASSEMBLY
        print("\n[FASE 4.2] Gerando código Assembly AVR...")
        asm_generator = AVRAssemblyGenerator()
        asm_instructions = asm_generator.gerarAssembly(tac_otimizado)
        print(f"✓ {len(asm_instructions)} linhas de Assembly geradas")
        
        # FASE 4.3: COMPILAÇÃO PARA HEX
        print("\n[FASE 4.3] Compilando Assembly para HEX...")
        salvarAssembly(asm_instructions, asm_file)
        print(f"✓ Assembly salvo: {asm_file}")
        
        hex_gerado = gerarHex(asm_file, hex_file)
        if hex_gerado:
            print(f"✓ HEX gerado com sucesso: {hex_file}")
            
            # UPLOAD AUTOMÁTICO (se configurado)
            if config.get('auto_upload', False):
                print(f"\n[UPLOAD] Fazendo upload para {config['porta_serial']}...")
                upload_ok = uploadHex(hex_file, config['porta_serial'], config.get('baud_upload', 115200))
                if upload_ok:
                    print("✓ Upload concluído!")
                    print(f"\n💡 Abra o monitor serial em {config.get('baud_monitor', 9600)} baud para ver os resultados")
                else:
                    print("⚠ Upload falhou. Tente manualmente:")
                    print(f"   avrdude -c arduino -p ATMEGA328P -P {config['porta_serial']} -b 115200 -U flash:w:{hex_file}:i")
            else:
                print(f"\n💡 Para fazer upload manualmente:")
                print(f"   avrdude -c arduino -p ATMEGA328P -P {config['porta_serial']} -b 115200 -U flash:w:{hex_file}:i")
                print(f"\n💡 Ou configure AUTO_UPLOAD=True em config.py")
        else:
            print("⚠ Não foi possível gerar HEX (toolchain AVR pode não estar instalada)")
            print("   O arquivo Assembly (.s) foi gerado e pode ser compilado manualmente")
        
        # GERAÇÃO DE RELATÓRIOS
        print("\n[SAÍDA] Gerando relatórios...")
        
        gerarGramaticaAtributosMd(gramatica_atributos, gramatica_file)
        print(f"  ✓ {gramatica_file}")
        
        gerarRelatorioTipos(arvore_anotada, relatorio_tipos_file)
        print(f"  ✓ {relatorio_tipos_file}")
        
        gerarRelatorioErros(erros_semanticos, relatorio_erros_file)
        print(f"  ✓ {relatorio_erros_file}")
        
        with open(arvore_json_file, 'w', encoding='utf-8') as f:
            json.dump(arvore_atribuida_final, f, indent=2, ensure_ascii=False)
        print(f"  ✓ {arvore_json_file}")
        
        with open(arvore_md_file, 'w', encoding='utf-8') as f:
            f.write(f"# Árvore Sintática Atribuída - {filename}\n\n")
            f.write("**Gerado pelo compilador RPN - Fase 3**\n\n")
            
            for linha_num, ast in arvore_anotada:
                f.write(f"## Expressão {linha_num}\n\n")
                f.write(f"**Tipo inferido:** `{ast.get('tipo_inferido', 'ERRO')}`\n\n")
                f.write("```\n")
                
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                imprimirArvore(ast)
                output = buffer.getvalue()
                sys.stdout = old_stdout
                
                f.write(output)
                f.write("```\n\n")
        print(f"  ✓ {arvore_md_file}")
        
        salvarTAC(tac_instructions, tac_file)
        print(f"  ✓ {tac_file}")
        
        salvarTACOtimizado(tac_otimizado, tac_otimizado_file)
        print(f"  ✓ {tac_otimizado_file}")
        
        gerarRelatorioOtimizacoes(tac_instructions, tac_otimizado, stats, otimizacoes_file)
        print(f"  ✓ {otimizacoes_file}")
        
        gerarRelatorioAssembly(tac_otimizado, asm_instructions, relatorio_asm_file)
        print(f"  ✓ {relatorio_asm_file}")
        
        # RESUMO
        print("\n" + "=" * 60)
        print("RESUMO DA COMPILAÇÃO")
        print("=" * 60)
        print(f"Tokens processados:          {num_tokens}")
        print(f"Expressões analisadas:       {len(ast_list)}")
        print(f"Variáveis declaradas:        {len(tabela_simbolos['simbolos'])}")
        print(f"Erros semânticos:            {len(erros_semanticos)}")
        print(f"Instruções TAC (original):   {len(tac_instructions)}")
        print(f"Instruções TAC (otimizado):  {len(tac_otimizado)}")
        print(f"Otimizações aplicadas:       {total_opts}")
        print(f"Linhas Assembly geradas:     {len(asm_instructions)}")
        
        if erros_semanticos:
            print("\n⚠ Status: COMPILAÇÃO CONCLUÍDA COM ERROS")
        else:
            print("\n✅ Status: COMPILAÇÃO BEM-SUCEDIDA")
        
        print("=" * 60)
        
        if hex_gerado and not config.get('auto_upload', False):
            print("\n📌 PRÓXIMOS PASSOS:")
            print(f"   1. Faça upload: avrdude -c arduino -p ATMEGA328P -P {config['porta_serial']} -b 115200 -U flash:w:{hex_file}:i")
            print(f"   2. Monitore serial: python monitor_serial.py")
            print(f"   3. Configure baud rate: 9600")
        
    except FileNotFoundError as e:
        print(f"\n❌ ERRO: Arquivo não encontrado - {e}")
        sys.exit(1)
    except SyntaxError as e:
        print(f"\n❌ ERRO DE SINTAXE: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"\n❌ ERRO DE VALOR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()