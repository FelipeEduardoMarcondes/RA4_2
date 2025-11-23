# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -5): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ -5 : int
```

---

## Linha 2

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -10): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ -10 : int
```

---

## Linha 3

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: -3): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 4

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: -2.5): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 5

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: -2.52): Regra 2.1 (Literal) -> real
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, real) = real
```

---

## Linha 6

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

## Linha 7

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

