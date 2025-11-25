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

## Linha 4

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: FAT): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: RESULTADO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'RESULTADO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[RESULTADO ↦ {tipo: int}] ⊢ (e₁ RESULTADO) : int
```

---

## Linha 5

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: NUM): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'NUM' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[NUM ↦ {tipo: int}] ⊢ (e₁ NUM) : int
```

---

## Linha 6

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: FATORIAL1): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FATORIAL1' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FATORIAL1 ↦ {tipo: int}] ⊢ (e₁ FATORIAL1) : int
```

---

## Linha 7

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: NUM): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'NUM' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[NUM ↦ {tipo: int}] ⊢ (e₁ NUM) : int
```

---

## Linha 8

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
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

## Linha 9

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
3. Nó 'id' (Valor: FATORIAL2): Regra 2.2 (Identificador) -> None
4. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FATORIAL2' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FATORIAL2 ↦ {tipo: int}] ⊢ (e₁ FATORIAL2) : int
```

---

## Linha 10

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: NUM): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'NUM' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[NUM ↦ {tipo: int}] ⊢ (e₁ NUM) : int
```

---

## Linha 11

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: FATORIAL2): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 12

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
3. Nó 'id' (Valor: FATORIAL3): Regra 2.2 (Identificador) -> None
4. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FATORIAL3' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FATORIAL3 ↦ {tipo: int}] ⊢ (e₁ FATORIAL3) : int
```

