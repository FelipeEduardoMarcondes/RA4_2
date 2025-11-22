# assembly_generator.py
# FELIPE EDUARDO MARCONDES
# GRUPO 2
# Gerador de código Assembly AVR para Arduino Uno (ATmega328P)
# CORREÇÃO: Sintaxe GNU Assembler (lo8/hi8) e definições explícitas de constantes.

import re

class AVRAssemblyGenerator:
    def __init__(self):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
    
    def gerarAssembly(self, tac_instructions):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        
        # Passo 1: Mapear variáveis para memória
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
        # Definições explícitas para o ATmega328P para evitar erros de 'garbage'
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
            "    ; Inicializar pilha (Stack Pointer) usando sintaxe GNU (hi8/lo8)",
            "    ldi r16, hi8(RAMEND)",
            "    out SPH, r16",
            "    ldi r16, lo8(RAMEND)",
            "    out SPL, r16",
            "    ; R1 deve ser zero para rotinas GCC",
            "    clr r1",
            ""
        ])

    def _gerar_epilogo(self):
        self.assembly.extend([
            "fim_programa:",
            "    rjmp fim_programa"
        ])

    def _load_operand(self, operand, reg_low, reg_high):
        # Literal
        if re.match(r'^-?\d+(\.\d+)?$', operand):
            try:
                val = float(operand)
                val_int = int(val)
                if val_int < 0: val_int = 65536 + val_int
                
                # Divide em bytes low/high
                low_byte = val_int & 0xFF
                high_byte = (val_int >> 8) & 0xFF
                
                self.assembly.append(f"    ldi {reg_low}, {low_byte}")
                self.assembly.append(f"    ldi {reg_high}, {high_byte}")
            except:
                self.assembly.append(f"    ; Erro convertendo literal {operand}")
        # Variável
        else:
            mem_match = re.match(r'MEM\[(\w+)\]', operand)
            var_name = mem_match.group(1) if mem_match else operand
            
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
        # Atribuição
        match_assign = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)$', inst)
        if match_assign:
            dest, src = match_assign.groups()
            self._load_operand(src, 'r24', 'r25')
            self._store_result(dest, 'r24', 'r25')
            return True

        # Binária
        match_bin = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*([a-zA-Z0-9_\.\[\]]+)', inst)
        if match_bin:
            dest, op1, op, op2 = match_bin.groups()
            self._load_operand(op1, 'r24', 'r25')
            self._load_operand(op2, 'r22', 'r23')
            self._aplicar_operacao(op)
            self._store_result(dest, 'r24', 'r25')
            return True

        # Desvios
        match_goto = re.match(r'goto\s+(\w+)', inst)
        if match_goto:
            self.assembly.append(f"    rjmp {match_goto.group(1)}")
            return True

        # Condicional
        match_if = re.match(r'ifFalse\s+(t\d+|MEM\[\w+\])\s+goto\s+(\w+)', inst)
        if match_if:
            cond_var, label = match_if.groups()
            self._load_operand(cond_var, 'r24', 'r25')
            self.assembly.append("    or r24, r25")
            self.assembly.append(f"    breq {label}")
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
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            self.assembly.append("    cp r24, r22")
            self.assembly.append("    cpc r25, r23")
            
            lbl_true = f"L_TRUE_{len(self.assembly)}"
            lbl_end = f"L_END_{len(self.assembly)}"
            
            branch_map = {
                '==': 'breq', '!=': 'brne',
                '<': 'brcs', '>=': 'brcc',
                '>': 'brne', '<=': 'breq' # Simplificado
            }
            
            if op == '>':
                self.assembly[-2] = "    cp r22, r24"
                self.assembly[-1] = "    cpc r23, r25"
                branch = 'brcs'
            elif op == '<=':
                self.assembly[-2] = "    cp r22, r24"
                self.assembly[-1] = "    cpc r23, r25"
                branch = 'brcc'
            else:
                branch = branch_map.get(op, 'breq')

            self.assembly.append(f"    {branch} {lbl_true}")
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
    return False 

def gerarRelatorioAssembly(tac, asm, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório Assembly\nGerado com arquitetura Load-Store 16-bit.\n")