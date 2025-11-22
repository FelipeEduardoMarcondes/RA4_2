# assembly_generator.py
# FELIPE EDUARDO MARCONDES
# GRUPO 2
# Gerador de código Assembly AVR para Arduino Uno (ATmega328P)
# AJUSTE: Implementação de Ponto Fixo (Escalonamento), Comparações Signed e Toolchain

import re
import subprocess
import os

class AVRAssemblyGenerator:
    def __init__(self):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        # Fator de escala para Ponto Fixo (Fixed Point)
        # 100 significa que 1.00 será representado como 100
        # Isso permite 2 casas de precisão.
        self.SCALE = 100 
    
    def gerarAssembly(self, tac_instructions):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        
        # Passo 1: Mapear variáveis
        self._mapear_variaveis(tac_instructions)
        
        # Passo 2: Gerar Seção de Dados
        self._gerar_data_section()
        
        # Passo 3: Gerar Código
        self._gerar_prologo()
        
        for inst in tac_instructions:
            clean_inst = inst.split('#')[0].strip()
            if not clean_inst:
                if inst.strip().startswith('#'):
                    self.assembly.append(f"; {inst.strip()[1:]}")
                continue
                
            self.assembly.append(f"    ; TAC: {clean_inst}")
            
            if clean_inst.endswith(':'):
                self.assembly.append(clean_inst)
                continue

            if not self._processar_instrucao(clean_inst):
                self.assembly.append(f"    ; ERRO: Instrução não reconhecida: {clean_inst}")

        self._gerar_epilogo()
        
        return ["; Seção de Dados", ".data"] + self.data_section + \
               ["", "; Seção de Código", ".text"] + self.assembly

    def _mapear_variaveis(self, instructions):
        for inst in instructions:
            temps = re.findall(r'\b(t\d+)\b', inst)
            self.vars_declared.update(temps)
            mems = re.findall(r'MEM\[(\w+)\]', inst)
            self.vars_declared.update(mems)

    def _gerar_data_section(self):
        for var in sorted(list(self.vars_declared)):
            self.data_section.append(f"{var}: .byte 2")

    def _gerar_prologo(self):
        self.assembly.extend([
            "; Definições de Hardware (ATmega328P)",
            ".equ RAMEND, 0x08FF",
            ".equ SPL, 0x3D",
            ".equ SPH, 0x3E",
            "",
            ".global main",
            ".org 0x0000",
            "    rjmp main",
            "",
            "main:",
            "    ; Inicializar pilha",
            "    ldi r16, hi8(RAMEND)",
            "    out SPH, r16",
            "    ldi r16, lo8(RAMEND)",
            "    out SPL, r16",
            "    clr r1",
            "    ; Inicializar Serial (9600 baud)",
            "    call serial_init",
            ""
        ])

    def _gerar_epilogo(self):
        self.assembly.extend([
            "fim_programa:",
            "    rjmp fim_programa"
        ])

    def _load_operand(self, operand, reg_low, reg_high):
        # === AJUSTE DE ESCALONAMENTO ===
        
        # Literal (Número)
        if re.match(r'^-?\d+(\.\d+)?$', operand):
            try:
                val_float = float(operand)
                
                # Aplica o fator de escala (Fixed Point)
                # Ex: 3.14 -> 314
                val_scaled = int(val_float * self.SCALE)
                
                # Tratamento de complemento de dois para 16 bits
                if val_scaled < 0:
                    val_scaled = 65536 + val_scaled
                
                # Garante que cabe em 16 bits (máscara)
                val_scaled = val_scaled & 0xFFFF
                
                low_byte = val_scaled & 0xFF
                high_byte = (val_scaled >> 8) & 0xFF
                
                self.assembly.append(f"    ldi {reg_low}, {low_byte}")
                self.assembly.append(f"    ldi {reg_high}, {high_byte}")
            except:
                self.assembly.append(f"    ; Erro convertendo literal {operand}")
        
        # Variável (Memória)
        else:
            mem_match = re.match(r'MEM\[(\w+)\]', operand)
            var_name = mem_match.group(1) if mem_match else operand
            
            # Tratamento especial para RES (Histórico)
            if 'RES[' in var_name:
                 self.assembly.append(f"    ldi {reg_low}, 0")
                 self.assembly.append(f"    ldi {reg_high}, 0")
                 return

            self.assembly.append(f"    lds {reg_low}, {var_name}")
            self.assembly.append(f"    lds {reg_high}, {var_name} + 1")

    def _store_result(self, dest_var, reg_low, reg_high):
        mem_match = re.match(r'MEM\[(\w+)\]', dest_var)
        var_name = mem_match.group(1) if mem_match else dest_var
        
        self.assembly.append(f"    sts {var_name}, {reg_low}")
        self.assembly.append(f"    sts {var_name} + 1, {reg_high}")

    def _processar_instrucao(self, inst):
        # Detecção de RES (Impressão)
        # Padrão TAC: tX = RES[tY] ou tX = RES[10]
        match_res = re.match(r'(\w+)\s*=\s*RES\[(.*)\]', inst)
        if match_res:
            dest, src = match_res.groups()
            # Carrega o valor que está dentro dos colchetes do RES
            self._load_operand(src, 'r24', 'r25')
            # Chama a função de impressão
            self.assembly.append("    call print_uint16")
            # Guarda 0 no destino (ou o próprio valor, se preferir)
            self._store_result(dest, 'r24', 'r25')
            return True

        # Atribuição
        match_assign = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)$', inst)
        if match_assign:
            dest, src = match_assign.groups()
            # Ignora se for RES (já tratado acima)
            if 'RES[' in src: return False 
            
            self._load_operand(src, 'r24', 'r25')
            self._store_result(dest, 'r24', 'r25')
            return True

        # Operação Binária
        match_bin = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*([a-zA-Z0-9_\.\[\]]+)', inst)
        if match_bin:
            dest, op1, op, op2 = match_bin.groups()
            self._load_operand(op1, 'r24', 'r25') 
            self._load_operand(op2, 'r22', 'r23')
            self._aplicar_operacao(op)
            self._store_result(dest, 'r24', 'r25')
            return True

        # Desvio Incondicional
        match_goto = re.match(r'goto\s+(\w+)', inst)
        if match_goto:
            self.assembly.append(f"    rjmp {match_goto.group(1)}")
            return True

        # Desvio Condicional (com Trampolim Long Jump)
        match_if = re.match(r'ifFalse\s+(t\d+|MEM\[\w+\])\s+goto\s+(\w+)', inst)
        if match_if:
            cond_var, label = match_if.groups()
            self._load_operand(cond_var, 'r24', 'r25')
            self.assembly.append("    or r24, r25") 
            
            # AJUSTE LONG JUMP: breq label -> brne SKIP; rjmp label; SKIP:
            lbl_no_jump = f"L_NO_JUMP_{len(self.assembly)}"
            self.assembly.append(f"    brne {lbl_no_jump}") 
            self.assembly.append(f"    rjmp {label}")       
            self.assembly.append(f"{lbl_no_jump}:")
            return True

        return False

    def _aplicar_operacao(self, op):
        if op == '+':
            self.assembly.append("    add r24, r22")
            self.assembly.append("    adc r25, r23")
        elif op == '-':
            self.assembly.append("    sub r24, r22")
            self.assembly.append("    sbc r25, r23")
        elif op == '*':
            self.assembly.append("    call mul16")
        elif op in ['/', '|']:
            self.assembly.append("    call div16u")
        elif op == '%':
            self.assembly.append("    call mod16u")
        elif op == '^':
            self.assembly.append("    call pow16u")
        
        # === CORREÇÃO DE COMPARAÇÕES (SIGNED + LONG JUMPS) ===
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            
            lbl_true = f"L_TRUE_{len(self.assembly)}"
            lbl_end = f"L_END_{len(self.assembly)}"
            lbl_skip_jump = f"L_SKIP_{len(self.assembly)}"
            
            # Mapeamento para instruções de desvio inverso (para criar o trampolim)
            inverse_branch_map = {
                'breq': 'brne',
                'brne': 'breq',
                'brlt': 'brge',
                'brge': 'brlt'
            }
            
            branch_instruction = 'breq' 
            
            if op == '>':
                self.assembly.append("    cp r22, r24")
                self.assembly.append("    cpc r23, r25")
                branch_instruction = 'brlt' # Signed Less Than
                
            elif op == '<=':
                self.assembly.append("    cp r22, r24")
                self.assembly.append("    cpc r23, r25")
                branch_instruction = 'brge' # Signed Greater or Equal
                
            else:
                self.assembly.append("    cp r24, r22")
                self.assembly.append("    cpc r25, r23")
                
                mapping = {
                    '==': 'breq',
                    '!=': 'brne',
                    '<':  'brlt',
                    '>=': 'brge'
                }
                branch_instruction = mapping.get(op, 'breq')

            inv_branch = inverse_branch_map.get(branch_instruction, 'brne')
            
            self.assembly.append(f"    {inv_branch} {lbl_skip_jump}") # Pula se condição FALSA
            self.assembly.append(f"    rjmp {lbl_true}")              # Long jump se condição VERDADEIRA
            self.assembly.append(f"{lbl_skip_jump}:")                 # Ponto de continuação (False)
            
            self.assembly.append("    ldi r24, 0")
            self.assembly.append("    ldi r25, 0")
            self.assembly.append(f"    rjmp {lbl_end}")
            
            self.assembly.append(f"{lbl_true}:")
            self.assembly.append("    ldi r24, 1")
            self.assembly.append("    ldi r25, 0")
            
            self.assembly.append(f"{lbl_end}:")

# Funções auxiliares
def salvarAssembly(instructions, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in instructions:
            f.write(f"{line}\n")

def gerarHex(asm_file, hex_file):
    """
    Compila o arquivo Assembly (.s) para HEX usando a toolchain AVR.
    Requer que avr-gcc e avr-objcopy estejam instalados e no PATH.
    """
    # Deriva o nome do arquivo ELF temporário
    base_name = os.path.splitext(hex_file)[0]
    elf_file = f"{base_name}.elf"
    
    # Localiza a biblioteca matemática (necessária para mul16, div16u, etc.)
    # Tenta achar no diretório atual ou um nível acima (caso esteja dentro de 'analises')
    math_lib = "avr_math_lib.s"
    if not os.path.exists(math_lib):
        if os.path.exists(f"../{math_lib}"):
            math_lib = f"../{math_lib}"
        else:
            # Se não achar, tenta usar o caminho relativo fixo para o envio do aluno
            # Isso ajuda se estiver rodando de dentro de 'analises'
            math_lib_alt = os.path.join(os.path.dirname(asm_file), "..", "avr_math_lib.s")
            if os.path.exists(math_lib_alt):
                 math_lib = math_lib_alt
            else:
                 print(f"[AVISO] Biblioteca 'avr_math_lib.s' não encontrada. Erros de 'undefined reference' podem ocorrer.")

    # 1. Montagem e Ligação (Assembly -> ELF)
    # -mmcu=atmega328p: Especifica o chip do Arduino Uno
    # -nostartfiles:    Não usa o código de inicialização padrão do C (crt), 
    #                   pois seu assembly já define o vetor de reset (.org 0x0000).
    cmd_compile = [
        "avr-gcc",
        "-mmcu=atmega328p",
        "-o", elf_file,
        asm_file,
        "-nostartfiles" 
    ]
    
    # Inclui a biblioteca matemática na compilação se ela existir
    if os.path.exists(math_lib):
        cmd_compile.append(math_lib)

    # 2. Geração do HEX (ELF -> HEX)
    # Extrai apenas o código binário necessário para o upload
    cmd_objcopy = [
        "avr-objcopy",
        "-O", "ihex",
        "-R", ".eeprom",  # Remove seção da EEPROM (opcional, mas boa prática)
        elf_file,
        hex_file
    ]

    try:
        # Passo 1: Compilar
        print(f"   [CMD] {' '.join(cmd_compile)}")
        result_compile = subprocess.run(cmd_compile, capture_output=True, text=True)
        
        if result_compile.returncode != 0:
            print("   [ERRO] Falha no avr-gcc:")
            print(result_compile.stderr)
            return False

        # Passo 2: Gerar HEX
        print(f"   [CMD] {' '.join(cmd_objcopy)}")
        result_objcopy = subprocess.run(cmd_objcopy, capture_output=True, text=True)
        
        if result_objcopy.returncode != 0:
            print("   [ERRO] Falha no avr-objcopy:")
            print(result_objcopy.stderr)
            return False
            
        return True

    except FileNotFoundError:
        print("   [ERRO] Toolchain AVR não encontrada no PATH.")
        print("          Certifique-se de ter instalado 'avr-gcc' e 'avr-binutils'.")
        return False
    except Exception as e:
        print(f"   [ERRO] Exceção inesperada: {e}")
        return False

def uploadHex(hex_file, porta_serial, baud_rate=115200):
    """
    Faz o upload do arquivo .hex para o Arduino Uno usando o avrdude.
    """
    print(f"   [UPLOAD] Iniciando upload para {porta_serial}...")
    
    cmd_upload = [
        "avrdude",
        "-c", "arduino",
        "-p", "ATMEGA328P",
        "-P", porta_serial,
        "-b", str(baud_rate),
        "-U", f"flash:w:{hex_file}:i"
    ]
    
    try:
        result = subprocess.run(cmd_upload, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("   [ERRO] Falha no upload:")
            print(result.stderr)
            return False
            
        print("   [SUCESSO] Upload concluído!")
        return True
        
    except FileNotFoundError:
        print("   [ERRO] 'avrdude' não encontrado. Instale o Arduino IDE ou toolchain AVR.")
        return False

def gerarRelatorioAssembly(tac, asm, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório Assembly\nGerado com arquitetura Load-Store 16-bit (Escalonada).\n")