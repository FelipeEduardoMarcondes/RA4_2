# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'X' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[X ↦ {tipo: int}] ⊢ (e₁ X) : int
```

---

## Linha 2

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Y' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Y ↦ {tipo: int}] ⊢ (e₁ Y) : int
```

---

## Linha 3

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 25): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Z' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Z ↦ {tipo: int}] ⊢ (e₁ Z) : int
```

---

## Linha 4

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3.14159): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'PI' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PI ↦ {tipo: real}] ⊢ (e₁ PI) : real
```

---

## Linha 5

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2.71828): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'E' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[E ↦ {tipo: real}] ⊢ (e₁ E) : real
```

---

## Linha 6

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 4

---

## Linha 7

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 8

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 9

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 10

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
5. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : real
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 11

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
4. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 12

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 13

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
4. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
7. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 14

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, real) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 15

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 16

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
6. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, real) = real
```

---

## Linha 17

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
6. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 18

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, int) = real
```

---

## Linha 19

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
8. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
9. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
10. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 20

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 21

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 22

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 23

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(I).tipo = int, Γ(I).inicializada = true
──────────────────────────────────────────────
Γ ⊢ I : int
```

---

## Linha 24

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONTADOR' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CONTADOR ↦ {tipo: int}] ⊢ (e₁ CONTADOR) : int
```

---

## Linha 25

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONTADOR' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 26

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(CONTADOR).tipo = int, Γ(CONTADOR).inicializada = true
──────────────────────────────────────────────
Γ ⊢ CONTADOR : int
```

---

## Linha 27

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 28

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 29

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 30

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 31

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A ↦ {tipo: int}] ⊢ (e₁ A) : int
```

---

## Linha 32

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'C' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[C ↦ {tipo: int}] ⊢ (e₁ C) : int
```

---

## Linha 33

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'D' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[D ↦ {tipo: int}] ⊢ (e₁ D) : int
```

---

## Linha 34

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'F' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[F ↦ {tipo: int}] ⊢ (e₁ F) : int
```

---

## Linha 35

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B ↦ {tipo: int}] ⊢ (e₁ B) : int
```

---

## Linha 36

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: AREA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'AREA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[AREA ↦ {tipo: int}] ⊢ (e₁ AREA) : int
```

---

## Linha 37

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: VOLUME): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'VOLUME' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[VOLUME ↦ {tipo: int}] ⊢ (e₁ VOLUME) : int
```

---

## Linha 38

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 39

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 40

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 6): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 41

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 22): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 42

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 355): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 113): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 43

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 44

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
4. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 45

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 46

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 47

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 48

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 49

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 50

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 51

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 52

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 53

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 54

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[N ↦ {tipo: int}] ⊢ (e₁ N) : int
```

---

## Linha 55

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 56

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(N).tipo = int, Γ(N).inicializada = true
──────────────────────────────────────────────
Γ ⊢ N : int
```

---

## Linha 57

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[SOMA ↦ {tipo: int}] ⊢ (e₁ SOMA) : int
```

---

## Linha 58

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 59

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 60

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int
9. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
10. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
14. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
15. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 61

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(SOMA).tipo = int, Γ(SOMA).inicializada = true
──────────────────────────────────────────────
Γ ⊢ SOMA : int
```

---

## Linha 62

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 63

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
9. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
10. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
11. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
12. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
13. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
14. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
15. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 64

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 65

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FAT' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FAT ↦ {tipo: int}] ⊢ (e₁ FAT) : int
```

---

## Linha 66

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FAT' -> int
9. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
10. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
11. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
14. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
15. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 67

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(FAT).tipo = int, Γ(FAT).inicializada = true
──────────────────────────────────────────────
Γ ⊢ FAT : int
```

---

## Linha 68

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: LIMITE): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'LIMITE' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[LIMITE ↦ {tipo: int}] ⊢ (e₁ LIMITE) : int
```

---

## Linha 69

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONTADOR' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CONTADOR ↦ {tipo: int}] ⊢ (e₁ CONTADOR) : int
```

---

## Linha 70

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[SOMA ↦ {tipo: int}] ⊢ (e₁ SOMA) : int
```

---

## Linha 71

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: LIMITE): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 72

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(SOMA).tipo = int, Γ(SOMA).inicializada = true
──────────────────────────────────────────────
Γ ⊢ SOMA : int
```

---

## Linha 73

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'num' (Valor: 500.5): Regra 2.1 (Literal) -> real
9. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, real) = real
```

---

## Linha 74

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 75

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 76

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 25): Regra 2.1 (Literal) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 77

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 78

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 12): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 79

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 80

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 81

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 82

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 125): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 83

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 84

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 85

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 86

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 6): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 87

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 88

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 89

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 90

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 91

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 92

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 93

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 94

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 95

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 96

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 15): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 15): Regra 2.1 (Literal) -> int
3. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 97

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 98

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 99

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 100

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
3. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ !=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 101

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 102

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 2.5): Regra 2.1 (Literal) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 103

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 104

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, real) = real
```

---

## Linha 105

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 106

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 107

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 108

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0.25): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 109

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 110

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 111

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 112

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 113

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 114

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 22): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 115

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 116

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 117

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 118

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 119

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 120

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
4. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, int) = real
```

---

## Linha 121

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 122

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 123

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 124

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 125

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 126

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
5. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 127

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 128

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
5. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 129

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 130

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 126): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 127): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 131

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 132

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 127): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 127): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 133

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 134

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: -20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 135

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 136

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -50): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 137

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 138

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 139

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 140

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 141

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 142

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 143

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 144

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 145

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 146

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 147

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : booleano
```
Contexto: N = 1

---

## Linha 148

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0.1): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 0.1): Regra 2.1 (Literal) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 149

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 150

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0.1): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 151

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 152

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 12.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 153

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 154

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 60): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2.1): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 155

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 156

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 1.2): Regra 2.1 (Literal) -> real
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, real) = real
```

---

## Linha 157

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 158

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 159

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 160

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 11): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 161

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 162

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 163

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 164

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 165

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 166

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 167

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 168

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 120): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 169

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 1

---

## Linha 170

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 127.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, real) = real
```

---

## Linha 171

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

---

## Linha 172

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 250): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 173

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : real
```
Contexto: N = 1

