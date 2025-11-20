# FELIPE EDUARDO MARCONDES
# GRUPO 2

def lerTokens(filename):
    # Lê um arquivo e retorna uma lista de tokens (representados como dicionários).
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return tokenizar(f.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{filename}' não encontrado.")


def tokenizar(text):
    # Converte o texto de entrada em uma lista de tokens.

    KEYWORDS = {
        'RES': 'res',    # RES deve ser maiúsculo
    }
    
    KEYWORDS_CASE_INSENSITIVE = {
        'if': 'if',
        'while': 'while'
    }

    DOUBLE_OPS = {
        '==': 'eq', '!=': 'neq', '<=': 'lte', '>=': 'gte'
    }

    SINGLE_OPS = {
        '(': 'lparen', ')': 'rparen', '+': 'plus', '-': 'minus', '*': 'mult',
        '|': 'div_real', '/': 'div_int', '%': 'mod', '^': 'pow', '<': 'lt', '>': 'gt'
    }

    tokens = []
    lines = text.split('\n')

    for line_num, line in enumerate(lines, 1):
        line_content = line.split('#', 1)[0]
        i = 0

        while i < len(line_content):
            col = i + 1
            char = line_content[i]

            if char.isspace():
                i += 1
                continue

            # Operadores de dois caracteres
            if i + 1 < len(line_content) and line_content[i:i+2] in DOUBLE_OPS:
                op = line_content[i:i+2]
                tokens.append({'type': DOUBLE_OPS[op], 'value': op, 'line': line_num, 'col': col})
                i += 2
                continue

            # Números
            if char.isdigit() or (char == '-' and i + 1 < len(line_content) and line_content[i+1].isdigit()):
                start = i
                if char == '-':
                    i += 1

                while i < len(line_content) and (line_content[i].isdigit() or line_content[i] == '.'):
                    i += 1

                num_str = line_content[start:i]
                value = float(num_str) if '.' in num_str else int(num_str)
                tokens.append({'type': 'num', 'value': value, 'line': line_num, 'col': col})
                continue

            # Identificadores e keywords
            if char.isalpha():
                start = i
                i += 1

                while i < len(line_content) and (line_content[i].isalnum() or line_content[i] == '_'):
                    i += 1

                id_str = line_content[start:i]
                
                # Verifica se é keyword case-sensitive (RES)
                if id_str in KEYWORDS:
                    token_type = KEYWORDS[id_str]
                    tokens.append({'type': token_type, 'value': id_str, 'line': line_num, 'col': col})
                # Verifica se é keyword case-insensitive (if, while)
                elif id_str.lower() in KEYWORDS_CASE_INSENSITIVE:
                    token_type = KEYWORDS_CASE_INSENSITIVE[id_str.lower()]
                    tokens.append({'type': token_type, 'value': id_str.lower(), 'line': line_num, 'col': col})
                else:
                    # Identificadores devem estar em MAIÚSCULAS
                    if id_str != id_str.upper():
                        raise SyntaxError(f"Identificador '{id_str}' deve estar em MAIÚSCULAS na linha {line_num}, coluna {col}")
                    tokens.append({'type': 'id', 'value': id_str, 'line': line_num, 'col': col})
                
                continue

            # Operadores de um caractere
            if char in SINGLE_OPS:
                tokens.append({'type': SINGLE_OPS[char], 'value': char, 'line': line_num, 'col': col})
                i += 1
                continue

            raise SyntaxError(f"Token inválido '{char}' na linha {line_num}, coluna {col}")

    tokens.append({'type': 'eof', 'value': None, 'line': len(lines) + 1, 'col': 1})
    
    return tokens