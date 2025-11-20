# semantico.py
# FELIPE EDUARDO MARCONDES
# GRUPO 2

import json


def inicializarTabelaSimbolos():
    # Inicializa e retorna uma nova estrutura de tabela de símbolos.
    return {
        'simbolos': {},  # {nome: {tipo, valor, inicializada, linha}}
        'historico': []  # [{tipo, valor, linha}]
    }

def adicionarSimbolo(tabela, nome, tipo, valor, linha):
    # Adiciona ou atualiza uma variável na tabela.
    tabela['simbolos'][nome] = {
        'tipo': tipo,
        'valor': valor,
        'inicializada': True,
        'linha': linha
    }
    

def buscarSimbolo(tabela, nome):
    # Busca uma variável na tabela.
    return tabela['simbolos'].get(nome)

def tabelaEstaInicializada(tabela, nome):
    # Verifica se uma variável foi inicializada.
    simbolo = tabela['simbolos'].get(nome)

    return simbolo and simbolo.get('inicializada', False)

def adicionarSimboloHistorico(tabela, tipo, valor, linha):
    # Adiciona resultado ao histórico de expressões.
    tabela['historico'].append({'tipo': tipo, 'valor': valor, 'linha': linha})

def buscarSimboloHistorico(tabela, n):
    # Busca resultado N linhas anteriores
    # N=1 significa linha imediatamente anterior
    # N deve estar entre 1 e len(historico)
    if n < 1 or n > len(tabela['historico']):

        return None
    
    return tabela['historico'][-n]


def promoverTipo(tipo1, tipo2):

    if tipo1 == 'real' or tipo2 == 'real':
        return 'real'
    

    return 'int'


def definirGramaticaAtributos():
    # Define as regras semânticas da linguagem.
    return {
        'regras_tipo': {
            'plus': promoverTipo,
            'minus': promoverTipo,
            'mult': promoverTipo,
            'div_real': lambda t1, t2: promoverTipo(t1, t2),
            'div_int': lambda t1, t2: 'int' if t1 == 'int' and t2 == 'int' else None,
            'mod': lambda t1, t2: 'int' if t1 == 'int' and t2 == 'int' else None,
            'pow': lambda t1, t2: t1 if t2 == 'int' else None,
            'lt': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
            'gt': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
            'lte': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
            'gte': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
            'eq': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
            'neq': lambda t1, t2: 'booleano' if t1 in ['int', 'real'] and t2 in ['int', 'real'] else None,
        },
        'descricao': """
        Gramática de Atributos - Linguagem RPN
        
        Atributos principais:
        - tipo: {int, real, booleano}
        - valor: valor calculado (quando aplicável)
        - inicializada: boolean (para identificadores)
        - linha: número da linha no código fonte
        """
    }


def inferirTipoNode(node, tabela_simbolos, erros, linha_atual):
    # Infere o tipo de um nó da árvore recursivamente.
    
    if node is None:
        return None
    
    node_type = node['type']
    
    # ========== LITERAIS ==========
    if node_type == 'num':
        valor = node['value']
        if isinstance(valor, int):
            return 'int'
        else:
            return 'real'
    
    # ========== IDENTIFICADORES (RECUPERAÇÃO) ==========
    if node_type == 'id':
        nome = node['value']
        simbolo = buscarSimbolo(tabela_simbolos, nome)
        
        if not simbolo:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Memória '{nome}' utilizada sem inicialização\n"
                         f"Contexto: ({nome})")
            return None
        
        if not simbolo.get('inicializada', False):
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Memória '{nome}' declarada mas não inicializada\n"
                         f"Contexto: ({nome})")
            return None
        
        return simbolo['tipo']
    
   # ========== RES (HISTÓRICO) ==========
    if node_type == 'res':
        if not node['children']:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"RES requer um argumento inteiro\n"
                         f"Contexto: (RES)")
            return None
        
        n_node = node['children'][0]
        n_tipo = inferirTipoNode(n_node, tabela_simbolos, erros, linha_atual)
        
        n_node['tipo_inferido'] = n_tipo

        if n_tipo != 'int':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Argumento de RES deve ser inteiro, encontrado '{n_tipo}'\n"
                         f"Contexto: ({n_node.get('value', '?')} RES)")
            return None
        
        # Validar se N é literal e válido
        if n_node['type'] == 'num':
            n = n_node['value']

            if n < 1:
                erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                             f"RES requer valor positivo (>= 1), encontrado {n}\n"
                             f"Contexto: ({n} RES)")
                
                return None

            # Verificar se N não excede o número de linhas ANTERIORES
            num_linhas_anteriores = len(tabela_simbolos['historico']) 
            
            if n > num_linhas_anteriores:
                erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                             f"RES({n}) referencia linha inexistente\n"
                             f"Só existem {num_linhas_anteriores} expressões anteriores\n"
                             f"Contexto: ({n} RES)")
                
                return None
            
            # Busca o tipo real do histórico
            historico_entry = buscarSimboloHistorico(tabela_simbolos, n)
            if historico_entry and historico_entry['tipo']:

                return historico_entry['tipo']
            
            else:
                erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                             f"RES({n}) referencia expressão inválida\n"
                             f"Contexto: ({n} RES)")
                return None


        if n_node['type'] != 'num':
             erros.append(f"AVISO SEMÂNTICO [Linha {linha_atual}]: "
                         f"RES usado com variável ({n_node['value']}). "
                         f"Tipo não pode ser verificado estaticamente.\n"
                         f"Contexto: ({n_node['value']} RES)")

             return None
                
        return 'int'
    
    # ========== ARMAZENAMENTO (V MEM) ==========
    if node_type == 'store':
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Armazenamento requer valor e identificador")
            
            return None
        
        valor_node = node['children'][0]
        id_node = node['children'][1]
        
        tipo_valor = inferirTipoNode(valor_node, tabela_simbolos, erros, linha_atual)
        
        valor_node['tipo_inferido'] = tipo_valor
        id_node['tipo_inferido'] = None

        if tipo_valor is None:

            return None
        
        if tipo_valor == 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Não é permitido armazenar valores booleanos em memória\n"
                         f"Contexto: (... {id_node['value']})")
            
            return None
        
        nome = id_node['value']
        
        adicionarSimbolo(tabela_simbolos, nome, tipo_valor, None, linha_atual)
        
        return tipo_valor

    # ========== OPERADORES ARITMÉTICOS BINÁRIOS ==========
    if node_type in ['plus', 'minus', 'mult']:
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: Operador '{node_type}' requer 2 operandos")

            return None
        
        tipo1 = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo2 = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo1
        node['children'][1]['tipo_inferido'] = tipo2
        
        if tipo1 is None or tipo2 is None:
            return None
        
        if tipo1 == 'booleano' or tipo2 == 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador aritmético não aceita operandos booleanos\n"
                         f"Contexto: ({tipo1} {tipo2} {node_type})")
            
            return None
        
        return promoverTipo(tipo1, tipo2)
    
    # ========== DIVISÃO INTEIRA E MÓDULO ==========
    if node_type in ['div_int', 'mod']:
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador '{node_type}' requer 2 operandos")
            
            return None
        
        tipo1 = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo2 = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo1
        node['children'][1]['tipo_inferido'] = tipo2
        
        if tipo1 is None or tipo2 is None:

            return None
        
        if tipo1 != 'int' or tipo2 != 'int':
            op_symbol = '/' if node_type == 'div_int' else '%'
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador '{op_symbol}' requer operandos inteiros, "
                         f"encontrado '{tipo1}' e '{tipo2}'\n"
                         f"Contexto: (... ... {op_symbol})")
            
            return None
        
        divisor_node = node['children'][1]

        if divisor_node['type'] == 'num' and divisor_node['value'] == 0:
            op_symbol = '/' if node_type == 'div_int' else '%'
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                        f"Divisão por zero com operador '{op_symbol}'\n"
                        f"Contexto: (... 0 {op_symbol})")
        
            return None
        
        return 'int'
        
    # ========== DIVISÃO REAL ==========
    if node_type == 'div_real':
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                        f"Operador '|' requer 2 operandos")
            
            return None
        
        tipo1 = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo2 = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo1
        node['children'][1]['tipo_inferido'] = tipo2
        
        if tipo1 is None or tipo2 is None:

            return None
        
        if tipo1 == 'booleano' or tipo2 == 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                        f"Operador aritmético não aceita operandos booleanos\n"
                        f"Contexto: ({tipo1} {tipo2} div_real)")
            
            return None
        
        divisor_node = node['children'][1]

        if divisor_node['type'] == 'num' and divisor_node['value'] == 0:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                        f"Divisão por zero com operador '|'\n"
                        f"Contexto: (... 0 |)")
            return None
    
        return 'real'
        
    # ========== POTENCIAÇÃO ==========
    if node_type == 'pow':
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador '^' requer 2 operandos")
            
            return None
        
        tipo1 = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo2 = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo1
        node['children'][1]['tipo_inferido'] = tipo2

        if tipo1 is None or tipo2 is None:

            return None
        
        if tipo2 != 'int':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Expoente de potenciação deve ser inteiro, encontrado '{tipo2}'\n"
                         f"Contexto: (... ... ^)")
            
            return None
        
        exp_node = node['children'][1]

        if exp_node['type'] == 'num' and exp_node['value'] <= 0:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Expoente de potenciação deve ser positivo (>= 1), encontrado {exp_node['value']}\n"
                         f"Contexto: (... {exp_node['value']} ^)")
            
            return None
        
        return tipo1
    
    # ========== OPERADORES RELACIONAIS ==========
    if node_type in ['lt', 'gt', 'lte', 'gte', 'eq', 'neq']:
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador relacional requer 2 operandos")
            
            return None
        
        tipo1 = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo2 = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)

        node['children'][0]['tipo_inferido'] = tipo1
        node['children'][1]['tipo_inferido'] = tipo2

        if tipo1 is None or tipo2 is None:

            return None
        
        if tipo1 == 'booleano' or tipo2 == 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador relacional não aceita operandos booleanos\n"
                         f"Contexto: ({tipo1} {tipo2} {node_type})")
            
            return None
        
        if tipo1 not in ['int', 'real'] or tipo2 not in ['int', 'real']:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Operador relacional requer operandos numéricos, "
                         f"encontrado '{tipo1}' e '{tipo2}'")
            
            return None
        
        return 'booleano'
    
    # ========== IF (CONDICIONAL) ==========
    if node_type == 'if':
        if len(node['children']) < 3:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"IF requer 3 operandos (condição, then, else)")
            
            return None
        
        tipo_cond = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo_then = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        tipo_else = inferirTipoNode(node['children'][2], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo_cond
        node['children'][1]['tipo_inferido'] = tipo_then
        node['children'][2]['tipo_inferido'] = tipo_else

        if tipo_cond is None or tipo_then is None or tipo_else is None:

            return None
        
        if tipo_cond != 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Condição de IF deve ser booleana, encontrado '{tipo_cond}'\n"
                         f"Contexto: (... ... ... if)")
            
            return None
        
        if tipo_then != tipo_else:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Ramos de IF devem ter mesmo tipo: '{tipo_then}' vs '{tipo_else}'\n"
                         f"Contexto: (... ... ... if)")
            
            return None
        
        return tipo_then
    
    # ========== WHILE (LAÇO) ==========
    if node_type == 'while':
        if len(node['children']) < 2:
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"WHILE requer 2 operandos (condição, corpo)")
            
            return None
        
        tipo_cond = inferirTipoNode(node['children'][0], tabela_simbolos, erros, linha_atual)
        tipo_body = inferirTipoNode(node['children'][1], tabela_simbolos, erros, linha_atual)
        
        node['children'][0]['tipo_inferido'] = tipo_cond
        node['children'][1]['tipo_inferido'] = tipo_body

        if tipo_cond is None or tipo_body is None:

            return None
        
        if tipo_cond != 'booleano':
            erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                         f"Condição de WHILE deve ser booleana, encontrado '{tipo_cond}'\n"
                         f"Contexto: (... ... while)")
            
            return None
        
        return tipo_body
    
    # Tipo desconhecido
    erros.append(f"ERRO SEMÂNTICO [Linha {linha_atual}]: "
                 f"Tipo de nó desconhecido: '{node_type}'")
    
    return None

def analisarSemantica(ast_list, tabela_simbolos):
    # Analisa semanticamente a lista de ASTs.
    erros = []
    arvore_atribuida = []
    
    for linha_num, ast in ast_list:
        tipo = inferirTipoNode(ast, tabela_simbolos, erros, linha_num)
        
        ast['tipo_inferido'] = tipo
        ast['linha'] = linha_num
        
        arvore_atribuida.append((linha_num, ast))
        
        if tipo is not None:
            adicionarSimboloHistorico(tabela_simbolos, tipo, None, linha_num)

        else:
            adicionarSimboloHistorico(tabela_simbolos, None, None, linha_num)
    
    return arvore_atribuida, erros

def gerarProcessoInferencia(node):
    # Helper recursivo (pós-ordem) para construir a lista de inferência bottom-up.
    inferences = []
    
    # Visita filhos primeiro
    for child in node.get('children', []):
        inferences.extend(gerarProcessoInferencia(child))
        
    # Processa o nó atual
    tipo_resultado = node.get('tipo_inferido', 'ERRO')
    descricao_no = f"Nó '{node['type']}'"

    if node['value'] is not None:
        descricao_no += f" (Valor: {node['value']})"
    
    tipos_filhos = [str(c.get('tipo_inferido', '?')) for c in node.get('children', [])]
    
    justificativa = ""
    
    if node['type'] == 'num':
        justificativa = f"Regra 2.1 (Literal) -> {tipo_resultado}"

    elif node['type'] == 'id':
        justificativa = f"Regra 2.2 (Identificador) -> {tipo_resultado}"

    elif node['type'] in ['plus', 'minus', 'mult', 'div_real']:
        justificativa = f"Regra 2.3 (Aritmética) com ({', '.join(tipos_filhos)}) -> {tipo_resultado}"

    elif node['type'] in ['div_int', 'mod']:
        justificativa = f"Regra 2.4 (Div/Mod) com ({', '.join(tipos_filhos)}) -> {tipo_resultado}"

    elif node['type'] == 'pow':
        justificativa = f"Regra 2.5 (Potência) com ({', '.join(tipos_filhos)}) -> {tipo_resultado}"

    elif node['type'] in ['lt', 'gt', 'lte', 'gte', 'eq', 'neq']:
        justificativa = f"Regra 2.6 (Relacional) com ({', '.join(tipos_filhos)}) -> {tipo_resultado}"

    elif node['type'] == 'store':
        val_node = node['children'][0]
        id_node = node['children'][1]
        justificativa = f"Regra 2.7 (Armazenamento) de '{val_node.get('tipo_inferido', '?')}' em '{id_node.get('value', '?')}' -> {tipo_resultado}"

    elif node['type'] == 'res':
        n_node = node['children'][0]
        justificativa = f"Regra 2.8 (Histórico) com N='{n_node.get('tipo_inferido', '?')}' -> {tipo_resultado}"
    
    elif node['type'] == 'if':
        justificativa = f"Regra 2.9 (Condicional) com (cond:{tipos_filhos[0]}, then:{tipos_filhos[1]}, else:{tipos_filhos[2]}) -> {tipo_resultado}"
    
    elif node['type'] == 'while':
        justificativa = f"Regra 2.10 (Laço) com (cond:{tipos_filhos[0]}, body:{tipos_filhos[1]}) -> {tipo_resultado}"
    
    inferences.append(f"{descricao_no}: {justificativa}")
    
    return inferences

def descreverRegraFormal(node):
    # Retorna uma string formatada da regra formal aplicada a este nó.

    tipo_res = node.get('tipo_inferido', 'ERRO')
    children = node.get('children', [])
    
    if node['type'] == 'num':
        regra = f"**Regra 2.1: Literal**\n"
        regra += f"```\nΓ ⊢ {node['value']} : {tipo_res}\n```\n"

        return regra
        
    if node['type'] == 'id':
        regra = f"**Regra 2.2: Identificador**\n"
        regra += f"```\nΓ({node['value']}).tipo = {tipo_res}, Γ({node['value']}).inicializada = true\n"
        regra += f"──────────────────────────────────────────────\n"
        regra += f"Γ ⊢ {node['value']} : {tipo_res}\n```\n"
        return regra
    

    if node['type'] == 'store':
        t_val = children[0]['tipo_inferido']
        id_name = children[1]['value']
        regra = f"**Regra 2.7: Armazenamento**\n"
        regra += f"```\nΓ ⊢ e₁ : {t_val}    T ∈ {{int, real}}\n"
        regra += f"──────────────────────────────────────────────────\n"
        regra += f"Γ[{id_name} ↦ {{tipo: {t_val}}}] ⊢ (e₁ {id_name}) : {tipo_res}\n```\n"

        return regra
        
    if node['type'] == 'res':
        t_n = children[0]['tipo_inferido']
        n_val = children[0].get('value', 'N')
        regra = f"**Regra 2.8: Histórico**\n"
        regra += f"```\nΓ ⊢ e₁ : {t_n}    e₁.valor ≥ 1    historico[...].tipo = T\n"
        regra += f"────────────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ RES) : {tipo_res}\n```\n"
        regra += f"Contexto: N = {n_val}\n"

        return regra

    if node['type'] in ['plus', 'minus', 'mult', 'div_real']:
        t1 = children[0]['tipo_inferido']
        t2 = children[1]['tipo_inferido']
        op_map = {'plus': '+', 'minus': '-', 'mult': '*', 'div_real': '|'}
        op = op_map.get(node['type'], '?')
        regra = f"**Regra 2.3: Operação Aritmética (com promoção)**\n"
        regra += f"```\nΓ ⊢ e₁ : {t1}    Γ ⊢ e₂ : {t2}\n"
        regra += f"────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ {op}) : promover_tipo({t1}, {t2}) = {tipo_res}\n```\n"

        return regra
        
    if node['type'] in ['div_int', 'mod']:
        t1 = children[0]['tipo_inferido']
        t2 = children[1]['tipo_inferido']
        op = '/' if node['type'] == 'div_int' else '%'
        regra = f"**Regra 2.4: Divisão/Módulo Inteiro**\n"
        regra += f"```\nΓ ⊢ e₁ : {t1}    Γ ⊢ e₂ : {t2}\n"
        regra += f"────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ {op}) : {tipo_res}\n```\n"
        regra += f"**Restrição:** {t1} == int, {t2} == int\n"

        return regra

    if node['type'] == 'pow':
        t_base = children[0]['tipo_inferido']
        t_exp = children[1]['tipo_inferido']
        regra = f"**Regra 2.5: Potenciação**\n"
        regra += f"```\nΓ ⊢ e₁ : {t_base}    Γ ⊢ e₂ : {t_exp}\n"
        regra += f"────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ ^) : {tipo_res}\n```\n"
        regra += f"**Restrição:** {t_exp} == int, e₂.valor > 0\n"

        return regra
        
    if node['type'] in ['lt', 'gt', 'lte', 'gte', 'eq', 'neq']:
        t1 = children[0]['tipo_inferido']
        t2 = children[1]['tipo_inferido']
        op_map = {
            'lt': '<', 'gt': '>', 'lte': '<=', 'gte': '>=',
            'eq': '==', 'neq': '!='
        }
        op = op_map.get(node['type'], '?')
        regra = f"**Regra 2.6: Operador Relacional**\n"
        regra += f"```\nΓ ⊢ e₁ : {t1}    Γ ⊢ e₂ : {t2}\n"
        regra += f"────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ {op}) : {tipo_res}\n```\n"
        regra += f"**Restrição:** {t1}, {t2} ∈ {{int, real}}\n"

        return regra

    if node['type'] == 'if':
        t_cond = children[0]['tipo_inferido']
        t_then = children[1]['tipo_inferido']
        t_else = children[2]['tipo_inferido']
        regra = f"**Regra 2.9: Condicional**\n"
        regra += f"```\nΓ ⊢ e₁ : {t_cond}    Γ ⊢ e₂ : {t_then}    Γ ⊢ e₃ : {t_else}\n"
        regra += f"─────────────────────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ e₃ if) : {tipo_res}\n```\n"
        regra += f"**Restrições:** {t_cond} == booleano, {t_then} == {t_else}\n"

        return regra
        
    if node['type'] == 'while':
        t_cond = children[0]['tipo_inferido']
        t_body = children[1]['tipo_inferido']
        regra = f"**Regra 2.10: Laço de Repetição**\n"
        regra += f"```\nΓ ⊢ e₁ : {t_cond}    Γ ⊢ e₂ : {t_body}\n"
        regra += f"─────────────────────────────────────\n"
        regra += f"Γ ⊢ (e₁ e₂ while) : {tipo_res}\n```\n"
        regra += f"**Restrição:** {t_cond} == booleano\n"

        return regra

    return f"**Regra não documentada para:** {node['type']}\n"

def gerarRelatorioTipos(arvore_atribuida, filename='julgamento_tipos.md'):
    # Gera relatório markdown detalhado do julgamento de tipos.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Julgamento de Tipos\n\n")
        f.write("Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.\n\n")
        
        for linha_num, ast in arvore_atribuida:
            f.write(f"---\n\n## Linha {linha_num}\n\n")
            f.write(f"**Tipo Inferido Final:** `{ast.get('tipo_inferido', 'ERRO')}`\n\n")
            
            # Processo de Inferência
            f.write("### Processo de Inferência (Bottom-Up)\n\n")
            try:
                inferencias = gerarProcessoInferencia(ast)
                for i, inf in enumerate(inferencias, 1):
                    f.write(f"{i}. {inf}\n")
            except Exception as e:
                f.write(f"Erro ao gerar processo de inferência: {e}\n")
            
            # Regra Formal Aplicada (do Nó Raiz)
            f.write("\n### Regra de Dedução Formal (Nó Raiz)\n\n")
            try:
                f.write(descreverRegraFormal(ast))

            except Exception as e:
                f.write(f"Erro ao gerar regra formal: {e}\n")
            
            f.write("\n")


def gerarRelatorioErros(erros, filename='erros_semanticos.md'):
    # Gera relatório markdown com erros semânticos.
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Erros Semânticos\n\n")
        
        if not erros:
            f.write(" **Nenhum erro semântico encontrado!**\n")

        else:
            f.write(f" **{len(erros)} erro(s) encontrado(s):**\n\n")
            for i, erro in enumerate(sorted(list(set(erros))), 1):
                f.write(f"{i}. {erro}\n\n")


def gerarArvoreAtribuida(arvore_anotada):
    # Constrói a árvore sintática abstrata atribuída final.
    arvore_final = []
    
    for linha_num, ast in arvore_anotada:
        arvore_final.append({
            'linha': linha_num,
            'tipo_vertice': ast['type'],
            'tipo_inferido': ast.get('tipo_inferido'),
            'valor': ast.get('value'),
            'filhos': [extrairInfoFilho(c) for c in ast.get('children', [])]
        })
    
    return arvore_final


def extrairInfoFilho(node):
    # Extrai informações de um nó filho.
    if node is None:

        return None
    
    return {
        'tipo_vertice': node['type'],
        'tipo_inferido': node.get('tipo_inferido'),
        'valor': node.get('value'),
        'filhos': [extrairInfoFilho(c) for c in node.get('children', [])]
    }


def salvarArvoreAtribuida(arvore_atribuida, filename='arvore_atribuida.json'):
    # Salva árvore sintática abstrata atribuída em JSON.
    arvore_atribuida_json = gerarArvoreAtribuida(arvore_atribuida)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(arvore_atribuida_json, f, indent=2, ensure_ascii=False)