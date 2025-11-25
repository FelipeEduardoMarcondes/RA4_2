# assembly_generator_int.py
# Versão MODIFICADA para Inteiros Puros (Fibonacci/Fatorial)
# CORREÇÃO: Fix para erro R_AVR_7_PCREL (Pulo longo em condicionais)

import re
import os

# FORÇA ESCALA 1:1 (Inteiros Puros)
SCALE = 1 

class AVRAssemblyGeneratorInt:
    def __init__(self):
        self.assembly = []
        self.bss_section = []
        self.vars_declared = set()
        self.internal_label_count = 0 # Contador para labels locais
    
    def gerarAssembly(self, tac_instructions):
        self.assembly = []
        self.bss_section = []
        self.vars_declared = set()
        self.internal_label_count = 0 # Reseta contador
        
        self._mapear_variaveis(tac_instructions)
        self._gerar_bss_section()
        self._gerar_prologo()
        
        for inst in tac_instructions:
            clean_inst = inst.split('#')[0].strip()
            if not clean_inst: continue
            if clean_inst.endswith(':'):
                self.assembly.append(clean_inst)
                continue
            
            self.assembly.append(f"    ; TAC: {clean_inst}")
            self._processar_instrucao(clean_inst)
        
        self._gerar_epilogo()
        return self._montar_codigo_completo()

    def _mapear_variaveis(self, instructions):
        for inst in instructions:
            temps = re.findall(r'\b(t\d+)\b', inst)
            mems = re.findall(r'MEM\[(\w+)\]', inst)
            self.vars_declared.update(temps)
            self.vars_declared.update(mems)
            assign = re.match(r'([A-Z_][A-Z0-9_]*)\s*=', inst)
            if assign: self.vars_declared.update([assign.group(1)])

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
            "    clr r1",          # <--- ADICIONE ISSO (Zera registrador de "zero")
            "    ldi r16, 0x08", "    out 0x3E, r16",
            "    ldi r16, 0xFF", "    out 0x3D, r16",
            "    call uart_init", 
            "    call res_init"
        ])

    def _gerar_epilogo(self):
        self.assembly.extend(["end_loop:", "    rjmp end_loop"])

    def _montar_codigo_completo(self):
        return self.bss_section + self.assembly

    def _load_val(self, operand, reg_L='r24', reg_H='r25', is_raw=False):
        operand_str = str(operand).strip()
        if re.match(r'^-?\d+(\.\d+)?$', operand_str):
            val_float = float(operand_str)
            val_int = int(val_float) # Inteiro puro
            
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
        if var_name == "MEM": self.assembly.append("    call mem_store")
        else:
            self.assembly.append(f"    sts {var_name}, r24")
            self.assembly.append(f"    sts {var_name} + 1, r25")

    def _processar_instrucao(self, inst):
        if 'PRINT[' in inst:
            src = re.match(r'.*PRINT\[(.*)\]', inst).group(1)
            self._load_val(src, 'r24', 'r25')
            self.assembly.append("    call res_save")
            self.assembly.append("    call print_int16") 
            self.assembly.append("    call uart_newline")
            dest_match = re.match(r'(\w+)\s*=', inst)
            if dest_match: self._store_val(dest_match.group(1))
            return

        if 'RES[' in inst:
            match = re.match(r'(\w+)\s*=\s*RES\[(.*)\]', inst)
            if match:
                dest, n_operand = match.groups()
                self._load_val(n_operand, 'r22', 'r23', is_raw=True)
                self.assembly.append("    call res_fetch")
                self._store_val(dest)
                return

        match_bin = re.match(r'(\w+|MEM\[\w+\])\s*=\s*(.*)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*(.*)', inst)
        if match_bin and 'PRINT' not in inst and 'RES' not in inst and 'ifFalse' not in inst:
            dest, op1, op, op2 = match_bin.groups()
            if not op1.strip(): pass
            else:
                self._load_val(op1, 'r24', 'r25')
                self._load_val(op2, 'r22', 'r23')
                
                if op == '+':
                    self.assembly.append("    add r24, r22")
                    self.assembly.append("    adc r25, r23")
                elif op == '-':
                    self.assembly.append("    sub r24, r22")
                    self.assembly.append("    sbc r25, r23")
                elif op == '*': self.assembly.append("    call mul16u") 
                elif op == '|': self.assembly.append("    call fx_div") 
                elif op == '/': self.assembly.append("    call div16s")
                elif op == '%': self.assembly.append("    call op_mod")
                elif op == '^': self.assembly.append("    call op_pow_int") 
                
                # Relacionais
                elif op == '==': self.assembly.append("    call op_eq")
                elif op == '!=': self.assembly.append("    call op_neq")
                elif op == '>':  self.assembly.append("    call op_gt")
                elif op == '<':  self.assembly.append("    call op_lt")
                elif op == '>=': self.assembly.append("    call op_ge")
                elif op == '<=': self.assembly.append("    call op_le")
                
                self._store_val(dest)
                return

        match_assign = re.match(r'(\w+|MEM\[\w+\])\s*=\s*(.*)', inst)
        if match_assign and 'goto' not in inst and 'ifFalse' not in inst:
            dest, src = match_assign.groups()
            self._load_val(src, 'r24', 'r25')
            self._store_val(dest)
            return
            
        if 'ifFalse' in inst:
            cond, label = re.match(r'ifFalse\s+(.*)\s+goto\s+(\w+)', inst).groups()
            self._load_val(cond, 'r24', 'r25')
            self.assembly.append("    or r24, r25")
            
            # --- FIX TRAMPOLIM ---
            # Usa brne (pulo curto reverso) + rjmp (pulo longo)
            skip_lbl = f"_skip_jmp_{self.internal_label_count}"
            self.internal_label_count += 1
            
            self.assembly.append(f"    brne {skip_lbl}") # Se True (não zero), pula o rjmp
            self.assembly.append(f"    rjmp {label}")    # Se False (zero), pula longe para o alvo
            self.assembly.append(f"{skip_lbl}:")         # Alvo do pulo curto
            # ---------------------
            return
            
        if 'goto' in inst:
            label = re.match(r'goto\s+(\w+)', inst).group(1)
            self.assembly.append(f"    rjmp {label}")
            return

def salvarAssemblyInt(instructions, filename):
    libs_content = ""
    lib_files = [
        "lib_avr/uart.s", 
        "lib_avr/math_core.s", 
        "lib_avr/math_inteiro.s", 
        "lib_avr/runtime.s",
        "lib_avr/storage.s"
    ]
    
    for lib in lib_files:
        if os.path.exists(lib):
            with open(lib, 'r') as f:
                libs_content += f"\n; === LIB: {lib} ===\n" + f.read() + "\n"
    
    with open(filename, 'w') as f:
        for line in instructions:
            f.write(line + '\n')
        f.write("\n; === BIBLIOTECAS AVR ===\n")
        f.write(libs_content)