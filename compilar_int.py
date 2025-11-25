# compilar_int.py
# Compilador ALTERNATIVO para testes de Inteiros (Fibonacci/Fatorial)

import sys
import os
from leitor import lerTokens
from parser import parsear, construirGramatica, calcularFirst, calcularFollow, construirTabelaLL1
from semantico import inicializarTabelaSimbolos, analisarSemantica, gerarArvoreAtribuida
from tac_generator import TACGenerator
from otimizador import TACOptimizer
# Importa o NOVO gerador
from assembly_generator_int import AVRAssemblyGeneratorInt, salvarAssemblyInt
from assembly_generator import gerarHex, uploadHex # Reutiliza funções auxiliares
from tac_generator import TACGenerator, salvarTAC  # <--- Adicione salvarTAC
from otimizador import TACOptimizer, salvarTACOtimizado # <--- Adicione salvarTACOtimizado

def main():
    if len(sys.argv) != 2:
        print("Uso: python compilar_int.py <arquivo.txt>")
        sys.exit(1)
    
    filename = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_dir = os.path.join("analises", base_name)
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    
    asm_file = os.path.join(output_dir, f"{base_name}.s")
    hex_file = os.path.join(output_dir, f"{base_name}.hex")

    print(f"\n=== COMPILAÇÃO MODO INTEIRO (FIBONACCI/FATORIAL) ===")
    print(f"Arquivo: {filename}")

    # 1. Léxico e Sintático
    tokens = lerTokens(filename)
    gramatica = construirGramatica()
    tabela = construirTabelaLL1(gramatica, calcularFirst(gramatica), calcularFollow(gramatica, calcularFirst(gramatica)))
    ast_list, erros = parsear(tokens, tabela)
    if erros: 
        print("Erros Sintáticos:", erros)
        sys.exit(1)

    # 2. Semântico
    tabela_simbolos = inicializarTabelaSimbolos()
    arvore_anotada, erros_sem = analisarSemantica(ast_list, tabela_simbolos)
    # Ignora erros de tipo se for coisa simples, pois estamos forçando inteiros
    
    # 3. TAC
    tac_gen = TACGenerator()
    tac = tac_gen.gerarTAC(arvore_anotada)
    
    # 4. Otimização
    opt = TACOptimizer()
    tac_opt = opt.otimizarTAC(tac)
    # ... (código anterior) ...

    # Defina os nomes dos arquivos
    tac_file = os.path.join(output_dir, f"{base_name}_tac.txt")
    tac_opt_file = os.path.join(output_dir, f"{base_name}_tac_otimizado.txt")

    # 3. TAC
    tac_gen = TACGenerator()
    tac = tac_gen.gerarTAC(arvore_anotada)
    
    # --- ADICIONE ISTO ---
    salvarTAC(tac, tac_file)
    print(f"TAC salvo: {tac_file}")
    # ---------------------
    
    # 4. Otimização
    opt = TACOptimizer()
    tac_opt = opt.otimizarTAC(tac)
    
    # --- ADICIONE ISTO ---
    salvarTACOtimizado(tac_opt, tac_opt_file)
    print(f"TAC Otimizado salvo: {tac_opt_file}")
    # ---------------------

    # 5. Assembly (USANDO O GERADOR MODIFICADO)
    # ... (resto do código igual) ...
    # 5. Assembly (USANDO O GERADOR MODIFICADO)
    print("Gerando Assembly para inteiros sem sinal...")
    asm_gen = AVRAssemblyGeneratorInt()
    asm_code = asm_gen.gerarAssembly(tac_opt)
    
    salvarAssemblyInt(asm_code, asm_file)
    
    # 6. Hex e Upload
    if gerarHex(asm_file, hex_file):
        print(f"HEX gerado: {hex_file}")
        # Ajuste a porta serial conforme seu sistema, ou copie do config.py
        porta = "/dev/ttyACM0" 
        print(f"Enviando para {porta}...")
        uploadHex(hex_file, porta, 115200)
        print("Concluído! Abra o monitor serial.")

if __name__ == "__main__":
    main()