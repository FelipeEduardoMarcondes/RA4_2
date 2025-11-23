# FELIPE EDUARDO MARCONDES - GRUPO 2
# CORRIGIDO: RES, comparações, inicialização de variáveis

import re
import subprocess
import os

class AVRAssemblyGenerator:
    def __init__(self):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        self.SCALE = 1  # Escala para ponto flutuante simulado
        self.res_history = []  # Histórico de resultados por linha
        self.current_line = 0
        self.label_counter = 0
    
    def gerarAssembly(self, tac_instructions):
        """Gera código Assembly AVR a partir de TAC otimizado."""
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        self.res_history = []
        self.current_line = 0
        self.label_counter = 0
        
        # PASSO 1: Analisar histórico de resultados
        self._analisar_historico(tac_instructions)
        
        # PASSO 2: Mapear todas as variáveis
        self._mapear_variaveis(tac_instructions)
        
        # PASSO 3: Gerar seções
        self._gerar_data_section()
        self._gerar_prologo()
        
        # PASSO 4: Gerar corpo do programa
        for inst in tac_instructions:
            clean_inst = inst.split('#')[0].strip()
            
            # Atualizar contador de linha
            if inst.strip().startswith('# Linha'):
                try:
                    self.current_line = int(inst.split('Linha')[1].strip())
                    self.assembly.append(f"")
                    self.assembly.append(f";  ====== LINHA {self.current_line} ======")
                except:
                    pass
                continue
            
            if not clean_inst or clean_inst.startswith('#'):
                continue
            
            # Adiciona comentário TAC
            self.assembly.append(f"    ; TAC: {clean_inst}")
            
            # Processa rótulos
            if clean_inst.endswith(':'):
                self.assembly.append(clean_inst)
                continue
            
            # Processa instrução
            if not self._processar_instrucao(clean_inst):
                self.assembly.append(f"    ; AVISO: Instrução não reconhecida: {clean_inst}")
        
        # PASSO 5: Gerar epílogo
        self._gerar_epilogo()
        
        # Retorna código completo
        return self._montar_codigo_completo()

    def _analisar_historico(self, instructions):
        """
        Analisa TAC e constrói histórico de resultados.
        Cada linha RPN pode ter múltiplas instruções TAC.
        O resultado da linha é a ÚLTIMA variável atribuída (exceto PRINT).
        """
        self.res_history = []
        current_line_num = 0
        line_result = None
        
        for inst in instructions:
            clean_inst = inst.split('#')[0].strip()
            
            # Detecta início de nova linha
            if inst.strip().startswith('# Linha'):
                # Salva resultado da linha anterior
                if current_line_num > 0:
                    if line_result:
                        self.res_history.append(line_result)
                    else:
                        # Se não há resultado, usa "0" como placeholder
                        self.res_history.append("_NONE_")
                
                try:
                    current_line_num = int(inst.split('Linha')[1].strip())
                    line_result = None
                except:
                    pass
                continue
            
            if not clean_inst or clean_inst.endswith(':'):
                continue
            
            # Identifica última atribuição da linha (ignora PRINT)
            if '=' in clean_inst and 'PRINT[' not in clean_inst:
                match = re.match(r'(t\d+|MEM\[\w+\])\s*=', clean_inst)
                if match:
                    line_result = match.group(1)
        
        # Salva resultado da última linha
        if current_line_num > 0:
            if line_result:
                self.res_history.append(line_result)
            else:
                self.res_history.append("_NONE_")

    def _mapear_variaveis(self, instructions):
        """Encontra todas as variáveis usadas (temporárias e memórias)."""
        for inst in instructions:
            # Temporárias
            temps = re.findall(r'\b(t\d+)\b', inst)
            self.vars_declared.update(temps)
            
            # Memórias (MEM[X])
            mems = re.findall(r'MEM\[(\w+)\]', inst)
            self.vars_declared.update(mems)

    def _gerar_data_section(self):
        """Gera seção de dados (.data) com todas as variáveis."""
        self.data_section.append("; === Variáveis (16 bits cada) ===")
        
        for var in sorted(list(self.vars_declared)):
            self.data_section.append(f"{var}:    .word 0    ; {var}")

    def _gerar_prologo(self):
        """Gera código de inicialização do programa."""
        self.assembly.extend([
            "; === INICIALIZAÇÃO ===",
            ".equ RAMEND, 0x08FF",
            ".equ SPL, 0x3D",
            ".equ SPH, 0x3E",
            "",
            ".global main",
            ".org 0x0000",
            "    rjmp reset_handler",
            "",
            "; Vetores de interrupção (simplificado)",
            ".org 0x0034",
            "",
            "reset_handler:",
            "    ; Configura pilha",
            "    ldi r16, hi8(RAMEND)",
            "    out SPH, r16",
            "    ldi r16, lo8(RAMEND)",
            "    out SPL, r16",
            "    ",
            "    ; Zera R1 (convenção AVR-GCC)",
            "    clr r1",
            "    ",
            "    ; Inicializa UART",
            "    call uart_init",
            "    ",
            "    ; Delay para estabilização",
            "    ldi r17, 50",
            "delay_start:",
            "    ldi r16, 255",
            "delay_loop:",
            "    dec r16",
            "    brne delay_loop",
            "    dec r17",
            "    brne delay_start",
            "    ",
            "main:",
            "    ; === INÍCIO DO PROGRAMA PRINCIPAL ===",
            ""
        ])

    def _gerar_epilogo(self):
        """Gera código de finalização."""
        self.assembly.extend([
            "",
            "    ; === FIM DO PROGRAMA ===",
            "fim_programa:",
            "    rjmp fim_programa    ; Loop infinito",
            ""
        ])

    def _montar_codigo_completo(self):
        """Monta o código Assembly completo com todas as seções."""
        return [
            "; ===============================================",
            "; Código Assembly AVR para Arduino Uno",
            "; ATmega328P (8-bit, 16MHz)",
            "; Gerado automaticamente pelo Compilador RPN",
            "; FELIPE EDUARDO MARCONDES - GRUPO 2",
            "; ===============================================",
            "",
            "; === SEÇÃO DE DADOS ===",
            ".data"
        ] + self.data_section + [
            "",
            "; === SEÇÃO DE CÓDIGO ===",
            ".text"
        ] + self.assembly

    def _load_operand(self, operand, reg_low, reg_high):
        """
        Carrega operando em par de registradores (16-bit).
        
        Args:
            operand: String (literal, variável ou MEM[X])
            reg_low: Registrador low byte (ex: 'r24')
            reg_high: Registrador high byte (ex: 'r25')
        """
        # Literal numérico
        if re.match(r'^-?\d+(\.\d+)?$', operand):
            try:
                val_float = float(operand)
                val_scaled = int(val_float * self.SCALE)
                
                # Tratamento de negativos (complemento de 2 em 16 bits)
                if val_scaled < 0:
                    val_scaled = 65536 + val_scaled
                
                val_scaled = val_scaled & 0xFFFF
                low_byte = val_scaled & 0xFF
                high_byte = (val_scaled >> 8) & 0xFF
                
                self.assembly.append(f"    ldi {reg_low}, {low_byte}    ; Literal {operand} (low)")
                self.assembly.append(f"    ldi {reg_high}, {high_byte}    ; (high)")
            except Exception as e:
                self.assembly.append(f"    ; ERRO ao carregar literal {operand}: {e}")
                self.assembly.append(f"    clr {reg_low}")
                self.assembly.append(f"    clr {reg_high}")
        else:
            # Variável ou MEM[X]
            mem_match = re.match(r'MEM\[(\w+)\]', operand)
            var_name = mem_match.group(1) if mem_match else operand
            
            self.assembly.append(f"    lds {reg_low}, {var_name}    ; Carrega {var_name} (low)")
            self.assembly.append(f"    lds {reg_high}, {var_name} + 1    ; (high)")

    def _store_result(self, dest_var, reg_low, reg_high):
        """Armazena resultado em variável."""
        mem_match = re.match(r'MEM\[(\w+)\]', dest_var)
        var_name = mem_match.group(1) if mem_match else dest_var
        
        self.assembly.append(f"    sts {var_name}, {reg_low}    ; Armazena em {var_name} (low)")
        self.assembly.append(f"    sts {var_name} + 1, {reg_high}    ; (high)")

    def _processar_instrucao(self, inst):
        """
        Processa uma instrução TAC e gera Assembly correspondente.
        Retorna True se reconheceu a instrução.
        """
        
        # ========== PRINT[X] ==========
        match_print = re.match(r'(\w+)\s*=\s*PRINT\[(.*)\]', inst)
        if match_print:
            dest, src = match_print.groups()
            
            self.assembly.append(f"    ; >> PRINT({src})")
            self._load_operand(src, 'r24', 'r25')
            self.assembly.append("    call print_int16")
            self.assembly.append("    call uart_newline")
            
            # Armazena resultado (mesmo valor que foi impresso)
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== RES[N] ==========
        match_res = re.match(r'(\w+)\s*=\s*RES\[(.*)\]', inst)
        if match_res:
            dest, src = match_res.groups()
            
            # Verifica se N é literal
            if re.match(r'^\d+$', src):
                n = int(src)
                
                # Valida N
                if n < 1 or n > len(self.res_history):
                    self.assembly.append(f"    ; ERRO: RES({n}) fora do intervalo (1-{len(self.res_history)})")
                    self._load_operand("0", 'r24', 'r25')
                else:
                    # RES(N) retorna resultado de N linhas atrás
                    hist_index = -n
                    result_var = self.res_history[hist_index]
                    
                    if result_var == "_NONE_":
                        self.assembly.append(f"    ; AVISO: RES({n}) sem resultado válido")
                        self._load_operand("0", 'r24', 'r25')
                    else:
                        self.assembly.append(f"    ; >> RES({n}) = {result_var}")
                        self._load_operand(result_var, 'r24', 'r25')
            else:
                # N é variável (não suportado diretamente, usa valor zero)
                self.assembly.append(f"    ; AVISO: RES com variável ({src}) não suportado")
                self._load_operand("0", 'r24', 'r25')
            
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== ATRIBUIÇÃO SIMPLES: t1 = X ==========
        match_assign = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)$', inst)
        if match_assign:
            dest, src = match_assign.groups()
            
            self._load_operand(src, 'r24', 'r25')
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== OPERAÇÃO BINÁRIA: t1 = X op Y ==========
        match_bin = re.match(
            r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*([a-zA-Z0-9_\.\[\]]+)',
            inst
        )
        if match_bin:
            dest, op1, op, op2 = match_bin.groups()
            
            # Carrega operandos
            self._load_operand(op1, 'r24', 'r25')
            self._load_operand(op2, 'r22', 'r23')
            
            # Aplica operação
            self._aplicar_operacao(op)
            
            # Armazena resultado
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== GOTO L1 ==========
        match_goto = re.match(r'goto\s+(\w+)', inst)
        if match_goto:
            label = match_goto.group(1)
            self.assembly.append(f"    rjmp {label}")
            return True

        # ========== IFFALSE t1 GOTO L1 ==========
        match_if = re.match(r'ifFalse\s+(t\d+|MEM\[\w+\])\s+goto\s+(\w+)', inst)
        if match_if:
            cond_var, label = match_if.groups()
            
            self._load_operand(cond_var, 'r24', 'r25')
            
            # Verifica se é zero (falso)
            self.assembly.append("    or r24, r25    ; Testa se zero")
            self.assembly.append(f"    breq {label}    ; Se zero (falso), pula")
            return True

        # Instrução não reconhecida
        return False

    def _aplicar_operacao(self, op):
        """
        Aplica operação binária.
        Entrada: R25:R24 (op1), R23:R22 (op2)
        Saída: R25:R24 (resultado)
        """
        if op == '+':
            self.assembly.append("    add r24, r22    ; Soma (low)")
            self.assembly.append("    adc r25, r23    ; Soma com carry (high)")
        
        elif op == '-':
            self.assembly.append("    sub r24, r22    ; Subtração (low)")
            self.assembly.append("    sbc r25, r23    ; Subtração com borrow (high)")
        
        elif op == '*':
            self.assembly.append("    call mul16u    ; Multiplicação 16-bit")
        
        elif op in ['/', '|']:
            self.assembly.append("    call div16u    ; Divisão 16-bit")
        
        elif op == '%':
            self.assembly.append("    call mod16u    ; Módulo 16-bit")
        
        elif op == '^':
            self.assembly.append("    call pow16u    ; Potência 16-bit")
        
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            self._gerar_comparacao(op)
        
        else:
            self.assembly.append(f"    ; ERRO: Operador desconhecido '{op}'")

    def _gerar_comparacao(self, op):
        """
        Gera código para operadores relacionais.
        Retorna 1 (verdadeiro) ou 0 (falso) em R25:R24.
        """
        self.label_counter += 1
        lbl_true = f"CMP_TRUE_{self.label_counter}"
        lbl_end = f"CMP_END_{self.label_counter}"
        
        # Compara R25:R24 com R23:R22
        self.assembly.append("    cp r24, r22    ; Compara (low)")
        self.assembly.append("    cpc r25, r23   ; Compara com carry (high)")
        
        # Mapa de branches corretos
        if op == '==':
            self.assembly.append(f"    breq {lbl_true}    ; Se igual")
        elif op == '!=':
            self.assembly.append(f"    brne {lbl_true}    ; Se diferente")
        elif op == '<':
            self.assembly.append(f"    brlt {lbl_true}    ; Se menor (signed)")
        elif op == '>=':
            self.assembly.append(f"    brge {lbl_true}    ; Se maior ou igual (signed)")
        elif op == '>':
            self.assembly.append(f"    brge {lbl_end}     ; Se R24 >= R22, vai direto para falso")
            self.assembly.append(f"    rjmp {lbl_true}    ; Senão, é verdadeiro (R24 < R22, inverte)")
            # Para '>': precisamos R24 > R22, ou seja, NOT(R24 <= R22)
            # Melhor implementação:
        elif op == '<=':
            # R24 <= R22: equivale a NOT(R24 > R22), ou seja, (R24 < R22) OR (R24 == R22)
            self.assembly.append(f"    brlt {lbl_true}    ; Se menor")
            self.assembly.append(f"    breq {lbl_true}    ; Ou igual")
        
        # Caso falso
        self.assembly.append("    clr r24")
        self.assembly.append("    clr r25")
        self.assembly.append(f"    rjmp {lbl_end}")
        
        # Caso verdadeiro
        self.assembly.append(f"{lbl_true}:")
        self.assembly.append("    ldi r24, 1")
        self.assembly.append("    clr r25")
        
        self.assembly.append(f"{lbl_end}:")


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def salvarAssembly(instructions, filename):
    """Salva código Assembly em arquivo."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in instructions:
                f.write(f"{line}\n")
        return True
    except Exception as e:
        print(f"ERRO ao salvar Assembly: {e}")
        return False


def gerarHex(asm_file, hex_file):
    """
    Compila Assembly para HEX usando avr-gcc.
    Procura biblioteca matemática automaticamente.
    """
    base_name = os.path.splitext(hex_file)[0]
    elf_file = f"{base_name}.elf"
    
    # Procura biblioteca matemática
    math_lib = "avr_math_lib.s"
    search_paths = [
        math_lib,
        f"../{math_lib}",
        os.path.join(os.path.dirname(asm_file), math_lib),
        os.path.join(os.path.dirname(asm_file), "..", math_lib),
        os.path.join(os.getcwd(), math_lib)
    ]
    
    math_lib_path = None
    for path in search_paths:
        if os.path.exists(path):
            math_lib_path = path
            print(f"   [OK] Biblioteca encontrada: {path}")
            break
    
    if not math_lib_path:
        print(f"   [AVISO] Biblioteca {math_lib} não encontrada")
        print(f"   [INFO] Compilando sem funções auxiliares (pode falhar)")
    
    # Comando de compilação
    cmd_compile = [
        "avr-gcc",
        "-mmcu=atmega328p",
        "-DF_CPU=16000000UL",
        "-Os",
        "-o", elf_file,
        asm_file
    ]
    
    if math_lib_path:
        cmd_compile.append(math_lib_path)
    
    # Comando objcopy
    cmd_objcopy = [
        "avr-objcopy",
        "-O", "ihex",
        "-R", ".eeprom",
        elf_file,
        hex_file
    ]
    
    try:
        # Compilação
        print(f"\n   [COMPILANDO]")
        print(f"   $ {' '.join(cmd_compile)}")
        result = subprocess.run(cmd_compile, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("   [ERRO] Falha na compilação:")
            print(result.stderr)
            return False
        
        print("   [OK] Compilação bem-sucedida")
        
        # Conversão para HEX
        print(f"\n   [GERANDO HEX]")
        print(f"   $ {' '.join(cmd_objcopy)}")
        result = subprocess.run(cmd_objcopy, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("   [ERRO] Falha ao gerar HEX:")
            print(result.stderr)
            return False
        
        print("   [OK] HEX gerado com sucesso")
        
        # Informações de tamanho
        cmd_size = ["avr-size", "-C", "--mcu=atmega328p", elf_file]
        result = subprocess.run(cmd_size, capture_output=True, text=True)
        if result.returncode == 0:
            print("\n" + result.stdout)
        
        return True
        
    except FileNotFoundError as e:
        print(f"   [ERRO] Toolchain AVR não instalada: {e}")
        print("   [DICA] Instale com: sudo apt-get install gcc-avr avr-libc binutils-avr")
        return False
    except Exception as e:
        print(f"   [ERRO] Exceção durante compilação: {e}")
        return False


def uploadHex(hex_file, porta_serial, baud_rate=115200):
    """Faz upload do HEX para Arduino usando avrdude."""
    print(f"\n{'='*60}")
    print(f"UPLOAD PARA ARDUINO")
    print(f"{'='*60}")
    print(f"Porta: {porta_serial}")
    print(f"Baud: {baud_rate}")
    print(f"Arquivo: {hex_file}")
    print(f"{'='*60}\n")
    
    cmd_upload = [
        "avrdude",
        "-c", "arduino",
        "-p", "atmega328p",
        "-P", porta_serial,
        "-b", str(baud_rate),
        "-D",  # Não apaga EEPROM
        "-U", f"flash:w:{hex_file}:i"
    ]
    
    try:
        print(f"[EXECUTANDO]")
        print(f"$ {' '.join(cmd_upload)}\n")
        
        result = subprocess.run(cmd_upload, capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.returncode != 0:
            print("[ERRO] Falha no upload:")
            print(result.stderr)
            return False
        
        print("\n✓ Upload concluído com sucesso!")
        print(f"\n💡 Abra o monitor serial em 9600 baud para ver os resultados")
        return True
        
    except FileNotFoundError:
        print("[ERRO] 'avrdude' não encontrado no PATH")
        print("[DICA] Instale com: sudo apt-get install avrdude")
        return False
    except Exception as e:
        print(f"[ERRO] Exceção durante upload: {e}")
        return False


def gerarRelatorioAssembly(tac, asm, filename):
    """Gera relatório detalhado da geração de Assembly."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Geração de Assembly AVR\n\n")
        f.write("**Compilador RPN - Arduino Uno (ATmega328P)**\n\n")
        
        f.write("## Estatísticas\n\n")
        f.write(f"- **Instruções TAC:** {len(tac)}\n")
        f.write(f"- **Linhas Assembly:** {len(asm)}\n")
        f.write(f"- **Arquitetura:** ATmega328P (8-bit, 16MHz)\n")
        f.write(f"- **Precisão numérica:** 16-bit signed integer\n\n")
        
        f.write("## Implementação\n\n")
        
        f.write("### Operação PRINT[X]\n")
        f.write("```\n")
        f.write("1. Carrega X em R25:R24\n")
        f.write("2. Chama print_int16 (converte para decimal)\n")
        f.write("3. Chama uart_newline (envia CR+LF)\n")
        f.write("4. Armazena resultado (mesmo valor impresso)\n")
        f.write("```\n\n")
        
        f.write("### Operação RES(N)\n")
        f.write("```\n")
        f.write("1. Valida N (1 <= N <= número de linhas)\n")
        f.write("2. Recupera resultado de N linhas atrás\n")
        f.write("3. Carrega valor em R25:R24\n")
        f.write("4. Armazena em variável destino\n")
        f.write("```\n\n")
        
        f.write("### Convenção de Registradores\n\n")
        f.write("| Registrador | Uso |\n")
        f.write("|-------------|-----|\n")
        f.write("| R0-R1 | Multiplicação (mul) e zero |\n")
        f.write("| R16-R23 | Temporários |\n")
        f.write("| R24-R25 | Operando 1 / Retorno |\n")
        f.write("| R22-R23 | Operando 2 |\n")
        f.write("| R26-R27 (X) | Ponteiro |\n")
        f.write("| R30-R31 (Z) | Ponteiro de programa |\n\n")
        
        f.write("## Funções da Biblioteca\n\n")
        f.write("- `uart_init`: Inicializa UART 9600 baud\n")
        f.write("- `uart_tx`: Transmite um byte\n")
        f.write("- `uart_newline`: Envia CR+LF\n")
        f.write("- `print_int16`: Imprime inteiro 16-bit com sinal\n")
        f.write("- `mul16u`: Multiplicação 16x16=16 bit\n")
        f.write("- `div16u`: Divisão 16-bit unsigned\n")
        f.write("- `mod16u`: Módulo 16-bit\n")
        f.write("- `pow16u`: Potência 16-bit\n\n")
    
    return True