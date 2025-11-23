# Gramática de Atributos

**Autor:** FELIPE EDUARDO MARCONDES  
**Grupo:** 2  
**Universidade:** Pontifícia Universidade Católica do Paraná (PUCPR)  
**Disciplina:** Linguagens Formais e Compiladores 
**Professor:** Frank Coelho de Alcantara 
**Ano:** 2025

## 1. Atributos

### Para cada símbolo da gramática, definimos:

- **tipo**: {int, real, booleano}
- **valor**: valor calculado (quando aplicável)
- **inicializada**: boolean (para identificadores)
- **linha**: número da linha no código fonte

## 2. Regras de Produção com Atributos

### 2.1. Literais

**Regra:** EXPR -> num

**Notação Formal (Infixa):**
```
Γ ⊢ num : int    (se num é inteiro)
Γ ⊢ num : real   (se num tem ponto decimal)
```

**Adaptação RPN:**
```
Sintaxe: (5)      -> tipo: int
Sintaxe: (5.0)    -> tipo: real
```

**Atributos Sintetizados:**
- `EXPR.tipo = int` se `num.valor` é inteiro
- `EXPR.tipo = real` se `num.valor` tem ponto decimal
- `EXPR.valor = num.valor`
- `EXPR.linha = num.linha`

---

### 2.2. Identificadores

**Regra:** EXPR -> id

**Notação Formal (Infixa):**
```
Γ(x) = T    Γ(x).inicializada = true
─────────────────────────────────────
Γ ⊢ x : T
```

**Adaptação RPN:**
```
Sintaxe: (X)    -> recupera valor de X com tipo Γ(X)
```

**Atributos Sintetizados:**
- `EXPR.tipo = TabelaSimbolos[id.nome].tipo`
- `EXPR.valor = TabelaSimbolos[id.nome].valor`
- `EXPR.linha = id.linha`

**Restrição Semântica:**
- ERRO se `id.nome ∉ TabelaSimbolos`
- ERRO se `TabelaSimbolos[id.nome].inicializada = false`

**Exemplo RPN:**
```
(X)               -> recupera valor de X
Erro se X não foi inicializado com (valor X)
```

---

### 2.3. Operações Aritméticas Binárias

**Regra:** STMT -> EXPR₁ EXPR₂ OP_BIN  
*(corresponde a `(A B op)` em RPN)*

**Para op ∈ {+, -, *, |}:**

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : T₁    Γ ⊢ e₂ : T₂
─────────────────────────────────────────
Γ ⊢ e₁ op e₂ : promover_tipo(T₁, T₂)
```

**Adaptação RPN:**
```
Sintaxe: (A B op)
Onde:
  - A e B são expressões com tipos T₁ e T₂
  - op ∈ {+, -, *, |}
  - Resultado tem tipo promover_tipo(T₁, T₂)
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : T₁    Γ ⊢ EXPR₂ : T₂    T₁, T₂ ∈ {int, real}
────────────────────────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ op) : promover_tipo(T₁, T₂)
```

**Função promover_tipo:**
- `promover_tipo(int, int) = int`
- `promover_tipo(int, real) = real`
- `promover_tipo(real, int) = real`
- `promover_tipo(real, real) = real`

**Atributos Sintetizados:**
- `STMT.tipo = promover_tipo(EXPR₁.tipo, EXPR₂.tipo)`
- `STMT.valor = calcular(EXPR₁.valor, EXPR₂.valor, op)`
- `STMT.linha = OP_BIN.linha`

**Exemplos RPN:**
```
(3 5 +)           -> tipo: int, valor: 8
(3.0 5 +)         -> tipo: real, valor: 8.0
(X Y *)           -> tipo: promover_tipo(tipo(X), tipo(Y))
```

---

### 2.4. Divisão Inteira e Módulo

**Regra:** STMT -> EXPR₁ EXPR₂ OP_BIN  
*(para op ∈ {/, %})*

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int    e₂.valor ≠ 0
───────────────────────────────────────────
Γ ⊢ e₁ op e₂ : int
```

**Adaptação RPN:**
```
Sintaxe: (A B /)    -> divisão inteira
Sintaxe: (A B %)    -> módulo
Onde:
  - A e B devem ser ambos do tipo int
  - B ≠ 0
  - Resultado tem tipo int
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : int    Γ ⊢ EXPR₂ : int    EXPR₂.valor ≠ 0
─────────────────────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ op) : int
```

**Restrição Semântica:**
- ERRO se `EXPR₁.tipo ≠ int`
- ERRO se `EXPR₂.tipo ≠ int`
- ERRO se `EXPR₂.valor = 0` (divisão por zero)

**Atributos Sintetizados:**
- `STMT.tipo = int`
- `STMT.valor = EXPR₁.valor op EXPR₂.valor`

**Exemplos RPN:**
```
(10 3 /)          -> tipo: int, valor: 3
(10 3 %)          -> tipo: int, valor: 1
(10.0 3 /)        -> ERRO: divisão inteira requer operandos int
(10 0 /)          -> ERRO: divisão por zero
```

---

### 2.5. Potenciação

**Regra:** STMT -> EXPR₁ EXPR₂ pow

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : T    Γ ⊢ e₂ : int    e₂.valor > 0
────────────────────────────────────────
Γ ⊢ e₁ ^ e₂ : T
```

**Adaptação RPN:**
```
Sintaxe: (base exp ^)
Onde:
  - base pode ser int ou real
  - exp deve ser int e exp > 0
  - Resultado tem o mesmo tipo da base
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : T    Γ ⊢ EXPR₂ : int    EXPR₂.valor > 0    T ∈ {int, real}
────────────────────────────────────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ ^) : T
```

**Restrição Semântica:**
- ERRO se `EXPR₂.tipo ≠ int`
- ERRO se `EXPR₂.valor ≤ 0` (expoente deve ser positivo)

**Atributos Sintetizados:**
- `STMT.tipo = EXPR₁.tipo`
- `STMT.valor = EXPR₁.valor ^ EXPR₂.valor`

**Exemplos RPN:**
```
(2 8 ^)           -> tipo: int, valor: 256
(2.0 3 ^)         -> tipo: real, valor: 8.0
(2 -1 ^)          -> ERRO: expoente deve ser positivo
(2 3.5 ^)         -> ERRO: expoente deve ser inteiro
(2 0 ^)           -> ERRO: expoente deve ser positivo (>= 1)
```

---

### 2.6. Operadores Relacionais

**Regra:** STMT -> EXPR₁ EXPR₂ OP_REL  
*(para op ∈ {<, >, <=, >=, ==, !=})*

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : T₁    Γ ⊢ e₂ : T₂    T₁, T₂ ∈ {int, real}
──────────────────────────────────────────────────
Γ ⊢ e₁ op e₂ : booleano
```

**Adaptação RPN:**
```
Sintaxe: (A B op)
Onde:
  - A e B são expressões numéricas (int ou real)
  - op ∈ {<, >, <=, >=, ==, !=}
  - Resultado tem tipo booleano
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : T₁    Γ ⊢ EXPR₂ : T₂    T₁, T₂ ∈ {int, real}
─────────────────────────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ op) : booleano
```

**Atributos Sintetizados:**
- `STMT.tipo = booleano`
- `STMT.valor = EXPR₁.valor op EXPR₂.valor`

**Restrição Semântica:**
- ERRO se `EXPR₁.tipo ∉ {int, real}`
- ERRO se `EXPR₂.tipo ∉ {int, real}`

**Exemplos RPN:**
```
(X Y <)           -> tipo: booleano
(5 10 >=)         -> tipo: booleano, valor: false
(3.14 PI ==)      -> tipo: booleano
```

---

### 2.7. Armazenamento em Memória

**Regra:** STMT -> EXPR id (epsilon)  
*(corresponde a `(valor MEM)` em RPN)*

**Notação Formal (Infixa):**
```
Γ ⊢ e : T    T ∈ {int, real}
────────────────────────────────────────────────
Γ[x ↦ {tipo: T, inicializada: true}] ⊢ x := e : T
```

**Adaptação RPN:**
```
Sintaxe: (valor MEM)
Onde:
  - valor é uma expressão do tipo T ∈ {int, real}
  - MEM é um identificador (maiúsculas)
  - A operação armazena valor em MEM
  - Resultado tem tipo T
```

**Regra Semântica:**
```
Γ ⊢ EXPR : T    T ∈ {int, real}    id ∉ {RES}
──────────────────────────────────────────────────────────
Γ[id ↦ {tipo: T, inicializada: true}] ⊢ (EXPR id) : T
```

**Ação Semântica:**
- `TabelaSimbolos[id.nome] = {tipo: EXPR.tipo, valor: EXPR.valor, inicializada: true}`

**Atributos Sintetizados:**
- `STMT.tipo = EXPR.tipo`
- `STMT.valor = EXPR.valor`

**Restrição Semântica:**
- ERRO se `EXPR.tipo = booleano` (não pode armazenar booleanos)

**Exemplos RPN:**
```
(42 X)            -> armazena 42 (int) em X, tipo: int
(3.14 PI)         -> armazena 3.14 (real) em PI, tipo: real
((A B +) SOMA)    -> armazena resultado em SOMA
((5 10 >) FLAG)   -> ERRO: não pode armazenar booleano
```

---

### 2.8. Histórico (RES)

**Regra:** STMT -> EXPR res (epsilon)  
*(corresponde a `(N RES)` em RPN)*

**Notação Formal (Infixa):**
```
Γ ⊢ e : int    e.valor ≥ 1    e.valor ≤ linha_atual
historico[linha_atual - e.valor].tipo = T
─────────────────────────────────────────────────
Γ ⊢ RES(e) : T
```

**Adaptação RPN:**
```
Sintaxe: (N RES)
Onde:
  - N é uma expressão do tipo int
  - N ≥ 1 (referencia linha anterior)
  - N ≤ número_de_linhas_anteriores
  - Retorna o resultado da expressão N linhas atrás
  - Resultado tem o tipo da linha referenciada
```

**Regra de Tipo:**
```
Γ ⊢ EXPR : int    EXPR.valor ≥ 1    EXPR.valor ≤ |historico|
historico[|historico| - EXPR.valor].tipo = T
────────────────────────────────────────────────────────────
Γ ⊢ (EXPR RES) : T
```

**Restrição Semântica:**
- ERRO se `EXPR.tipo ≠ int`
- ERRO se `EXPR.valor < 1`
- ERRO se `EXPR.valor > tamanho_do_historico`
- ERRO se linha referenciada não existe ou é inválida

**Atributos Sintetizados:**
- `STMT.tipo = historico[tamanho - EXPR.valor].tipo`
- `STMT.valor = historico[tamanho - EXPR.valor].valor`

**Exemplos RPN:**
```
Linha 1: (5 10 +)     # resultado: 15 (int)
Linha 2: (1 RES)      # retorna 15 (int) da linha 1
Linha 3: (2 RES)      # retorna 15 (int) da linha 1
Linha 4: (0 RES)      # ERRO: N deve ser >= 1
Linha 5: (10 RES)     # ERRO: só existem 4 linhas anteriores
```

---

### 2.9. Estrutura Condicional (IF)

**Regra:** STMT -> EXPR₁ EXPR₂ EXPR₃ if  
*(corresponde a `(cond then else if)` em RPN)*

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : T    Γ ⊢ e₃ : T
──────────────────────────────────────────────
Γ ⊢ if e₁ then e₂ else e₃ : T
```

**Adaptação RPN:**
```
Sintaxe: (cond then else if)
Onde:
  - cond é uma expressão do tipo booleano
  - then é uma expressão do tipo T
  - else é uma expressão do tipo T (mesmo tipo de then)
  - Se cond = true, retorna then
  - Se cond = false, retorna else
  - Resultado tem tipo T
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : booleano    Γ ⊢ EXPR₂ : T    Γ ⊢ EXPR₃ : T
─────────────────────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ EXPR₃ if) : T
```

**Restrição Semântica:**
- ERRO se `EXPR₁.tipo ≠ booleano`
- ERRO se `EXPR₂.tipo ≠ EXPR₃.tipo`

**Atributos Sintetizados:**
- `STMT.tipo = EXPR₂.tipo` (= EXPR₃.tipo)
- `STMT.valor = EXPR₂.valor se EXPR₁.valor = true, senão EXPR₃.valor`

**Exemplos RPN:**
```
((X 0 >) (X) (0 X -) if)     -> se X>0 retorna X, senão -X (valor absoluto)
((A B <) (1) (0) if)         -> retorna 1 se A<B, senão 0
((5 10 <) (3.14) (2.71) if)  -> tipo: real
((5 10 <) (42) (3.14) if)    -> ERRO: ramos com tipos diferentes
((5 10 +) (1) (2) if)        -> ERRO: condição não é booleana
```

---

### 2.10. Laço de Repetição (WHILE)

**Regra:** STMT -> EXPR₁ EXPR₂ while  
*(corresponde a `(cond body while)` em RPN)*

**Notação Formal (Infixa):**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : T
─────────────────────────────────
Γ ⊢ while e₁ do e₂ : T
```

**Adaptação RPN:**
```
Sintaxe: (cond body while)
Onde:
  - cond é uma expressão do tipo booleano
  - body é uma expressão do tipo T
  - Executa body repetidamente enquanto cond = true
  - Resultado tem tipo T (último valor de body)
```

**Regra de Tipo:**
```
Γ ⊢ EXPR₁ : booleano    Γ ⊢ EXPR₂ : T
─────────────────────────────────────
Γ ⊢ (EXPR₁ EXPR₂ while) : T
```

**Restrição Semântica:**
- ERRO se `EXPR₁.tipo ≠ booleano`

**Atributos Sintetizados:**
- `STMT.tipo = EXPR₂.tipo`
- `STMT.valor = último valor de EXPR₂ após execução do laço`

**Exemplos RPN:**
```
((I 10 <) ((I 1 +) I) while)    -> incrementa I enquanto I < 10
((X 0 >) ((X 1 -) X) while)     -> decrementa X enquanto X > 0
((5) ((I 1 +) I) while)         -> ERRO: condição não é booleana
```

---

## 3. Função promoverTipo

```python
def promoverTipo(tipo1, tipo2):
    """
    Promove tipos em operações mistas.
    
    Regras:
    - int + int = int
    - int + real = real
    - real + int = real
    - real + real = real
    - booleano em qualquer operação aritmética = ERRO
    """
    if tipo1 == 'real' or tipo2 == 'real':
        return 'real'
    if tipo1 == 'booleano' or tipo2 == 'booleano':
        return None  # Erro: booleano não pode ser usado em aritmética
    return 'int'
```

---

## 4. Tabela de Tipos para Operações

| Operação | Op₁ | Op₂ | Resultado | Observações |
|----------|-----|-----|-----------|-------------|
| +, -, *, \| | int | int | int | Aritmética inteira |
| +, -, *, \| | int | real | real | Promove para real |
| +, -, *, \| | real | int | real | Promove para real |
| +, -, *, \| | real | real | real | Aritmética real |
| /, % | int | int | int | Divisão/módulo inteiro, Op₂ ≠ 0 |
| /, % | qualquer outro | - | ERRO | Requer ambos int |
| ^ | int | int>0 | int | Expoente positivo |
| ^ | real | int>0 | real | Expoente positivo |
| ^ | qualquer | real | ERRO | Expoente deve ser int |
| ^ | qualquer | ≤0 | ERRO | Expoente deve ser > 0 |
| <, >, <=, >=, ==, != | int/real | int/real | booleano | Comparação numérica |
| <, >, <=, >=, ==, != | booleano | - | ERRO | Não compara booleanos |

---

## 5. Validações Semânticas Implementadas

### 5.1. Validações de Tipo
- Expoente de `^` deve ser inteiro positivo (>= 1)
- Operandos de `/` e `%` devem ser inteiros
- Condições em `if` e `while` devem resultar em booleano
- Operações mistas `int`/`real` promovem para `real`
- Booleanos não podem ser usados em operações aritméticas
- Ramos de `if` devem ter o mesmo tipo

### 5.2. Validações de Memória
- Identificadores devem ser inicializados antes do uso em `(ID)`
- `(valor ID)` define/atualiza a memória `ID`
- Booleanos não podem ser armazenados em memória
- Escopo: cada arquivo é independente

### 5.3. Validações de Comandos Especiais
- `(N RES)`: N deve ser inteiro, N ≥ 1, e linha válida
- `RES` não pode ser usado como identificador de memória
- Linha referenciada por `RES` deve existir e ser válida
- Divisão por zero detectada (quando literal)

### 5.4. Validações de Estruturas de Controle
- `if` requer exatamente 3 operandos: condição, then, else
- `while` requer exatamente 2 operandos: condição, corpo
- Condições devem ser expressões booleanas válidas

---

## 6. Exemplos Completos de Inferência

### Exemplo 1: Operação Aritmética Simples
```
Entrada RPN: (3 5 +)

Derivação:
1. Γ ⊢ 3 : int          (literal)
2. Γ ⊢ 5 : int          (literal)
3. promover_tipo(int, int) = int
4. Γ ⊢ (3 5 +) : int    (resultado)

Resultado: tipo = int, valor = 8
```

### Exemplo 2: Promoção de Tipo
```
Entrada RPN: (3.0 5 +)

Derivação:
1. Γ ⊢ 3.0 : real       (literal com ponto decimal)
2. Γ ⊢ 5 : int          (literal)
3. promover_tipo(real, int) = real
4. Γ ⊢ (3.0 5 +) : real (resultado)

Resultado: tipo = real, valor = 8.0
```

### Exemplo 3: Condicional com Comparação
```
Entrada RPN: ((X 0 >) (X) (0 X -) if)

Derivação:
1. Γ ⊢ X : int          (assume X: int inicializado)
2. Γ ⊢ 0 : int          (literal)
3. Γ ⊢ (X 0 >) : booleano (comparação)
4. Γ ⊢ (X) : int        (ramo then)
5. Γ ⊢ 0 : int          (literal)
6. Γ ⊢ X : int          (referência)
7. Γ ⊢ (0 X -) : int    (ramo else)
8. int = int            (tipos compatíveis)
9. Γ ⊢ ((X 0 >) (X) (0 X -) if) : int

Resultado: tipo = int (valor absoluto de X)
```

### Exemplo 4: Erro Semântico - Divisão Inteira com Real
```
Entrada RPN: (10.0 3 /)

Derivação:
1. Γ ⊢ 10.0 : real      (literal)
2. Γ ⊢ 3 : int          (literal)
3. Operador / requer: int, int
4. real ≠ int            ERRO

ERRO SEMÂNTICO: Operador '/' requer operandos inteiros,
                encontrado 'real' e 'int'
```

### Exemplo 5: Armazenamento e Recuperação
```
Entrada (duas linhas):
Linha 1: (42 X)
Linha 2: (X)

Derivação Linha 1:
1. Γ ⊢ 42 : int
2. Γ[X ↦ {tipo: int, inicializada: true}]
3. Γ ⊢ (42 X) : int

Derivação Linha 2:
1. Γ(X) = {tipo: int, inicializada: true}
2. Γ ⊢ (X) : int

Resultado: Linha 1 armazena 42 em X, Linha 2 retorna 42
```

---

## 7. Correspondência entre Notação Formal e RPN

| Notação Formal (Infixa) | Notação RPN | Tipo |
|-------------------------|-------------|------|
| `e₁ + e₂` | `(e₁ e₂ +)` | promover_tipo(T₁, T₂) |
| `e₁ / e₂` | `(e₁ e₂ /)` | int (se ambos int) |
| `e₁ ^ e₂` | `(e₁ e₂ ^)` | T₁ (se e₂ é int > 0) |
| `e₁ < e₂` | `(e₁ e₂ <)` | booleano |
| `x := e` | `(e x)` | tipo(e) |
| `RES(n)` | `(n RES)` | tipo(linha n atrás) |
| `if e₁ then e₂ else e₃` | `(e₁ e₂ e₃ if)` | tipo(e₂) = tipo(e₃) |
| `while e₁ do e₂` | `(e₁ e₂ while)` | tipo(e₂) |

---

## 8. Notas de Implementação

1. **Ordem de Avaliação**: Em RPN, os operandos sempre vêm antes do operador, facilitando a avaliação em pilha.

2. **Aninhamento**: Expressões podem ser aninhadas sem limite: `((A B +) (C D *) /)` é válido.

3. **Tipos Booleanos**: Resultam apenas de operadores relacionais e só podem ser usados em condições de `if` e `while`.

4. **Histórico**: `RES` usa indexação relativa (1 = linha anterior), não absoluta.

5. **Escopo**: Cada arquivo tem sua própria tabela de símbolos independente.