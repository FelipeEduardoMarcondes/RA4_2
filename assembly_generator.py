# assembly_generator.py
# FELIPE EDUARDO MARCONDES - GRUPO 2

import re
import subprocess
import os
from config import get_config

cfg = get_config()

class AVRAssemblyGenerator:
    def __init__(self, int_mode=False):
        self.assembly = []
        self.bss_section = []
        self.vars_declared = set()
        self.label_counter = 0
        self.int_mode = int_mode
        
        # Define a escala dinamicamente
        # Modo Inteiro: 1 (1 = 1)
        # Modo Ponto Fixo: 256 (1.0 = 256)
        self.scale = 1 if int_mode else cfg['scale']
    
    def gerarAssembly(self, tac_instructions):
        self.assembly = []
        self.bss_section = []
        self.vars_declared = set()
        self.label_counter = 0
        
        # 1. Identifica variáveis
        self._mapear_variaveis(tac_instructions)
        self._gerar_bss_section()
        
        # 2. Gera Prólogo
        self._gerar_prologo()
        
        # 3. Traduz instruções TAC linha a linha
        for inst in tac_instructions:
            clean_inst = inst.split('#')[0].strip()
            
            if inst.strip().startswith('#'):
                self.assembly.append(f"\n    ; {inst.strip()}")

                continue
            
            if not clean_inst:

                continue
            
            if clean_inst.endswith(':'):
                self.assembly.append(clean_inst)

                continue
            
            self.assembly.append(f"    ; TAC: {clean_inst}")
            
            if not self._processar_instrucao(clean_inst):
                self.assembly.append(f"    ; ERRO: Instrução não suportada: {clean_inst}")
        
        # 4. Gera Epílogo
        self._gerar_epilogo()
        return self._montar_codigo_completo()

    def _mapear_variaveis(self, instructions):
        for inst in instructions:
            temps = re.findall(r'\b(t\d+)\b', inst)
            mems = re.findall(r'MEM\[(\w+)\]', inst)
            self.vars_declared.update(temps)
            self.vars_declared.update(mems)
            assign = re.match(r'([A-Z_][A-Z0-9_]*)\s*=', inst)

            if assign:
                self.vars_declared.update([assign.group(1)])

    def _gerar_bss_section(self):
        self.bss_section.append(".section .bss")
        for var in sorted(list(self.vars_declared)):
            if var == "MEM": continue

            self.bss_section.append(f"    .lcomm {var}, 2")

    def _gerar_prologo(self):
        self.assembly.extend([
            ".section .text",
            ".global main",
            "main:",
            "    ; --- Setup Inicial ---",
            "    clr r1",          # Zera registrador de segurança
            "    ldi r16, 0x08", "    out 0x3E, r16", # SPH
            "    ldi r16, 0xFF", "    out 0x3D, r16", # SPL
            "    call uart_init  ; Inicia Serial",
            "    call res_init   ; Inicia Buffer RES",
            "    ; --- Inicio do Programa ---"
        ])

    def _gerar_epilogo(self):
        self.assembly.extend([
            "    ; --- Fim ---",
            "end_loop:",
            "    rjmp end_loop"
        ])

    def _montar_codigo_completo(self):

        return self.bss_section + self.assembly

    def _load_val(self, operand, reg_L='r24', reg_H='r25', is_raw=False):
        operand_str = str(operand).strip()

        if re.match(r'^-?\d+(\.\d+)?$', operand_str):
            val_float = float(operand_str)
            
            if is_raw:
                val_int = int(val_float)

            else:
                # Usa self.scale (1 ou 256 dependendo do modo)
                val_int = int(val_float * self.scale)
            
            if val_int < 0: val_int = 65536 + val_int
            val_int = val_int & 0xFFFF
            
            self.assembly.append(f"    ldi {reg_L}, {val_int & 0xFF}")
            self.assembly.append(f"    ldi {reg_H}, {(val_int >> 8) & 0xFF}")
        
        else:
            var_name = operand_str

            if 'MEM[' in operand_str:
                var_name = re.match(r'MEM\[(\w+)\]', operand_str).group(1)
            
            if var_name == "MEM":
                self.assembly.append(f"    call mem_load")

                if reg_L != 'r24':
                    self.assembly.append(f"    mov {reg_L}, r24")
                    self.assembly.append(f"    mov {reg_H}, r25")

            else:
                self.assembly.append(f"    lds {reg_L}, {var_name}")
                self.assembly.append(f"    lds {reg_H}, {var_name} + 1")

    def _store_val(self, dest):
        var_name = dest

        if 'MEM[' in dest:
            var_name = re.match(r'MEM\[(\w+)\]', dest).group(1)
            
        if var_name == "MEM":
            self.assembly.append("    call mem_store")

        else:
            self.assembly.append(f"    sts {var_name}, r24")
            self.assembly.append(f"    sts {var_name} + 1, r25")

    def _processar_instrucao(self, inst):
        # 1. PRINT
        if 'PRINT[' in inst:
            src = re.match(r'.*PRINT\[(.*)\]', inst).group(1)
            self._load_val(src, 'r24', 'r25')
            self.assembly.append("    call res_save") 
            
            # DECISÃO DE MODO: Imprime Inteiro ou Fixo
            if self.int_mode:
                self.assembly.append("    call print_int16")

            else:
                self.assembly.append("    call fx_print")
                
            self.assembly.append("    call uart_newline")
            
            dest_match = re.match(r'(\w+)\s*=', inst)

            if dest_match:
                self._store_val(dest_match.group(1))

            return True

        # 2. RES (Histórico)
        if 'RES[' in inst:
            match = re.match(r'(\w+)\s*=\s*RES\[(.*)\]', inst)

            if match:
                dest, n_operand = match.groups()
                self._load_val(n_operand, 'r22', 'r23', is_raw=True)
                self.assembly.append("    call res_fetch")
                self._store_val(dest)

                return True

        # 3. Operações Binárias
        match_bin = re.match(r'(\w+|MEM\[\w+\])\s*=\s*(.*)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*(.*)', inst)

        if match_bin and 'PRINT' not in inst and 'RES' not in inst and 'ifFalse' not in inst:
            dest, op1, op, op2 = match_bin.groups()
            
            if not op1.strip(): pass # Negativo literal

            else:
                self._load_val(op1, 'r24', 'r25')
                is_power = (op == '^')
                self._load_val(op2, 'r22', 'r23', is_raw=is_power)
                
                if op == '+':
                    self.assembly.append("    add r24, r22")
                    self.assembly.append("    adc r25, r23")

                elif op == '-':
                    self.assembly.append("    sub r24, r22")
                    self.assembly.append("    sbc r25, r23")
                
                # DECISÃO DE MODO: Operações Complexas
                elif op == '*': 
                    if self.int_mode: self.assembly.append("    call mul16u")
                    else: self.assembly.append("    call fx_mul")
                
                elif op == '|': 
                    if self.int_mode: self.assembly.append("    call fx_div") # Fallback ou erro se int puro não tiver div
                    else: self.assembly.append("    call fx_div")
                
                elif op == '/': 
                    self.assembly.append("    call div16s")
                
                elif op == '%': 
                    self.assembly.append("    call op_mod")
                
                elif op == '^':

                    if self.int_mode: self.assembly.append("    call op_pow_int")
                    
                    else: self.assembly.append("    call fx_pow")
                
                # Relacionais
                elif op == '==': self.assembly.append("    call op_eq")
                elif op == '!=': self.assembly.append("    call op_neq")
                elif op == '>':  self.assembly.append("    call op_gt")
                elif op == '<':  self.assembly.append("    call op_lt")
                elif op == '>=': self.assembly.append("    call op_ge")
                elif op == '<=': self.assembly.append("    call op_le")
                
                self._store_val(dest)

                return True

        # 4. Atribuição Simples
        match_assign = re.match(r'(\w+|MEM\[\w+\])\s*=\s*(.*)', inst)

        if match_assign and 'goto' not in inst and 'ifFalse' not in inst:
            dest, src = match_assign.groups()
            self._load_val(src, 'r24', 'r25')
            self._store_val(dest)

            return True
            
        # 5. Controle de Fluxo (COM FIX DO TRAMPOLIM)
        if 'ifFalse' in inst:
            cond, label = re.match(r'ifFalse\s+(.*)\s+goto\s+(\w+)', inst).groups()
            self._load_val(cond, 'r24', 'r25')
            self.assembly.append("    or r24, r25")
            
            # Trampolim para evitar R_AVR_7_PCREL
            skip_label = f"_skip_{self.label_counter}"
            self.label_counter += 1
            self.assembly.append(f"    brne {skip_label}")
            self.assembly.append(f"    rjmp {label}")
            self.assembly.append(f"{skip_label}:")

            return True
            
        if 'goto' in inst:
            label = re.match(r'goto\s+(\w+)', inst).group(1)
            self.assembly.append(f"    rjmp {label}")

            return True
            
        return False

def salvarAssembly(instructions, filename, int_mode=False):
    libs_content = ""
    # Bibliotecas comuns
    lib_files = [
        "lib_avr/uart.s", 
        "lib_avr/math_core.s", 
        "lib_avr/runtime.s",
        "lib_avr/storage.s"
    ]
    
    # Seleção de Bibliotecas baseada no Modo
    if int_mode:
        lib_files.append("lib_avr/math_inteiro.s")
        print("[ASM] Incluindo libs para MODO INTEIRO (Unsigned)")

    else:
        # Modo Normal: Usa math_signed e math_fixed
        lib_files.append("lib_avr/math_signed.s")
        lib_files.append("lib_avr/math_fixed.s")
        print("[ASM] Incluindo libs para MODO PONTO FIXO (Q8.8)")
    
    for lib in lib_files:

        if os.path.exists(lib):
            with open(lib, 'r') as f:
                libs_content += f"\n; === LIB: {lib} ===\n" + f.read() + "\n"

        else:
            print(f"AVISO: Biblioteca {lib} não encontrada!")

    with open(filename, 'w') as f:

        for line in instructions:
            f.write(line + '\n')

        f.write("\n; === BIBLIOTECAS AVR ===\n")
        f.write(libs_content)

def gerarHex(asm_file, hex_file):
    base = os.path.splitext(asm_file)[0]
    cmd1 = f"avr-gcc -mmcu=atmega328p -o {base}.elf {asm_file}"
    cmd2 = f"avr-objcopy -O ihex {base}.elf {hex_file}"
    
    print(f"Compilando ELF...")
    res = subprocess.run(cmd1, shell=True)

    if res.returncode != 0: return False
    
    print(f"Gerando HEX...")
    res = subprocess.run(cmd2, shell=True)

    return res.returncode == 0

def uploadHex(hex_file, port, baud):
    cmd = f"avrdude -c arduino -p atmega328p -P {port} -b {baud} -D -U flash:w:\"{hex_file}\":i"
    
    subprocess.run(cmd, shell=True)
    return True

def gerarRelatorioAssembly(tac, asm, filename):
    with open(filename, 'w') as f:
        f.write("# Relatório Assembly\n")