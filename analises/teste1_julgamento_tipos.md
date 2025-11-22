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

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
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

## Linha 4

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = A

---

## Linha 5

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = B

---

## Linha 6

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 24): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'MAX' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MAX ↦ {tipo: int}] ⊢ (e₁ MAX) : int
```

---

## Linha 7

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'C' -> int
9. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
10. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, None) -> None
12. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
13. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
14. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A' -> int
15. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
16. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
17. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B' -> int
18. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
19. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, int) -> None
20. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
21. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
22. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
23. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
24. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int
25. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, int) -> None
26. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:None) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : None
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : None
```
**Restrição:** booleano == booleano

