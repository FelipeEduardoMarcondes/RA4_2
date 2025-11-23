#!/usr/bin/env python3
# debug_assembly.py - Diagnóstico detalhado do Assembly

import sys
import os
import re

def analisar_assembly(arquivo):
    """Analisa arquivo Assembly em detalhes."""
    
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo não encontrado: {arquivo}")
        return
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        linhas = conteudo.split('\n')
    
    print("=" * 80)
    print("ANÁLISE DETALHADA DO ASSEMBLY")
    print("=" * 80)
    
    # 1. Estatísticas gerais
    print("\n📊 ESTATÍSTICAS:")
    print(f"   Total de linhas: {len(linhas)}")
    print(f"   Linhas de código (não comentário): {len([l for l in linhas if l.strip() and not l.strip().startswith(';')])}")
    
    # 2. Chamadas importantes
    print("\n🔍 CHAMADAS DE FUNÇÃO:")
    chamadas = {
        'serial_init': conteudo.count('call serial_init'),
        'serial_tx': conteudo.count('call serial_tx'),
        'print_int16': conteudo.count('call print_int16'),
        'print_newline': conteudo.count('call print_newline'),
    }
    
    for func, count in chamadas.items():
        status = "✓" if count > 0 else "❌"
        print(f"   {status} {func:20s}: {count:3d} vezes")
    
    if chamadas['print_int16'] == 0:
        print("\n   ⚠️  CRÍTICO: Nenhuma chamada a print_int16!")
        print("   Os números não serão impressos.")
    
    # 3. Encontrar seção do programa compilado
    print("\n📝 CÓDIGO COMPILADO:")
    
    inicio_idx = None
    fim_idx = None
    
    for i, linha in enumerate(linhas):
        if "; === INÍCIO DO PROGRAMA COMPILADO ===" in linha:
            inicio_idx = i
        elif "; === FIM DO PROGRAMA ===" in linha:
            fim_idx = i
            break
    
    if inicio_idx is not None and fim_idx is not None:
        codigo_compilado = linhas[inicio_idx:fim_idx+1]
        linhas_codigo = [l for l in codigo_compilado if l.strip() and not l.strip().startswith(';')]
        
        print(f"   Linhas entre INÍCIO e FIM: {len(codigo_compilado)}")
        print(f"   Linhas de código executável: {len(linhas_codigo)}")
        
        if len(linhas_codigo) == 0:
            print("\n   ❌ PROBLEMA: Nenhum código gerado!")
            print("   O TAC não está sendo convertido para Assembly.")
            return
        
        print(f"\n   Código gerado:")
        print("   " + "-" * 76)
        for linha in codigo_compilado[:100]:  # Primeiras 100 linhas
            print(f"   {linha}")
        
        if len(codigo_compilado) > 100:
            print(f"   ... ({len(codigo_compilado) - 100} linhas restantes)")
    
    else:
        print("   ❌ Não encontrou marcadores de INÍCIO/FIM")
    
    # 4. Procurar por instruções PRINT específicas
    print("\n🔎 PROCURANDO INSTRUÇÕES PRINT:")
    
    # Procurar padrões de PRINT no Assembly
    i = 0
    prints_encontrados = 0
    
    while i < len(linhas):
        linha = linhas[i]
        
        # Procurar comentário TAC com PRINT
        if 'TAC:' in linha and 'PRINT[' in linha:
            prints_encontrados += 1
            print(f"\n   Print #{prints_encontrados}:")
            print(f"   {i:4d} | {linha.strip()}")
            
            # Mostrar próximas 20 linhas (o código Assembly gerado)
            for j in range(1, min(21, len(linhas) - i)):
                proxima = linhas[i + j]
                print(f"   {i+j:4d} | {proxima.strip()}")
                
                # Parar se encontrar próximo comentário TAC
                if 'TAC:' in proxima and j > 5:
                    break
            
            i += 20
        else:
            i += 1
    
    if prints_encontrados == 0:
        print("   ❌ Nenhuma instrução PRINT encontrada no Assembly!")
        print("   O assembly_generator.py não está processando PRINT corretamente.")
    else:
        print(f"\n   ✓ Total de PRINTs encontrados: {prints_encontrados}")
    
    # 5. Verificar se há erros de compilação
    print("\n⚠️  POSSÍVEIS PROBLEMAS:")
    problemas = []
    
    if chamadas['print_int16'] == 0:
        problemas.append("Nenhuma chamada a print_int16 (números não serão impressos)")
    
    if chamadas['serial_init'] == 0:
        problemas.append("Nenhuma inicialização de serial")
    
    # Procurar por avisos
    avisos = [l for l in linhas if 'AVISO:' in l or 'ERRO:' in l]
    if avisos:
        problemas.append(f"{len(avisos)} avisos/erros no código")
        for aviso in avisos[:5]:
            print(f"      {aviso.strip()}")
    
    if not problemas:
        print("   ✓ Nenhum problema óbvio detectado")
    else:
        for p in problemas:
            print(f"   ❌ {p}")
    
    # 6. Análise de registradores
    print("\n📋 USO DE REGISTRADORES:")
    
    # Contar uso de registradores importantes
    regs = {
        'r24/r25 (resultado)': conteudo.count('r24') + conteudo.count('r25'),
        'r22/r23 (operando)': conteudo.count('r22') + conteudo.count('r23'),
        'r16 (temporário)': conteudo.count('r16'),
    }
    
    for reg, count in regs.items():
        print(f"   {reg:25s}: {count:4d} usos")
    
    print("\n" + "=" * 80)

def main():
    if len(sys.argv) < 2:
        print("Uso: python debug_assembly.py <arquivo.s>")
        print("\nExemplo: python debug_assembly.py analises/teste_serial.s")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    analisar_assembly(arquivo)

if __name__ == "__main__":
    main()