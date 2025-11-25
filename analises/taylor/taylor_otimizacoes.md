# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 74
- **Instruções otimizadas:** 56
- **Redução:** 18 instruções (24.3%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 0

**Descrição:** Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

### Constant Propagation

**Aplicações:** 19

**Descrição:** Propaga valores constantes através do código.

**Exemplo:**
```
Antes: t1 = 5
       t2 = t1 + 3
Depois: t1 = 5
        t2 = 5 + 3
        (que será reduzido para t2 = 8)
```

### Dead Code Elimination

**Aplicações:** 18

**Descrição:** Remove código que não afeta o resultado do programa.

**IMPORTANTE:** Preserva instruções com efeitos colaterais (PRINT, MEM, RES).

**Exemplo:**
```
Antes: t1 = 5
       t2 = 3  # t2 nunca é usado
       t3 = t1 + 2
Depois: t1 = 5
        t3 = t1 + 2
```

### Redundant Jumps

**Aplicações:** 0

**Descrição:** Remove saltos para a próxima instrução.

**Exemplo:**
```
Antes: goto L1
       L1:
Depois: L1:
```

## Comparação de Código

### TAC Original

```
# Linha 1
t0 = 0.5
MEM[X_VAL] = t0
HIST[t0]
# Linha 2
t1 = MEM[X_VAL]
t2 = 2
t3 = t1 ^ t2
t4 = 2.0
t5 = t3 | t4
MEM[T2] = t5
HIST[t5]
# Linha 3
t6 = MEM[X_VAL]
t7 = 4
t8 = t6 ^ t7
t9 = 24.0
t10 = t8 | t9
MEM[T3] = t10
HIST[t10]
# Linha 4
t11 = MEM[X_VAL]
t12 = 6
t13 = t11 ^ t12
t14 = 24.0
t15 = t13 | t14
t16 = 30.0
t17 = t15 | t16
MEM[T4] = t17
HIST[t17]
# Linha 5
t18 = MEM[X_VAL]
t19 = 8
t20 = t18 ^ t19
t21 = 24.0
t22 = t20 | t21
t23 = 30.0
t24 = t22 | t23
t25 = 56.0
t26 = t24 | t25
MEM[T5] = t26
HIST[t26]
# Linha 6
t27 = MEM[X_VAL]
t28 = 10
t29 = t27 ^ t28
t30 = 24.0
t31 = t29 | t30
t32 = 30.0
t33 = t31 | t32
t34 = 56.0
t35 = t33 | t34
t36 = 90.0
t37 = t35 | t36
MEM[T6] = t37
HIST[t37]
# Linha 7
t38 = 1.0
t39 = MEM[T2]
t40 = t38 - t39
t41 = MEM[T3]
t42 = t40 + t41
t43 = MEM[T4]
t44 = t42 - t43
t45 = MEM[T5]
t46 = t44 + t45
t47 = MEM[T6]
t48 = t46 - t47
MEM[FINAL_COS] = t48
HIST[t48]
# Linha 8
t49 = MEM[FINAL_COS]
HIST[t49]
t50 = PRINT[t49]
```

### TAC Otimizado

```
# Linha 1
MEM[X_VAL] = 0.5
HIST[0.5]
# Linha 2
t1 = MEM[X_VAL]
t3 = t1 ^ 2
t5 = t3 | 2.0
MEM[T2] = t5
HIST[t5]
# Linha 3
t6 = MEM[X_VAL]
t8 = t6 ^ 4
t10 = t8 | 24.0
MEM[T3] = t10
HIST[t10]
# Linha 4
t11 = MEM[X_VAL]
t13 = t11 ^ 6
t15 = t13 | 24.0
t17 = t15 | 30.0
MEM[T4] = t17
HIST[t17]
# Linha 5
t18 = MEM[X_VAL]
t20 = t18 ^ 8
t22 = t20 | 24.0
t24 = t22 | 30.0
t26 = t24 | 56.0
MEM[T5] = t26
HIST[t26]
# Linha 6
t27 = MEM[X_VAL]
t29 = t27 ^ 10
t31 = t29 | 24.0
t33 = t31 | 30.0
t35 = t33 | 56.0
t37 = t35 | 90.0
MEM[T6] = t37
HIST[t37]
# Linha 7
t39 = MEM[T2]
t40 = 1.0 - t39
t41 = MEM[T3]
t42 = t40 + t41
t43 = MEM[T4]
t44 = t42 - t43
t45 = MEM[T5]
t46 = t44 + t45
t47 = MEM[T6]
t48 = t46 - t47
MEM[FINAL_COS] = t48
HIST[t48]
# Linha 8
t49 = MEM[FINAL_COS]
HIST[t49]
t50 = PRINT[t49]
```

