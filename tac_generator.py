# tac_generator.py
# FELIPE EDUARDO MARCONDES - GRUPO 2
# Gerador de Three Address Code (TAC)

class TACGenerator:
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.instructions = []
        
    def new_temp(self):
        # Cria uma nova variável temporária.
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1

        return temp
    
    def new_label(self):
        # Cria um novo rótulo.
        label = f"L{self.label_counter}"
        self.label_counter += 1

        return label
    
    def emit(self, instruction):
        # Adiciona uma instrução TAC.
        self.instructions.append(instruction)

        return instruction
    
    def gerarTAC(self, arvore_atribuida):
        self.instructions = []
        self.temp_counter = 0
        self.label_counter = 0
        
        for linha_num, ast in arvore_atribuida:
            self.emit(f"# Linha {linha_num}")
            
            # Gera código da expressão
            resultado_temp = self._gerar_expressao(ast)
            
            # Tipos que não devem aparecer no Serial
            tipos_silenciosos = ['store', 'if', 'while']
            
            if resultado_temp:
                # [CORREÇÃO] Passo 1:
                # Sempre gera instrução para salvar no histórico, independente do tipo.
                # O comando 'HIST' deve apenas salvar, sem imprimir.
                self.emit(f"HIST[{resultado_temp}]")

                # Passo 2:
                # Só gera o PRINT se não for silencioso
                if ast['type'] not in tipos_silenciosos:
                    # Para RES, usamos o valor retornado, mas ele já foi salvo pelo HIST acima?
                    # Geralmente RES apenas lê. Se RES for "visualizar histórico", ele imprime.
                    print_temp = self.new_temp()
                    self.emit(f"{print_temp} = PRINT[{resultado_temp}]")
            
        return self.instructions
    def _gerar_expressao(self, node):
        
        # Gera TAC para um nó da árvore recursivamente.
        # Retorna o nome da variável/temporária que contém o resultado.
        
        if node is None:

            return None
        
        node_type = node['type']
        
        # Literais
        if node_type == 'num':
            temp = self.new_temp()
            self.emit(f"{temp} = {node['value']}")

            return temp
        
        # Identificadores (recuperação de memória)
        if node_type == 'id':
            temp = self.new_temp()
            self.emit(f"{temp} = MEM[{node['value']}]")

            return temp
        
        # Armazenamento (V MEM)
        if node_type == 'store':
            valor_node = node['children'][0]
            id_node = node['children'][1]
            
            valor_temp = self._gerar_expressao(valor_node)
            mem_name = id_node['value']
            
            self.emit(f"MEM[{mem_name}] = {valor_temp}")
            return valor_temp
        
        # Histórico (N RES)
        if node_type == 'res':
            n_node = node['children'][0]
            n_temp = self._gerar_expressao(n_node)
            
            temp = self.new_temp()
            # RES busca do histórico
            self.emit(f"{temp} = RES[{n_temp}]")

            return temp
        
        # Operadores binários aritméticos
        if node_type in ['plus', 'minus', 'mult', 'div_real', 'div_int', 'mod', 'pow']:
            left = self._gerar_expressao(node['children'][0])
            right = self._gerar_expressao(node['children'][1])
            
            op_map = {
                'plus': '+',
                'minus': '-',
                'mult': '*',
                'div_real': '|',
                'div_int': '/',
                'mod': '%',
                'pow': '^'
            }
            
            op = op_map[node_type]
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")

            return temp
        
        # Operadores relacionais
        if node_type in ['lt', 'gt', 'lte', 'gte', 'eq', 'neq']:
            left = self._gerar_expressao(node['children'][0])
            right = self._gerar_expressao(node['children'][1])
            
            op_map = {
                'lt': '<',
                'gt': '>',
                'lte': '<=',
                'gte': '>=',
                'eq': '==',
                'neq': '!='
            }
            
            op = op_map[node_type]
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")

            return temp
        
        # Condicional (IF)
        if node_type == 'if':
            cond_node = node['children'][0]
            then_node = node['children'][1]
            else_node = node['children'][2]
            
            cond_temp = self._gerar_expressao(cond_node)
            
            label_else = self.new_label()
            label_end = self.new_label()
            result_temp = self.new_temp()
            
            self.emit(f"ifFalse {cond_temp} goto {label_else}")
            
            then_temp = self._gerar_expressao(then_node)
            self.emit(f"{result_temp} = {then_temp}")
            self.emit(f"goto {label_end}")
            
            self.emit(f"{label_else}:")
            else_temp = self._gerar_expressao(else_node)
            self.emit(f"{result_temp} = {else_temp}")
            
            self.emit(f"{label_end}:")
            
            return result_temp
        
        # Laço (WHILE)
        if node_type == 'while':
            cond_node = node['children'][0]
            body_node = node['children'][1]
            
            label_start = self.new_label()
            label_end = self.new_label()
            result_temp = self.new_temp()
            
            self.emit(f"{label_start}:")
            cond_temp = self._gerar_expressao(cond_node)
            self.emit(f"ifFalse {cond_temp} goto {label_end}")
            
            body_temp = self._gerar_expressao(body_node)
            self.emit(f"{result_temp} = {body_temp}")
            self.emit(f"goto {label_start}")
            
            self.emit(f"{label_end}:")
            
            return result_temp
        
        return None


def salvarTAC(instructions, filename):
    # Salva instruções TAC em arquivo.
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Three Address Code (TAC)\n")
        f.write("# Gerado automaticamente\n")
        
        for inst in instructions:

            if inst.startswith('#'):
                f.write(f"\n{inst}\n")

            else:
                f.write(f"{inst}\n")