# otimizador.py
# FELIPE EDUARDO MARCONDES - GRUPO 2
# Otimizador de Three Address Code (TAC) - CORRIGIDO

import re


class TACOptimizer:
    def __init__(self):
        self.optimizations_applied = {
            'constant_folding': 0,
            'constant_propagation': 0,
            'dead_code_elimination': 0,
            'redundant_jumps': 0
        }
    
    def otimizarTAC(self, instructions):
        """
        Aplica otimizações no código TAC.
        
        Args:
            instructions: Lista de instruções TAC
            
        Returns:
            Lista de instruções TAC otimizadas
        """
        optimized = instructions.copy()
        
        # Múltiplas passagens para permitir otimizações em cascata
        max_iterations = 5
        for _ in range(max_iterations):
            old_size = len(optimized)
            
            optimized = self._constant_folding(optimized)
            optimized = self._constant_propagation(optimized)
            optimized = self._dead_code_elimination(optimized)
            optimized = self._eliminate_redundant_jumps(optimized)
            
            # Se não houve mudança, podemos parar
            if len(optimized) == old_size:
                break
        
        return optimized
    
    def _constant_folding(self, instructions):
        """
        Avalia expressões constantes em tempo de compilação.
        Exemplo: t1 = 2 + 3 -> t1 = 5
        """
        optimized = []
        
        for inst in instructions:
            if inst.startswith('#') or ':' in inst:
                optimized.append(inst)
                continue
            
            # Padrão: t1 = num1 op num2
            match = re.match(r'(\w+)\s*=\s*(-?\d+\.?\d*)\s*([+\-*/%^|])\s*(-?\d+\.?\d*)', inst)
            if match:
                var, left, op, right = match.groups()
                
                try:
                    left_val = float(left) if '.' in left else int(left)
                    right_val = float(right) if '.' in right else int(right)
                    
                    # Avaliar a operação
                    result = None
                    if op == '+':
                        result = left_val + right_val
                    elif op == '-':
                        result = left_val - right_val
                    elif op == '*':
                        result = left_val * right_val
                    elif op == '/':
                        if right_val != 0:
                            result = int(left_val // right_val)
                    elif op == '|':
                        if right_val != 0:
                            result = left_val / right_val
                    elif op == '%':
                        if right_val != 0:
                            result = int(left_val % right_val)
                    elif op == '^':
                        if isinstance(right_val, int) and right_val > 0:
                            result = left_val ** right_val
                    
                    if result is not None:
                        # Manter tipo int ou float
                        if isinstance(result, float) and result.is_integer() and op not in ['|']:
                            result = int(result)
                        
                        optimized.append(f"{var} = {result}")
                        self.optimizations_applied['constant_folding'] += 1
                        continue
                        
                except (ValueError, ZeroDivisionError):
                    pass
            
            # Padrão para comparações: t1 = num1 op num2 (onde op é <, >, ==, etc)
            match = re.match(r'(\w+)\s*=\s*(-?\d+\.?\d*)\s*([<>]=?|[!=]=)\s*(-?\d+\.?\d*)', inst)
            if match:
                var, left, op, right = match.groups()
                
                try:
                    left_val = float(left) if '.' in left else int(left)
                    right_val = float(right) if '.' in right else int(right)
                    
                    result = None
                    if op == '<':
                        result = 1 if left_val < right_val else 0
                    elif op == '>':
                        result = 1 if left_val > right_val else 0
                    elif op == '<=':
                        result = 1 if left_val <= right_val else 0
                    elif op == '>=':
                        result = 1 if left_val >= right_val else 0
                    elif op == '==':
                        result = 1 if left_val == right_val else 0
                    elif op == '!=':
                        result = 1 if left_val != right_val else 0
                    
                    if result is not None:
                        optimized.append(f"{var} = {result}")
                        self.optimizations_applied['constant_folding'] += 1
                        continue
                        
                except ValueError:
                    pass
            
            optimized.append(inst)
        
        return optimized
    
    def _constant_propagation(self, instructions):
        """
        Propaga valores constantes através do código.
        Exemplo: t1 = 5; t2 = t1 + 3 -> t1 = 5; t2 = 8
        """
        optimized = []
        constants = {}
        
        for inst in instructions:
            if inst.startswith('#') or ':' in inst:
                optimized.append(inst)
                # Rótulos invalidam constantes (podem ser alvos de saltos)
                if ':' in inst:
                    constants.clear()
                continue
            
            # Detectar atribuições de constantes: t1 = num
            match = re.match(r'(\w+)\s*=\s*(-?\d+\.?\d*)$', inst)
            if match:
                var, value = match.groups()
                constants[var] = value
                optimized.append(inst)
                continue
            
            # Substituir variáveis por constantes conhecidas
            new_inst = inst
            for var, value in constants.items():
                # Substituir variável por constante em expressões
                # Padrão: t2 = t1 op ...
                new_inst = re.sub(rf'\b{var}\b', value, new_inst)
            
            # Se houve substituição, marcar otimização
            if new_inst != inst:
                self.optimizations_applied['constant_propagation'] += 1
            
            optimized.append(new_inst)
            
            # Se a instrução modifica uma variável, remover das constantes
            match = re.match(r'(\w+)\s*=', new_inst)
            if match:
                modified_var = match.group(1)
                if modified_var in constants:
                    del constants[modified_var]
            
            # Limpar constantes após saltos ou condicionais
            if 'goto' in new_inst or 'ifFalse' in new_inst:
                constants.clear()
        
        return optimized
    
    def _dead_code_elimination(self, instructions):
        """
        Remove código morto (variáveis que nunca são usadas).
        
        CRÍTICO: NÃO remove instruções com efeitos colaterais:
        - PRINT[...]
        - MEM[...]
        - RES[...]
        - goto/ifFalse
        """
        # Primeira passagem: encontrar todas as variáveis usadas
        used_vars = set()
        
        for inst in instructions:
            if inst.startswith('#') or ':' in inst:
                continue
            
            # --- CORREÇÃO AQUI (Passagem 1) ---
            # Removemos 'goto' e 'ifFalse' desta lista para que caiam na verificação específica abaixo
            if any(keyword in inst for keyword in ['PRINT[', 'MEM[', 'RES[']):
                # Marca TODAS as variáveis do lado direito como usadas
                parts = inst.split('=')
                if len(parts) > 1:
                    right_side = parts[1]
                    used_in_right = re.findall(r'\b(t\d+|[A-Z_][A-Z0-9_]*)\b', right_side)
                    used_vars.update(used_in_right)
                continue
            
            # Variáveis usadas no lado direito (Atribuições normais)
            if '=' in inst:
                _, right_side = inst.split('=', 1)
                used_in_right = re.findall(r'\b(t\d+)\b', right_side)
                used_vars.update(used_in_right)
            
            # Variáveis usadas em condicionais (AGORA O CÓDIGO CHEGA AQUI)
            if 'ifFalse' in inst or 'goto' in inst:
                used_in_cond = re.findall(r'\b(t\d+)\b', inst)
                used_vars.update(used_in_cond)
        
        # Segunda passagem: remover atribuições a variáveis não usadas
        optimized = []
        
        for inst in instructions:
            if inst.startswith('#') or ':' in inst:
                optimized.append(inst)
                continue
            
            # --- MANTER ISTO (Passagem 2) ---
            # Aqui mantemos 'goto' e 'ifFalse' para não removê-las da saída
            if any(keyword in inst for keyword in ['PRINT[', 'MEM[', 'RES[', 'goto', 'ifFalse']):
                optimized.append(inst)
                continue
            
            # Verificar se é uma atribuição simples a uma temporária
            match = re.match(r'(t\d+)\s*=', inst)
            if match:
                var = match.group(1)
                
                # Se a variável não é usada E não tem efeitos colaterais, remover
                if var not in used_vars:
                    self.optimizations_applied['dead_code_elimination'] += 1
                    continue
            
            optimized.append(inst)
        
        return optimized
    def _eliminate_redundant_jumps(self, instructions):
        """
        Remove saltos redundantes (saltos para a próxima instrução).
        """
        optimized = []
        
        for i, inst in enumerate(instructions):
            # Detectar goto L1 seguido imediatamente por L1:
            if 'goto' in inst and not 'ifFalse' in inst:
                match = re.match(r'goto\s+(\w+)', inst)
                if match:
                    target = match.group(1)
                    
                    # Verificar se a próxima instrução é o rótulo alvo
                    if i + 1 < len(instructions):
                        next_inst = instructions[i + 1]
                        if next_inst.strip() == f"{target}:":
                            self.optimizations_applied['redundant_jumps'] += 1
                            continue
            
            optimized.append(inst)
        
        return optimized
    
    def get_optimization_stats(self):
        """Retorna estatísticas das otimizações aplicadas."""
        return self.optimizations_applied.copy()


def salvarTACOtimizado(instructions, filename):
    """Salva instruções TAC otimizadas em arquivo."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Three Address Code (TAC) - Otimizado\n")
        f.write("# Gerado automaticamente\n")
        f.write("# INSTRUÇÕES PRINT E RES SÃO PRESERVADAS\n\n")
        
        for inst in instructions:
            if inst.startswith('#'):
                f.write(f"\n{inst}\n")
            else:
                f.write(f"{inst}\n")


def gerarRelatorioOtimizacoes(tac_original, tac_otimizado, stats, filename):
    """Gera relatório markdown com as otimizações aplicadas."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Otimizações de Código\n\n")
        f.write("**Gerado automaticamente pelo otimizador TAC**\n\n")
        
        f.write("## Estatísticas\n\n")
        f.write(f"- **Instruções originais:** {len(tac_original)}\n")
        f.write(f"- **Instruções otimizadas:** {len(tac_otimizado)}\n")
        
        reducao = len(tac_original) - len(tac_otimizado)
        if len(tac_original) > 0:
            perc = 100 * reducao / len(tac_original)
        else:
            perc = 0
            
        f.write(f"- **Redução:** {reducao} instruções ({perc:.1f}%)\n\n")
        
        f.write("## Otimizações Aplicadas\n\n")
        
        for opt_name, count in stats.items():
            opt_title = opt_name.replace('_', ' ').title()
            f.write(f"### {opt_title}\n\n")
            f.write(f"**Aplicações:** {count}\n\n")
            
            if opt_name == 'constant_folding':
                f.write("**Descrição:** Avalia expressões constantes em tempo de compilação.\n\n")
                f.write("**Exemplo:**\n")
                f.write("```\n")
                f.write("Antes: t1 = 2 + 3\n")
                f.write("Depois: t1 = 5\n")
                f.write("```\n\n")
            
            elif opt_name == 'constant_propagation':
                f.write("**Descrição:** Propaga valores constantes através do código.\n\n")
                f.write("**Exemplo:**\n")
                f.write("```\n")
                f.write("Antes: t1 = 5\n")
                f.write("       t2 = t1 + 3\n")
                f.write("Depois: t1 = 5\n")
                f.write("        t2 = 5 + 3\n")
                f.write("        (que será reduzido para t2 = 8)\n")
                f.write("```\n\n")
            
            elif opt_name == 'dead_code_elimination':
                f.write("**Descrição:** Remove código que não afeta o resultado do programa.\n\n")
                f.write("**IMPORTANTE:** Preserva instruções com efeitos colaterais (PRINT, MEM, RES).\n\n")
                f.write("**Exemplo:**\n")
                f.write("```\n")
                f.write("Antes: t1 = 5\n")
                f.write("       t2 = 3  # t2 nunca é usado\n")
                f.write("       t3 = t1 + 2\n")
                f.write("Depois: t1 = 5\n")
                f.write("        t3 = t1 + 2\n")
                f.write("```\n\n")
            
            elif opt_name == 'redundant_jumps':
                f.write("**Descrição:** Remove saltos para a próxima instrução.\n\n")
                f.write("**Exemplo:**\n")
                f.write("```\n")
                f.write("Antes: goto L1\n")
                f.write("       L1:\n")
                f.write("Depois: L1:\n")
                f.write("```\n\n")
        
        f.write("## Comparação de Código\n\n")
        f.write("### TAC Original\n\n")
        f.write("```\n")
        for inst in tac_original:
            f.write(f"{inst}\n")
        f.write("```\n\n")
        
        f.write("### TAC Otimizado\n\n")
        f.write("```\n")
        for inst in tac_otimizado:
            f.write(f"{inst}\n")
        f.write("```\n\n")