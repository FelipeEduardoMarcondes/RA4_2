# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

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

## Linha 2

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

## Linha 3

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 8): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FAT' -> int
9. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
10. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int
14. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
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

## Linha 4

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

