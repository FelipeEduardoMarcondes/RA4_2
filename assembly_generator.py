# assembly_generator.py
# FELIPE EDUARDO MARCONDES
# GRUPO 2
# Gerador de código Assembly AVR para Arduino Uno (ATmega328P)

import re


class AVRAssemblyGenerator:
    """
    Gerador de código Assembly AVR compatível com Arduino Uno (ATmega328P).
    
    Convenções de Registradores:
    - R16-R23: Variáveis temporárias (8 registradores)
    - R24-R25: Parâmetros e valores de retorno
    - R26-R27 (X): Ponteiro para dados
    - R28-R29 (Y): Frame pointer
    - R30-R31 (Z): Ponteiro de pilha
    """
    
    def __init__(self):
        self.temp_to_reg = {}  # Mapeamento de temporárias para registradores
        self.reg_counter = 16  # R16 é o primeiro registrador de uso geral
        self.mem_vars = {}     # Mapeamento de variáveis de memória para endereços
        self.mem_counter = 0x100  # Início da SRAM
        self.assembly = []
        self.data_section = []
        
    def gerarAssembly(self, tac_instructions):
        """
        Gera código Assembly AVR a partir de instruções TAC otimizadas.
        
        Args:
            tac_instructions: Lista de instruções TAC
            
        Returns:
            Lista de instruções Assembly
        """
        self.assembly = []
        self.data_section = []
        self.temp_to_reg = {}
        self.mem_vars = {}
        self.reg_counter = 16
        self.mem_counter = 0x100
        
        # Gerar prólogo
        self._gerar_prologo()
        
        # Processar instruções TAC
        for inst in tac_instructions:
            if inst.startswith('#'):
                # Comentário
                self.assembly.append(f"; {inst[1:].strip()}")
            elif ':' in inst and not '=' in inst:
                # Rótulo
                label = inst.strip().rstrip(':')
                self.assembly.append(f"{label}:")
            else:
                # Instrução TAC
                self._processar_instrucao(inst)
        
        # Gerar epílogo
        self._gerar_epilogo()
        
        # Combinar seção de dados + código
        resultado = []
        
        # Seção de dados
        if self.data_section:
            resultado.append("; Seção de dados")
            resultado.append(".data")
            resultado.extend(self.data_section)
            resultado.append("")
        
        # Seção de código
        resultado.append("; Seção de código")
        resultado.append(".text")
        resultado.extend(self.assembly)
        
        return resultado
    
    def _gerar_prologo(self):
        """Gera o prólogo do programa Assembly."""
        self.assembly.extend([
            "; Prólogo do programa",
            ".include \"m328Pdef.inc\"",
            "",
            ".org 0x0000",
            "    rjmp main",
            "",
            "main:",
            "    ; Inicializar pilha",
            "    ldi r16, high(RAMEND)",
            "    out SPH, r16",
            "    ldi r16, low(RAMEND)",
            "    out SPL, r16",
            "",
            "    ; Inicializar registradores",
            "    clr r1              ; R1 sempre zero (convenção AVR-GCC)",
            "",
        ])
    
    def _gerar_epilogo(self):
        """Gera o epílogo do programa Assembly."""
        self.assembly.extend([
            "",
            "fim:",
            "    ; Loop infinito no final",
            "    rjmp fim",
            "",
        ])
    
    def _processar_instrucao(self, inst):
        """Processa uma instrução TAC e gera Assembly correspondente."""
        inst = inst.strip()
        
        if not inst or inst.startswith('#'):
            return
        
        # Comentário com a instrução TAC original
        self.assembly.append(f"    ; TAC: {inst}")
        
        # Atribuição simples: t1 = num
        match = re.match(r'(t\d+)\s*=\s*(-?\d+\.?\d*)$', inst)
        if match:
            self._atribuicao_simples(match)
            return
        
        # Operação binária: t1 = t2 op t3 ou t1 = num op num
        match = re.match(r'(t\d+)\s*=\s*(\S+)\s*([+\-*/%^|]|[<>]=?|[!=]=)\s*(\S+)', inst)
        if match:
            self._operacao_binaria(match)
            return
        
        # Acesso à memória: t1 = MEM[var]
        match = re.match(r'(t\d+)\s*=\s*MEM\[(\w+)\]', inst)
        if match:
            self._carregar_memoria(match)
            return
        
        # Armazenar em memória: MEM[var] = t1
        match = re.match(r'MEM\[(\w+)\]\s*=\s*(t\d+)', inst)
        if match:
            self._armazenar_memoria(match)
            return
        
        # Salto incondicional: goto L1
        match = re.match(r'goto\s+(\w+)', inst)
        if match:
            self._salto_incondicional(match)
            return
        
        # Salto condicional: ifFalse t1 goto L1
        match = re.match(r'ifFalse\s+(t\d+)\s+goto\s+(\w+)', inst)
        if match:
            self._salto_condicional(match)
            return
        
        # RES: t1 = RES[t2]
        match = re.match(r'(t\d+)\s*=\s*RES\[(t\d+)\]', inst)
        if match:
            self._acessar_historico(match)
            return
        
        # Instrução não reconhecida
        self.assembly.append(f"    ; AVISO: Instrução não mapeada: {inst}")
    
    def _atribuicao_simples(self, match):
        """t1 = num"""
        temp, valor = match.groups()
        reg = self._obter_registrador(temp)
        
        # Verificar se é float ou int
        if '.' in valor:
            # Float - por simplicidade, vamos converter para int16 escalado
            float_val = float(valor)
            int_val = int(float_val * 100)  # Escalar por 100
            self.assembly.append(f"    ldi {reg}, {int_val & 0xFF}")
            self.assembly.append(f"    ; Float {valor} escalado como {int_val}")
        else:
            # Integer
            int_val = int(float(valor))
            if -128 <= int_val <= 127:
                self.assembly.append(f"    ldi {reg}, {int_val}")
            else:
                # Valor grande, usar 16 bits
                self.assembly.append(f"    ldi {reg}, {int_val & 0xFF}")
                self.assembly.append(f"    ; Valor de 16 bits: {int_val}")
        
        self.assembly.append("")
    
    def _operacao_binaria(self, match):
        """t1 = t2 op t3"""
        dest, left, op, right = match.groups()
        
        reg_dest = self._obter_registrador(dest)
        
        # Obter operandos
        if left.startswith('t'):
            reg_left = self._obter_registrador(left)
        else:
            # Constante
            reg_left = 'r24'
            valor = int(float(left))
            self.assembly.append(f"    ldi {reg_left}, {valor}")
        
        if right.startswith('t'):
            reg_right = self._obter_registrador(right)
        else:
            # Constante
            reg_right = 'r25'
            valor = int(float(right))
            self.assembly.append(f"    ldi {reg_right}, {valor}")
        
        # Copiar left para dest (se necessário)
        if reg_left != reg_dest:
            self.assembly.append(f"    mov {reg_dest}, {reg_left}")
        
        # Aplicar operação
        if op == '+':
            self.assembly.append(f"    add {reg_dest}, {reg_right}")
        elif op == '-':
            self.assembly.append(f"    sub {reg_dest}, {reg_right}")
        elif op == '*':
            self._multiplicacao(reg_dest, reg_left, reg_right)
        elif op == '/':
            self._divisao_inteira(reg_dest, reg_left, reg_right)
        elif op == '|':
            self._divisao_real(reg_dest, reg_left, reg_right)
        elif op == '%':
            self._modulo(reg_dest, reg_left, reg_right)
        elif op == '^':
            self._potenciacao(reg_dest, reg_left, reg_right)
        elif op in ['<', '>', '<=', '>=', '==', '!=']:
            self._comparacao(reg_dest, reg_left, reg_right, op)
        
        self.assembly.append("")
    
    def _multiplicacao(self, dest, left, right):
        """Multiplicação usando instrução mul."""
        self.assembly.append(f"    mul {left}, {right}  ; Mult 8x8=16 bits em R1:R0")
        self.assembly.append(f"    mov {dest}, r0       ; Pegar byte baixo")
    
    def _divisao_inteira(self, dest, left, right):
        """Divisão inteira (simplificada)."""
        self.assembly.append(f"    ; Divisão inteira: {left} / {right}")
        self.assembly.append(f"    call div8u           ; Rotina de divisão")
        self.assembly.append(f"    mov {dest}, r24      ; Resultado em R24")
    
    def _divisao_real(self, dest, left, right):
        """Divisão real (ponto flutuante simplificado)."""
        self.assembly.append(f"    ; Divisão real: {left} | {right}")
        self.assembly.append(f"    call divfloat16      ; Rotina de divisão float")
        self.assembly.append(f"    mov {dest}, r24      ; Resultado em R24:R25")
    
    def _modulo(self, dest, left, right):
        """Módulo (resto da divisão)."""
        self.assembly.append(f"    ; Módulo: {left} % {right}")
        self.assembly.append(f"    call mod8u           ; Rotina de módulo")
        self.assembly.append(f"    mov {dest}, r25      ; Resto em R25")
    
    def _potenciacao(self, dest, left, right):
        """Potenciação."""
        self.assembly.append(f"    ; Potenciação: {left} ^ {right}")
        self.assembly.append(f"    call pow8u           ; Rotina de potência")
        self.assembly.append(f"    mov {dest}, r24      ; Resultado em R24")
    
    def _comparacao(self, dest, left, right, op):
        """Operadores relacionais."""
        self.assembly.append(f"    cp {left}, {right}   ; Comparar {left} com {right}")
        
        # Mapear operador para branch
        branch_map = {
            '<': 'brlt',   # Branch if less than
            '>': 'brlt',   # Inverter ordem para >
            '<=': 'brge',  # Branch if greater or equal (negado)
            '>=': 'brge',  # Branch if greater or equal
            '==': 'breq',  # Branch if equal
            '!=': 'brne'   # Branch if not equal
        }
        
        branch = branch_map.get(op, 'breq')
        label_true = f"cmp_true_{id(dest)}"
        label_end = f"cmp_end_{id(dest)}"
        
        if op == '>':
            # Para >, inverter: right < left
            self.assembly.append(f"    cp {right}, {left}")
        
        self.assembly.append(f"    {branch} {label_true}")
        self.assembly.append(f"    ldi {dest}, 0        ; Falso")
        self.assembly.append(f"    rjmp {label_end}")
        self.assembly.append(f"{label_true}:")
        self.assembly.append(f"    ldi {dest}, 1        ; Verdadeiro")
        self.assembly.append(f"{label_end}:")
    
    def _carregar_memoria(self, match):
        """t1 = MEM[var]"""
        temp, var_name = match.groups()
        reg = self._obter_registrador(temp)
        
        # Alocar endereço se necessário
        if var_name not in self.mem_vars:
            self.mem_vars[var_name] = self.mem_counter
            self.data_section.append(f"{var_name}: .byte 2  ; 0x{self.mem_counter:04X}")
            self.mem_counter += 2
        
        addr = self.mem_vars[var_name]
        
        self.assembly.append(f"    lds {reg}, {var_name}  ; Carregar de 0x{addr:04X}")
        self.assembly.append("")
    
    def _armazenar_memoria(self, match):
        """MEM[var] = t1"""
        var_name, temp = match.groups()
        reg = self._obter_registrador(temp)
        
        # Alocar endereço se necessário
        if var_name not in self.mem_vars:
            self.mem_vars[var_name] = self.mem_counter
            self.data_section.append(f"{var_name}: .byte 2  ; 0x{self.mem_counter:04X}")
            self.mem_counter += 2
        
        addr = self.mem_vars[var_name]
        
        self.assembly.append(f"    sts {var_name}, {reg}  ; Armazenar em 0x{addr:04X}")
        self.assembly.append("")
    
    def _salto_incondicional(self, match):
        """goto L1"""
        label = match.group(1)
        self.assembly.append(f"    rjmp {label}")
        self.assembly.append("")
    
    def _salto_condicional(self, match):
        """ifFalse t1 goto L1"""
        temp, label = match.groups()
        reg = self._obter_registrador(temp)
        
        self.assembly.append(f"    cpi {reg}, 0         ; Comparar com zero")
        self.assembly.append(f"    breq {label}         ; Saltar se zero (falso)")
        self.assembly.append("")
    
    def _acessar_historico(self, match):
        """t1 = RES[t2]"""
        dest, index = match.groups()
        reg_dest = self._obter_registrador(dest)
        reg_index = self._obter_registrador(index)
        
        self.assembly.append(f"    ; RES[{index}] - histórico não implementado")
        self.assembly.append(f"    ldi {reg_dest}, 0    ; Placeholder")
        self.assembly.append("")
    
    def _obter_registrador(self, temp_var):
        """Aloca ou retorna registrador para uma variável temporária."""
        if temp_var not in self.temp_to_reg:
            if self.reg_counter > 23:
                # Sem registradores disponíveis - usar pilha ou reutilizar
                self.reg_counter = 16
            
            reg = f"r{self.reg_counter}"
            self.temp_to_reg[temp_var] = reg
            self.reg_counter += 1
        
        return self.temp_to_reg[temp_var]


def salvarAssembly(instructions, filename):
    """Salva código Assembly em arquivo .s"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("; Assembly AVR para Arduino Uno (ATmega328P)\n")
        f.write("; Gerado automaticamente\n\n")
        
        for inst in instructions:
            f.write(f"{inst}\n")


def gerarHex(asm_file, hex_file):
    """
    Compila Assembly para HEX usando avr-gcc.
    
    Requer toolchain AVR instalada:
    - avr-gcc
    - avr-objcopy
    """
    import subprocess
    import os
    
    try:
        # Compilar .s para .o
        obj_file = asm_file.replace('.s', '.o')
        cmd_compile = [
            'avr-gcc',
            '-mmcu=atmega328p',
            '-c',
            asm_file,
            '-o', obj_file
        ]
        
        subprocess.run(cmd_compile, check=True)
        
        # Linkar para .elf
        elf_file = asm_file.replace('.s', '.elf')
        cmd_link = [
            'avr-gcc',
            '-mmcu=atmega328p',
            obj_file,
            '-o', elf_file
        ]
        
        subprocess.run(cmd_link, check=True)
        
        # Gerar .hex
        cmd_hex = [
            'avr-objcopy',
            '-O', 'ihex',
            '-R', '.eeprom',
            elf_file,
            hex_file
        ]
        
        subprocess.run(cmd_hex, check=True)
        
        # Limpar arquivos temporários
        if os.path.exists(obj_file):
            os.remove(obj_file)
        if os.path.exists(elf_file):
            os.remove(elf_file)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao compilar Assembly: {e}")
        return False
    except FileNotFoundError:
        print("Erro: Toolchain AVR não encontrada. Instale avr-gcc e avr-objcopy.")
        return False


def gerarRelatorioAssembly(tac_instructions, asm_instructions, filename):
    """Gera relatório markdown comparando TAC e Assembly."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Geração de Assembly AVR\n\n")
        f.write("**Gerado automaticamente**\n\n")
        
        f.write("## Estatísticas\n\n")
        f.write(f"- **Instruções TAC:** {len(tac_instructions)}\n")
        f.write(f"- **Instruções Assembly:** {len(asm_instructions)}\n")
        f.write(f"- **Razão:** {len(asm_instructions)/len(tac_instructions):.2f} instruções Assembly por TAC\n\n")
        
        f.write("## Convenções de Registradores\n\n")
        f.write("| Registrador | Uso |\n")
        f.write("|-------------|-----|\n")
        f.write("| R0-R1 | Resultado de MUL, R1 sempre zero |\n")
        f.write("| R16-R23 | Variáveis temporárias |\n")
        f.write("| R24-R25 | Parâmetros e retorno |\n")
        f.write("| R26-R27 (X) | Ponteiro de dados |\n")
        f.write("| R28-R29 (Y) | Frame pointer |\n")
        f.write("| R30-R31 (Z) | Ponteiro de pilha |\n\n")
        
        f.write("## Mapeamento TAC → Assembly\n\n")
        f.write("### Operações Aritméticas\n\n")
        f.write("```\n")
        f.write("TAC: t1 = t2 + t3\n")
        f.write("ASM: mov r16, r17\n")
        f.write("     add r16, r18\n\n")
        f.write("TAC: t1 = t2 * t3\n")
        f.write("ASM: mul r17, r18\n")
        f.write("     mov r16, r0\n")
        f.write("```\n\n")
        
        f.write("### Acesso à Memória\n\n")
        f.write("```\n")
        f.write("TAC: t1 = MEM[X]\n")
        f.write("ASM: lds r16, X\n\n")
        f.write("TAC: MEM[X] = t1\n")
        f.write("ASM: sts X, r16\n")
        f.write("```\n\n")
        
        f.write("### Saltos e Rótulos\n\n")
        f.write("```\n")
        f.write("TAC: goto L1\n")
        f.write("ASM: rjmp L1\n\n")
        f.write("TAC: ifFalse t1 goto L1\n")
        f.write("ASM: cpi r16, 0\n")
        f.write("     breq L1\n")
        f.write("```\n\n")
        
        f.write("## Código Assembly Completo\n\n")
        f.write("```asm\n")
        for inst in asm_instructions[:50]:  # Primeiras 50 linhas
            f.write(f"{inst}\n")
        if len(asm_instructions) > 50:
            f.write("...\n")
        f.write("```\n")