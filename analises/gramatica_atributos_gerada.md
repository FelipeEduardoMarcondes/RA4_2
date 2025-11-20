# Gramática de Atributos - Linguagem RPN

**Gerado automaticamente pelo compilador (Versão Completa)**

## 1. Atributos


        Gramática de Atributos - Linguagem RPN
        
        Atributos principais:
        - tipo: {int, real, booleano}
        - valor: valor calculado (quando aplicável)
        - inicializada: boolean (para identificadores)
        - linha: número da linha no código fonte
        

## 2. Regras de Produção com Atributos

Para cada nó da árvore, calculamos os seguintes atributos **sintetizados**:
- **tipo**: {int, real, booleano}
- **valor**: Valor computado (se aplicável)

---

### 2.1 Literais (EXPR -> num)

- **Regra:** `Γ ⊢ num : int` (se `num` é inteiro); `Γ ⊢ num : real` (se `num` tem ponto decimal)
- **RPN:** `(5)` -> `tipo: int` | `(5.0)` -> `tipo: real`
- **Sintetizado:** `EXPR.tipo` = `int` ou `real`

---

### 2.2 Identificadores (EXPR -> id)

- **Regra:** `Γ(x) = T, Γ(x).inicializada = true ──────────────── Γ ⊢ x : T`
- **RPN:** `(X)` -> `tipo: Γ(X).tipo`
- **Sintetizado:** `EXPR.tipo` = `TabelaSimbolos[id.nome].tipo`
- **Restrição:** ERRO se `id.nome` não inicializado.

---

### 2.3 Operações Aritméticas (STMT -> EXPR₁ EXPR₂ op_bin) (op ∈ {+, -, *, |})

- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂ ──────────────── Γ ⊢ (e₁ e₂ op) : promover_tipo(T₁, T₂)`
- **RPN:** `(3.0 5 +)` -> `tipo: real`
- **Sintetizado:** `STMT.tipo` = `promover_tipo(EXPR₁.tipo, EXPR₂.tipo)`.
- **Restrição:** ERRO se `T₁` ou `T₂` for `booleano`.

---

### 2.4 Divisão Inteira/Módulo (STMT -> EXPR₁ EXPR₂ op_bin) (op ∈ {/, %})

- **Regra:** `Γ ⊢ e₁ : int, Γ ⊢ e₂ : int, e₂.valor ≠ 0 ──────────────── Γ ⊢ (e₁ e₂ op) : int`
- **RPN:** `(10 3 /)` -> `tipo: int`
- **Sintetizado:** `STMT.tipo` = `int`
- **Restrição:** ERRO se `EXPR₁.tipo ≠ int` ou `EXPR₂.tipo ≠ int`.

---

### 2.5 Potenciação (STMT -> EXPR₁ EXPR₂ pow)

- **Regra:** `Γ ⊢ e₁ : T, Γ ⊢ e₂ : int, e₂.valor > 0 ──────────────── Γ ⊢ (e₁ e₂ ^) : T`
- **RPN:** `(2.0 3 ^)` -> `tipo: real`
- **Sintetizado:** `STMT.tipo` = `EXPR₁.tipo`
- **Restrição:** ERRO se `EXPR₂.tipo ≠ int` ou `EXPR₂.valor ≤ 0`.

---

### 2.6 Operadores Relacionais (STMT -> EXPR₁ EXPR₂ op_rel)

- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂, T₁,T₂ ∈ {int, real} ──────────────── Γ ⊢ (e₁ e₂ op) : booleano`
- **RPN:** `(X 10 <)` -> `tipo: booleano`
- **Sintetizado:** `STMT.tipo` = `booleano`
- **Restrição:** ERRO se `T₁` ou `T₂` ∉ `{int, real}`.

---

### 2.7 Armazenamento (STMT -> EXPR id)

- **Regra:** `Γ ⊢ e : T, T ∈ {int, real} ──────────────── Γ[id ↦ {tipo:T}] ⊢ (e id) : T`
- **RPN:** `(42 X)` -> `tipo: int` (Efeito colateral: atualiza `Γ(X)`)
- **Sintetizado:** `STMT.tipo` = `EXPR.tipo`
- **Restrição:** ERRO se `EXPR.tipo = booleano`.

---

### 2.8 Histórico (STMT -> EXPR res)

- **Regra:** `Γ ⊢ e : int, e.valor ≥ 1, ... ──────────────── Γ ⊢ (e RES) : T` (onde T = tipo da linha referenciada)
- **RPN:** `(1 RES)` -> `tipo: T` (tipo da linha anterior)
- **Sintetizado:** `STMT.tipo` = `historico[tamanho - EXPR.valor].tipo`
- **Restrição:** ERRO se `EXPR.tipo ≠ int` ou `EXPR.valor < 1`.

---

### 2.9 Condicional (STMT -> EXPR₁ EXPR₂ EXPR₃ if)

- **Regra:** `Γ ⊢ e₁ : booleano, Γ ⊢ e₂ : T, Γ ⊢ e₃ : T ──────────────── Γ ⊢ (e₁ e₂ e₃ if) : T`
- **RPN:** `((X 0 >) (1) (0) if)` -> `tipo: int`
- **Sintetizado:** `STMT.tipo` = `EXPR₂.tipo`
- **Restrição:** ERRO se `EXPR₁.tipo ≠ booleano` ou `EXPR₂.tipo ≠ EXPR₃.tipo`.

---

### 2.10 Laço (STMT -> EXPR₁ EXPR₂ while)

- **Regra:** `Γ ⊢ e₁ : booleano, Γ ⊢ e₂ : T ──────────────── Γ ⊢ (e₁ e₂ while) : T`
- **RPN:** `((I 10 <) ((I 1 +) I) while)` -> `tipo: int` (tipo do corpo `T`)
- **Sintetizado:** `STMT.tipo` = `EXPR₂.tipo`
- **Restrição:** ERRO se `EXPR₁.tipo ≠ booleano`.

---

## 3. Tabela de Operadores (Extraída de `definirGramaticaAtributos`)

| Operador | Função de Tipo |
|----------|----------------|
| `plus` | promover_tipo(T₁, T₂) |
| `minus` | promover_tipo(T₁, T₂) |
| `mult` | promover_tipo(T₁, T₂) |
| `div_real` | promover_tipo(T₁, T₂) |
| `div_int` | int se T₁=int ∧ T₂=int |
| `mod` | int se T₁=int ∧ T₂=int |
| `pow` | T₁ se T₂=int |
| `lt` | booleano se T₁,T₂ ∈ {int,real} |
| `gt` | booleano se T₁,T₂ ∈ {int,real} |
| `lte` | booleano se T₁,T₂ ∈ {int,real} |
| `gte` | booleano se T₁,T₂ ∈ {int,real} |
| `eq` | booleano se T₁,T₂ ∈ {int,real} |
| `neq` | booleano se T₁,T₂ ∈ {int,real} |
