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
2. Nó 'id' (Valor: CONT): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONT' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CONT ↦ {tipo: int}] ⊢ (e₁ CONT) : int
```

---

## Linha 4

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: TEMP): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'TEMP' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[TEMP ↦ {tipo: int}] ⊢ (e₁ TEMP) : int
```

---

## Linha 5

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONT): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 12): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: TEMP): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'TEMP' -> int
9. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
10. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
11. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A' -> int
12. Nó 'id' (Valor: TEMP): Regra 2.2 (Identificador) -> int
13. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
14. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B' -> int
15. Nó 'id' (Valor: CONT): Regra 2.2 (Identificador) -> int
16. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
17. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
18. Nó 'id' (Valor: CONT): Regra 2.2 (Identificador) -> None
19. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONT' -> int
20. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
21. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
22. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
23. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
24. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
25. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 6

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

