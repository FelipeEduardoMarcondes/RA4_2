# Gramática LL(1) para Linguagem RPN

**Autor:** FELIPE EDUARDO MARCONDES  
**Grupo:** 2  
**Universidade:** Pontifícia Universidade Católica do Paraná (PUCPR)  
**Disciplina:** Linguagens Formais e Compiladores 
**Professor:** Frank Coelho de Alcantara 
**Ano:** 2025

---

## 1. Visão Geral

Este projeto implementa um compilador completo para uma linguagem de programação simplificada em **Notação Polonesa Reversa (RPN)**. O compilador realiza análise léxica, sintática e semântica, gerando relatórios detalhados sobre tipos, erros e a árvore sintática abstrata atribuída.

**Características principais:**
- Expressões em notação pós-fixada: `(A B op)`
- Operações aritméticas e relacionais
- Estruturas de controle (`IF`, `WHILE`)
- Comandos de memória (identificadores em maiúsculas, `RES`)
- Aninhamento ilimitado de expressões
- Verificação de tipos e análise semântica completa
- Geração automática de relatórios em Markdown e JSON

---

## Requisitos

### Sistema Operacional
- Windows, Linux ou macOS

### Software Necessário
- **Python 3.8 ou superior**

Para verificar se o Python está instalado:
```bash
python --version
# ou
python3 --version
```

### Instalação do Python

**Windows:**
1. Baixe o instalador em [python.org](https://www.python.org/downloads/)
2. Execute o instalador e marque "Add Python to PATH"

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**macOS:**
```bash
# Usando Homebrew
brew install python3
```

O projeto deve conter os seguintes arquivos:
```
.
├── compilar.py          # Programa principal
├── leitor.py            # Analisador léxico
├── parser.py            # Analisador sintático
├── semantico.py         # Analisador semântico
├── readme.md            # Este arquivo
├── atributos.md         # Gramática de atributos
├── teste1.txt           # Arquivo de teste 1
├── teste2.txt           # Arquivo de teste 2
├── teste3.txt           # Arquivo de teste 3
└── analises/            # Diretório de saída
```

---

## Execução

### Sintaxe Básica

```bash
python compilar.py <arquivo_de_teste.txt>
```

### Exemplos

**Executar teste 1:**
```bash
python compilar.py teste1.txt
```

**Executar teste 2:**
```bash
python compilar.py teste2.txt
```

**Executar teste 3:**
```bash
python compilar.py teste3.txt
```

### Saída Esperada

O programa exibirá:
1. **Console:** Resumo da compilação e árvores sintáticas
2. **Arquivos gerados** no diretório `analises/`:
   - `gramatica_atributos_gerada.md` - Gramática de atributos
   - `<arquivo>_julgamento_tipos.md` - Relatório de tipos
   - `<arquivo>_erros_semanticos.md` - Relatório de erros
   - `<arquivo>_arvore_atribuida.json` - AST em JSON
   - `<arquivo>_arvore_sintatica.md` - AST em Markdown

**Exemplo de saída no console:**
```
============================================================
COMPILANDO: teste1.txt
============================================================

[FASE 1] Análise Léxica...
15 token(s) identificado(s)

[FASE 2] Análise Sintática...
5 expressão(ões) válida(s)

[FASE 3] Análise Semântica...
Nenhum erro semântico detectado

[FASE 3.1] Gerando árvore atribuída...
Árvore sintática abstrata atribuída gerada

[SAÍDA] Gerando relatórios...
analises/gramatica_atributos_gerada.md (estático)
analises/teste1_julgamento_tipos.md
analises/teste1_erros_semanticos.md
analises/teste1_arvore_atribuida.json
analises/teste1_arvore_sintatica.md

============================================================
RESUMO DA COMPILAÇÃO
============================================================
Tokens processados:      15
Expressões analisadas:   5
Variáveis declaradas:    3
Histórico de resultados: 5
Erros semânticos:        0

Status: COMPILAÇÃO BEM-SUCEDIDA
============================================================
```

---

### Erros Comuns e Soluções

**Erro: "Arquivo não encontrado"**
```bash
# Solução: Verifique se o arquivo existe no diretório atual
ls -la teste1.txt
# ou no Windows:
dir teste1.txt
```

**Erro: "Identificador 'x' deve estar em MAIÚSCULAS"**
```
# Problema: Identificadores devem ser maiúsculos
(42 x)  Errado
(42 X)  Correto
```

**Erro: "Memória 'X' utilizada sem inicialização"**
```
# Problema: Tentou usar variável antes de inicializar
(X)     Errado - X não foi inicializado
(42 X)  Correto - Inicializa X primeiro
(X)     Agora pode usar X
```

**Erro: "ERRO SEMÂNTICO: Divisão por zero"**
```
(10 0 /)  Errado - Divisão por zero
(10 2 /)  Correto
```

### Executar Testes Unitários

Para testar componentes individuais:

**Teste do analisador léxico:**
```python
python -c "from leitor import lerTokens; print(lerTokens('teste1.txt'))"
```

**Teste do analisador sintático:**
```python
python -c "from leitor import lerTokens; from parser import parsear, construirGramatica, calcularFirst, calcularFollow, construirTabelaLL1; tokens = lerTokens('teste1.txt'); g = construirGramatica(); f = calcularFirst(g); fo = calcularFollow(g, f); t = construirTabelaLL1(g, f, fo); print(parsear(tokens, t))"
```

---

## Arquivos do Projeto

### Arquivos Fonte

| Arquivo | Descrição | Responsabilidade |
|---------|-----------|------------------|
| `compilar.py` | Programa principal | Orquestra todas as fases e gera relatórios |
| `leitor.py` | Analisador léxico | Tokenização do código fonte |
| `parser.py` | Analisador sintático | Parsing LL(1) e geração da AST |
| `semantico.py` | Analisador semântico | Verificação de tipos e análise semântica |

### Arquivos de Documentação

| Arquivo | Descrição |
|---------|-----------|
| `readme.md` | Este arquivo - Instruções completas |
| `atributos.md` | Gramática de atributos da linguagem |

---

## 2. Símbolos Terminais

### 2.1 Delimitadores
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `lparen` | `(` | Abre parênteses |
| `rparen` | `)` | Fecha parênteses |

### 2.2 Operadores Aritméticos
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `plus`    | `+` | Adição |
| `minus`   | `-` | Subtração |
| `mult`    | `*` | Multiplicação |
| `div_real`| `\|`| Divisão real (ponto flutuante) |
| `div_int` | `/` | Divisão inteira |
| `mod`     | `%` | Módulo (resto da divisão) |
| `pow`     | `^` | Potenciação |

### 2.3 Operadores Relacionais
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `eq`  | `==` | Igualdade |
| `neq` | `!=` | Diferença |
| `lt`  | `<` | Menor que |
| `gt`  | `>` | Maior que |
| `lte` | `<=` | Menor ou igual |
| `gte` | `>=` | Maior ou igual |

### 2.4 Operandos e Keywords
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `num`   | N/A | Literal numérico (int ou real) |
| `id`    | N/A | Identificador em MAIÚSCULAS (ex: `X`, `MEM`, `CONTADOR`) |
| `res`   | `RES` | Keyword para histórico (sempre maiúsculo) |
| `if`    | `if` | Keyword condicional |
| `while` | `while` | Keyword laço |
| `eof`   | N/A | Fim de arquivo |

**Nota Importante:** 
- `id` = qualquer sequência de letras MAIÚSCULAS (ex: `X`, `VAR`, `CONTADOR`, `MEM`)
- `res` = keyword específica `RES` (sempre maiúsculo, reservado)
- `if` e `while` = keywords

---

## 3. Produções da Gramática LL(1)

```ebnf
PROGRAM -> LINE PROGRAM 
        | ε

LINE -> lparen STMT rparen

STMT -> EXPR STMT_TAIL

STMT_TAIL -> EXPR STMT_TAIL2           
          | OP_BIN                    
          | ε                         

STMT_TAIL2 -> OP_BIN                   
           | CONTROL                  
           | EXPR CONTROL             
           | ε                        
           
CONTROL -> if                          
        | while                       

EXPR -> num
     | id
     | res
     | lparen STMT rparen

OP_BIN -> plus | minus | mult | div_real | div_int | mod | pow
       | eq | neq | lt | gt | lte | gte
```

---

## 4. Semântica da Linguagem

### 4.1 Operações Binárias
Formato: `(A B op)`
- `A` e `B` são operandos (números, identificadores ou sub-expressões)
- `op` é um operador binário

**Exemplos:**
```
(3 5 +)           -> 3 + 5 = 8
(10 3 /)          -> 10 / 3 = 3 (divisão inteira)
(10.0 3.0 |)      -> 10.0 / 3.0 = 3.333... (divisão real)
(X Y *)           -> X * Y (valores de memória)
```

### 4.2 Comandos de Memória

#### Armazenamento: `(valor ID)`
Armazena um valor em um identificador (memória).

**Exemplos:**
```
(42 X)            -> Armazena 42 em X
(3.14 PI)         -> Armazena 3.14 em PI
((A B +) SOMA)    -> Armazena resultado de A+B em SOMA
```

#### Recuperação: `(ID)`
Retorna o valor armazenado em um identificador.

**Exemplos:**
```
(X)               -> Retorna valor de X
(CONTADOR)        -> Retorna valor de CONTADOR
```

**Erro semântico:** Usar `(ID)` antes de inicializar com `(valor ID)`.

#### Histórico: `(N RES)`
Retorna o resultado da expressão N linhas anteriores.

**Exemplos:**
```
Linha 1: (3 5 +)         -> resultado = 8
Linha 2: (1 RES)         -> retorna 8 (linha anterior)
Linha 3: (2 RES)         -> retorna 8 (duas linhas antes)
```

**Validações semânticas:**
- N deve ser inteiro não-negativo
- N não pode referenciar linha além do início do arquivo
- Linha referenciada deve ser uma expressão válida

### 4.3 Estruturas de Controle

#### Condicional: `(condição then else if)`
Executa `then` se `condição` é verdadeira, senão executa `else`.

**Formato RPN:**
```
(cond then else if)
```

**Exemplo:**
```
((X 0 >) (X) (0 X -) if)
-> Se X > 0 retorna X, senão retorna -X (valor absoluto)
```

#### Laço: `(condição corpo while)`
Executa `corpo` enquanto `condição` for verdadeira.

**Formato RPN:**
```
(cond body while)
```

**Exemplo:**
```
((I 10 <) ((I 1 +) I) while)
-> Incrementa I enquanto I < 10
```

### 4.4 Expressões Aninhadas

Qualquer `EXPR` pode conter sub-expressões entre parênteses.

**Exemplos:**
```
(A (C D *) +)              -> A + (C * D)
((A B %) (D E *) /)        -> (A % B) / (D * E)
((A B +) (C D *) |)        -> (A + B) | (C * D)
(((X 1 +) X) ((Y 2 *) Y) +) -> Múltiplos níveis de aninhamento
```

---

## 5. Conjuntos FIRST

| Não-Terminal | FIRST |
|--------------|-------|
| **PROGRAM** | { `lparen`, **ε** } |
| **LINE** | { `lparen` } |
| **STMT** | { `num`, `id`, `res`, `lparen` } |
| **STMT_TAIL** | { `num`, `id`, `res`, `lparen`, `plus`, `minus`, `mult`, `div_real`, `div_int`, `mod`, `pow`, `eq`, `neq`, `lt`, `gt`, `lte`, `gte`, **ε** } |
| **STMT_TAIL2** | { `plus`, `minus`, `mult`, `div_real`, `div_int`, `mod`, `pow`, `eq`, `neq`, `lt`, `gt`, `lte`, `gte`, `if`, `while`, `num`, `id`, `res`, `lparen`, **ε** } |
| **CONTROL** | { `if`, `while` } |
| **EXPR** | { `num`, `id`, `res`, `lparen` } |
| **OP_BIN** | { `plus`, `minus`, `mult`, `div_real`, `div_int`, `mod`, `pow`, `eq`, `neq`, `lt`, `gt`, `lte`, `gte` } |

---

## 6. Conjuntos FOLLOW

| Não-Terminal | FOLLOW |
|--------------|--------|
| **PROGRAM** | { `eof` } |
| **LINE** | { `lparen`, `eof` } |
| **STMT** | { `rparen` } |
| **STMT_TAIL** | { `rparen` } |
| **STMT_TAIL2** | { `rparen` } |
| **CONTROL** | { `rparen` } |
| **EXPR** | { `plus`, `minus`, `mult`, `div_real`, `div_int`, `mod`, `pow`, `eq`, `neq`, `lt`, `gt`, `lte`, `gte`, `if`, `while`, `num`, `id`, `res`, `lparen`, `rparen` } |
| **OP_BIN** | { `rparen` } |


---

## 7. Tabela de Análise LL(1)

| Não-Terminal | lparen | rparen | num | id | res | ops* | while | if | eof |
|--------------|--------|--------|-----|----|----|------|-------|----|----|
| **PROGRAM** | LINE PROGRAM | - | - | - | - | - | - | - | ε |
| **LINE** | lparen STMT rparen | - | - | - | - | - | - | - | - |
| **STMT** | EXPR STMT_TAIL | - | EXPR STMT_TAIL | EXPR STMT_TAIL | EXPR STMT_TAIL | - | - | - | - |
| **STMT_TAIL** | EXPR STMT_TAIL2 | ε | EXPR STMT_TAIL2 | EXPR STMT_TAIL2 | EXPR STMT_TAIL2 | OP_BIN | - | - | - |
| **STMT_TAIL2** | EXPR CONTROL | ε | EXPR CONTROL | EXPR CONTROL | EXPR CONTROL | OP_BIN | CONTROL | CONTROL | - |
| **CONTROL** | - | - | - | - | - | - | while | if | - |
| **EXPR** | lparen STMT rparen | - | num | id | res | - | - | - | - |
| **OP_BIN** | - | - | - | - | - | específico | - | - | - |

**Legenda:**  
`ops*` = qualquer operador (`+`, `-`, `*`, `|`, `/`, `%`, `^`, `==`, `!=`, `<`, `>`, `<=`, `>=`)

---

## 8. Tipos de Dados e Precisão

### 8.1 Tipos Suportados

| Tipo | Descrição |
|------|-----------|
| `int` | Números inteiros |
| `real` (ou `float`) | Números de ponto flutuante |
| `booleano` | Resultado de operadores relacionais |

**Nota:** O tipo booleano **não pode ser armazenado** em memórias (identificadores), sendo usado apenas como resultado de expressões relacionais em estruturas de controle.

### 8.2 Precisão Numérica (Arquitetura 8 bits - Arduino Uno)

Para processadores de **8 bits** (Arduino Uno R3, Arduino Mega):
- **Números de ponto flutuante:** Meia precisão (16 bits, IEEE 754)

### 8.3 Regras de Tipo

1. **Operações aritméticas com tipos mistos:** Promovem para `real`
   - `int + real -> real`
   - `int * real -> real`

2. **Divisão:**
   - `/` (divisão inteira): Requer ambos operandos `int`, retorna `int`
   - `|` (divisão real): Aceita `int` ou `real`, retorna `real`

3. **Módulo (%)**: Requer ambos operandos `int`, retorna `int`

4. **Potenciação (^)**: 
   - Base: `int` ou `real`
   - Expoente: **deve ser `int` positivo**
   - Retorno: mesmo tipo da base

5. **Operadores relacionais:** Aceitam `int` ou `real`, retornam `booleano`

---

## 9. Validações Semânticas

A gramática sintática aceita algumas estruturas que são validadas apenas na análise semântica:

### 9.1 Validações de Tipo
- Expoente de `^` deve ser inteiro positivo
- Operandos de `/` e `%` devem ser inteiros
- Condições em `if` e `while` devem resultar em booleano
- Operações mistas `int`/`real` promovem para `real`

### 9.2 Validações de Memória
- Identificadores devem ser inicializados antes do uso em `(ID)`
- `(valor ID)` define/atualiza a memória `ID`
- Escopo: cada arquivo é independente

### 9.3 Validações de Comandos Especiais
- `(N RES)`: N deve ser inteiro não-negativo e linha válida
- `RES` não pode ser usado como identificador de memória
- Linha referenciada por `RES` deve existir

### 9.4 Validações de Estruturas de Controle
- `if` requer exatamente 3 operandos: condição, then, else
- `while` requer exatamente 2 operandos: condição, corpo
- Condições devem ser expressões booleanas válidas

---

## 10. Divisão de Responsabilidades

### 10.1 Analisador Sintático
**Responsabilidade:** Validar estrutura gramatical

**Exemplos aceitos:**
```
(42 X)          ->  Sintaxe OK (armazenamento)
(5 RES)         ->  Sintaxe OK (histórico)
(X Y +)         ->  Sintaxe OK (operação)
((X 0 >) (X) (0) if)  ->  Sintaxe OK (condicional)
((I 10 <) ((I 1 +) I) while) ->  Sintaxe OK (laço)
```

### 10.2 Analisador Semântico
**Responsabilidade:** Validar contextos, tipos e inicialização

```
Valida: Todos os itens da seção 11  
Gera: AST atribuída com tipos  
Reporta: Erros semânticos com linha e descrição
```