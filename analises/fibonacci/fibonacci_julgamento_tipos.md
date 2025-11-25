# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
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

## Linha 2

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
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

## Linha 3

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

## Linha 4

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
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

## Linha 5

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(A).tipo = int, Γ(A).inicializada = true
──────────────────────────────────────────────
Γ ⊢ A : int
```

---

## Linha 6

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(B).tipo = int, Γ(B).inicializada = true
──────────────────────────────────────────────
Γ ⊢ B : int
```

---

## Linha 7

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: TEMP): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'TEMP' -> int
9. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
10. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
11. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A' -> int
12. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
13. Nó 'id' (Valor: TEMP): Regra 2.2 (Identificador) -> int
14. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
15. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B' -> int
16. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
17. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
18. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
19. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
20. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
21. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
22. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
23. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
24. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
25. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
26. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
27. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
28. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 8

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(A).tipo = int, Γ(A).inicializada = true
──────────────────────────────────────────────
Γ ⊢ A : int
```

---

## Linha 9

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(B).tipo = int, Γ(B).inicializada = true
──────────────────────────────────────────────
Γ ⊢ B : int
```

---

## Linha 10

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(A).tipo = int, Γ(A).inicializada = true
──────────────────────────────────────────────
Γ ⊢ A : int
```

---

## Linha 11

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(B).tipo = int, Γ(B).inicializada = true
──────────────────────────────────────────────
Γ ⊢ B : int
```

---

## Linha 12

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 13

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

