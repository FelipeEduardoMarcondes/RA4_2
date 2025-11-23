# assembly_generator.py - VERSÃO COMPLETA COM RES
# FELIPE EDUARDO MARCONDES
# GRUPO 2

import re
import subprocess
import os

class AVRAssemblyGenerator:
    def __init__(self):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        self.SCALE = 1  # SEM escalonamento para inteiros
        self.res_history = []  # Armazena variáveis de resultado de cada linha
        self.current_line = 0
    
    def gerarAssembly(self, tac_instructions):
        self.assembly = []
        self.data_section = []
        self.vars_declared = set()
        self.res_history = []
        self.current_line = 0
        
        # Passo 1: Analisar TAC e identificar resultados de cada linha
        self._analisar_historico(tac_instructions)
        
        # Passo 2: Mapear variáveis
        self._mapear_variaveis(tac_instructions)
        
        # Passo 3: Gerar Seção de Dados
        self._gerar_data_section()
        
        # Passo 4: Gerar Código
        self._gerar_prologo()
        
        for inst in tac_instructions:
            clean_inst = inst.split('#')[0].strip()
            
            # Atualizar linha atual
            if inst.strip().startswith('# Linha'):
                try:
                    self.current_line = int(inst.split('Linha')[1].strip())
                    self.assembly.append(f"; {inst.strip()[1:]}")
                except:
                    pass
                continue
            
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

    def _analisar_historico(self, instructions):
        """
        Analisa o TAC e identifica qual variável armazena o resultado de cada linha.
        Exemplo:
        # Linha 1
        t0 = 5
        t1 = 10
        t2 = t0 + t1
        MEM[X] = t2
        -> res_history[1] = 't2'
        """
        current_line_num = 0
        line_result = None
        
        for inst in instructions:
            clean_inst = inst.split('#')[0].strip()
            
            # Detecta início de nova linha
            if inst.strip().startswith('# Linha'):
                # Salva resultado da linha anterior
                if current_line_num > 0 and line_result:
                    self.res_history.append(line_result)
                
                # Inicia nova linha
                try:
                    current_line_num = int(inst.split('Linha')[1].strip())
                    line_result = None
                except:
                    pass
                continue
            
            if not clean_inst or clean_inst.endswith(':'):
                continue
            
            # Última atribuição da linha é o resultado
            match = re.match(r'(t\d+|MEM\[\w+\])\s*=', clean_inst)
            if match:
                line_result = match.group(1)
        
        # Salva resultado da última linha
        if current_line_num > 0 and line_result:
            self.res_history.append(line_result)

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
        """Carrega operando em registradores."""
        # Literal (Número)
        if re.match(r'^-?\d+(\.\d+)?$', operand):
            try:
                val_float = float(operand)
                val_scaled = int(val_float * self.SCALE)
                
                # Complemento de 2 para negativos
                if val_scaled < 0:
                    val_scaled = 65536 + val_scaled
                
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
            
            self.assembly.append(f"    lds {reg_low}, {var_name}")
            self.assembly.append(f"    lds {reg_high}, {var_name} + 1")

    def _store_result(self, dest_var, reg_low, reg_high):
        """Armazena resultado em variável."""
        mem_match = re.match(r'MEM\[(\w+)\]', dest_var)
        var_name = mem_match.group(1) if mem_match else dest_var
        
        self.assembly.append(f"    sts {var_name}, {reg_low}")
        self.assembly.append(f"    sts {var_name} + 1, {reg_high}")

    def _processar_instrucao(self, inst):
        """Processa uma instrução TAC."""
        
        # ========== RES (HISTÓRICO) ==========
        # Padrão: tX = RES[tY] ou tX = RES[N]
        match_res = re.match(r'(\w+)\s*=\s*RES\[(.*)\]', inst)
        if match_res:
            dest, src = match_res.groups()
            
            # Carrega N (número de linhas atrás)
            self._load_operand(src, 'r24', 'r25')
            
            # Verifica se N é literal (estaticamente verificável)
            if re.match(r'^\d+$', src):
                n = int(src)
                
                # Valida N
                if n < 1 or n > len(self.res_history):
                    self.assembly.append(f"    ; ERRO: RES({n}) inválido (histórico: {len(self.res_history)} linhas)")
                    self._load_operand("0", 'r24', 'r25')
                    self._store_result(dest, 'r24', 'r25')
                    return True
                
                # Recupera variável do histórico
                # res_history[0] = resultado da linha 1
                # RES(1) = linha anterior = res_history[-1]
                # RES(2) = 2 linhas atrás = res_history[-2]
                hist_index = -n
                result_var = self.res_history[hist_index]
                
                self.assembly.append(f"    ; Recupera resultado da linha {self.current_line - n} ({result_var})")
                
                # Carrega valor do histórico
                self._load_operand(result_var, 'r24', 'r25')
                
            else:
                # N é variável: implementação dinâmica (mais complexa)
                self.assembly.append(f"    ; AVISO: RES com variável ({src}) - não implementado dinamicamente")
                self.assembly.append(f"    ; Retornando 0")
                self._load_operand("0", 'r24', 'r25')
            
            # Imprime valor (chamada de print)
            self.assembly.append("    call print_int16")
            
            # Armazena resultado
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== ATRIBUIÇÃO SIMPLES ==========
        match_assign = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)$', inst)
        if match_assign:
            dest, src = match_assign.groups()
            
            self._load_operand(src, 'r24', 'r25')
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== OPERAÇÃO BINÁRIA ==========
        match_bin = re.match(r'(MEM\[\w+\]|t\d+)\s*=\s*([a-zA-Z0-9_\.\[\]]+)\s*([+\-*/%^|]|==|!=|<=|>=|<|>)\s*([a-zA-Z0-9_\.\[\]]+)', inst)
        if match_bin:
            dest, op1, op, op2 = match_bin.groups()
            self._load_operand(op1, 'r24', 'r25') 
            self._load_operand(op2, 'r22', 'r23')
            self._aplicar_operacao(op)
            self._store_result(dest, 'r24', 'r25')
            return True

        # ========== GOTO ==========
        match_goto = re.match(r'goto\s+(\w+)', inst)
        if match_goto:
            self.assembly.append(f"    rjmp {match_goto.group(1)}")
            return True

        # ========== IF FALSE ==========
        match_if = re.match(r'ifFalse\s+(t\d+|MEM\[\w+\])\s+goto\s+(\w+)', inst)
        if match_if:
            cond_var, label = match_if.groups()
            self._load_operand(cond_var, 'r24', 'r25')
            self.assembly.append("    or r24, r25") 
            
            lbl_no_jump = f"L_NO_JUMP_{len(self.assembly)}"
            self.assembly.append(f"    brne {lbl_no_jump}") 
            self.assembly.append(f"    rjmp {label}")       
            self.assembly.append(f"{lbl_no_jump}:")
            return True

        return False

    def _aplicar_operacao(self, op):
        """Aplica operação binária."""
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
        
        # Comparações
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            lbl_true = f"L_TRUE_{len(self.assembly)}"
            lbl_end = f"L_END_{len(self.assembly)}"
            lbl_skip_jump = f"L_SKIP_{len(self.assembly)}"
            
            inverse_branch = {
                'breq': 'brne', 'brne': 'breq',
                'brlt': 'brge', 'brge': 'brlt'
            }
            
            branch_instruction = 'breq' 
            
            if op == '>':
                self.assembly.append("    cp r22, r24")
                self.assembly.append("    cpc r23, r25")
                branch_instruction = 'brlt'
            elif op == '<=':
                self.assembly.append("    cp r22, r24")
                self.assembly.append("    cpc r23, r25")
                branch_instruction = 'brge'
            else:
                self.assembly.append("    cp r24, r22")
                self.assembly.append("    cpc r25, r23")
                mapping = {
                    '==': 'breq', '!=': 'brne',
                    '<':  'brlt', '>=': 'brge'
                }
                branch_instruction = mapping.get(op, 'breq')

            inv_branch = inverse_branch.get(branch_instruction, 'brne')
            
            self.assembly.append(f"    {inv_branch} {lbl_skip_jump}")
            self.assembly.append(f"    rjmp {lbl_true}")
            self.assembly.append(f"{lbl_skip_jump}:")
            
            self.assembly.append("    ldi r24, 0")
            self.assembly.append("    ldi r25, 0")
            self.assembly.append(f"    rjmp {lbl_end}")
            
            self.assembly.append(f"{lbl_true}:")
            self.assembly.append("    ldi r24, 1")
            self.assembly.append("    ldi r25, 0")
            
            self.assembly.append(f"{lbl_end}:")


# ========== FUNÇÕES AUXILIARES ==========

def salvarAssembly(instructions, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in instructions:
            f.write(f"{line}\n")

def gerarHex(asm_file, hex_file):
    base_name = os.path.splitext(hex_file)[0]
    elf_file = f"{base_name}.elf"
    
    math_lib = "avr_math_lib.s"
    if not os.path.exists(math_lib):
        if os.path.exists(f"../{math_lib}"):
            math_lib = f"../{math_lib}"
        else:
            math_lib_alt = os.path.join(os.path.dirname(asm_file), "..", "avr_math_lib.s")
            if os.path.exists(math_lib_alt):
                math_lib = math_lib_alt

    cmd_compile = [
        "avr-gcc", "-mmcu=atmega328p",
        "-o", elf_file, asm_file, "-nostartfiles"
    ]
    
    if os.path.exists(math_lib):
        cmd_compile.append(math_lib)

    cmd_objcopy = [
        "avr-objcopy", "-O", "ihex",
        "-R", ".eeprom", elf_file, hex_file
    ]

    try:
        print(f"   [CMD] {' '.join(cmd_compile)}")
        result_compile = subprocess.run(cmd_compile, capture_output=True, text=True)
        
        if result_compile.returncode != 0:
            print("   [ERRO] Falha no avr-gcc:")
            print(result_compile.stderr)
            return False

        print(f"   [CMD] {' '.join(cmd_objcopy)}")
        result_objcopy = subprocess.run(cmd_objcopy, capture_output=True, text=True)
        
        if result_objcopy.returncode != 0:
            print("   [ERRO] Falha no avr-objcopy:")
            print(result_objcopy.stderr)
            return False
            
        return True

    except FileNotFoundError:
        print("   [ERRO] Toolchain AVR não encontrada.")
        return False
    except Exception as e:
        print(f"   [ERRO] Exceção: {e}")
        return False

def uploadHex(hex_file, porta_serial, baud_rate=115200):
    print(f"   [UPLOAD] Iniciando upload para {porta_serial}...")
    
    cmd_upload = [
        "avrdude", "-c", "arduino",
        "-p", "ATMEGA328P", "-P", porta_serial,
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
        print("   [ERRO] 'avrdude' não encontrado.")
        return False

def gerarRelatorioAssembly(tac, asm, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório Assembly\n")
        f.write("Gerado com suporte a RES (Histórico de Resultados).\n\n")
        f.write("## Implementação de RES\n\n")
        f.write("O comando `(N RES)` recupera o resultado da expressão N linhas anteriores.\n\n")
        f.write("**Implementação:**\n")
        f.write("1. Durante análise do TAC, rastreia variável final de cada linha\n")
        f.write("2. Armazena em array `res_history[]`\n")
        f.write("3. `RES(N)` carrega valor de `res_history[-N]`\n")
        f.write("4. Imprime valor com `print_int16`\n\n")