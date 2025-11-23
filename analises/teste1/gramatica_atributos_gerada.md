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

- **Regra:** `Γ(x) = T, Γ(x).inicializada = true ──────────── Γ ⊢ x : T`
- **RPN:** `(X)` -> `tipo: Γ(X).tipo`
- **Sintetizado:** `EXPR.tipo` = `TabelaSimbolos[id.nome].tipo`
- **Restrição:** ERRO se `id.nome` não inicializado.

---

### 2.3 Operações Aritméticas

- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂ ──────────── Γ ⊢ (e₁ e₂ op) : promover_tipo(T₁, T₂)`
