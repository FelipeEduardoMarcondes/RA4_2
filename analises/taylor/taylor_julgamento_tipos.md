# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'X_VAL' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[X_VAL ↦ {tipo: real}] ⊢ (e₁ X_VAL) : real
```

---

## Linha 2

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 2.0): Regra 2.1 (Literal) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'id' (Valor: T2): Regra 2.2 (Identificador) -> None
7. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'T2' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T2 ↦ {tipo: real}] ⊢ (e₁ T2) : real
```

---

## Linha 3

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 24.0): Regra 2.1 (Literal) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'id' (Valor: T3): Regra 2.2 (Identificador) -> None
7. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'T3' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T3 ↦ {tipo: real}] ⊢ (e₁ T3) : real
```

---

## Linha 4

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 6): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 24.0): Regra 2.1 (Literal) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'num' (Valor: 30.0): Regra 2.1 (Literal) -> real
7. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
8. Nó 'id' (Valor: T4): Regra 2.2 (Identificador) -> None
9. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'T4' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T4 ↦ {tipo: real}] ⊢ (e₁ T4) : real
```

---

## Linha 5

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 8): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 24.0): Regra 2.1 (Literal) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'num' (Valor: 30.0): Regra 2.1 (Literal) -> real
7. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
8. Nó 'num' (Valor: 56.0): Regra 2.1 (Literal) -> real
9. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
10. Nó 'id' (Valor: T5): Regra 2.2 (Identificador) -> None
11. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'T5' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T5 ↦ {tipo: real}] ⊢ (e₁ T5) : real
```

---

## Linha 6

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X_VAL): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 24.0): Regra 2.1 (Literal) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'num' (Valor: 30.0): Regra 2.1 (Literal) -> real
7. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
8. Nó 'num' (Valor: 56.0): Regra 2.1 (Literal) -> real
9. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
10. Nó 'num' (Valor: 90.0): Regra 2.1 (Literal) -> real
11. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real
12. Nó 'id' (Valor: T6): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'T6' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T6 ↦ {tipo: real}] ⊢ (e₁ T6) : real
```

---

## Linha 7

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1.0): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: T2): Regra 2.2 (Identificador) -> real
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: T3): Regra 2.2 (Identificador) -> real
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'id' (Valor: T4): Regra 2.2 (Identificador) -> real
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real
8. Nó 'id' (Valor: T5): Regra 2.2 (Identificador) -> real
9. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
10. Nó 'id' (Valor: T6): Regra 2.2 (Identificador) -> real
11. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real
12. Nó 'id' (Valor: FINAL_COS): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'FINAL_COS' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FINAL_COS ↦ {tipo: real}] ⊢ (e₁ FINAL_COS) : real
```

---

## Linha 8

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: FINAL_COS): Regra 2.2 (Identificador) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(FINAL_COS).tipo = real, Γ(FINAL_COS).inicializada = true
──────────────────────────────────────────────
Γ ⊢ FINAL_COS : real
```

