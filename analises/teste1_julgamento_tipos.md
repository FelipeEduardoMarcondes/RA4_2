# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 2

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 3

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
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

## Linha 4

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
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

## Linha 5

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
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

## Linha 6

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 7

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
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

## Linha 8

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
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

## Linha 9

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 99): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: UNUSED): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'UNUSED' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[UNUSED ↦ {tipo: int}] ⊢ (e₁ UNUSED) : int
```

---

## Linha 10

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 11

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
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

## Linha 12

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
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

## Linha 13

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
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

## Linha 14

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
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

## Linha 15

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 16

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
4. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
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

## Linha 17

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
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

## Linha 18

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
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

## Linha 19

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
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

## Linha 20

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 200): Regra 2.1 (Literal) -> int
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

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
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

## Linha 22

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'M' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[M ↦ {tipo: int}] ⊢ (e₁ M) : int
```

---

## Linha 23

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: K): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'K' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[K ↦ {tipo: int}] ⊢ (e₁ K) : int
```

---

## Linha 24

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: K): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 25

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3.14): Regra 2.1 (Literal) -> real
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

## Linha 26

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2.0): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, real) = real
```

---

## Linha 27

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

## Linha 28

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 8): Regra 2.1 (Literal) -> int
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

## Linha 29

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
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

