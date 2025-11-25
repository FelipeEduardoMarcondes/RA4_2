# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 48
- **Instruções otimizadas:** 39
- **Redução:** 9 instruções (18.8%)

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

**Aplicações:** 11

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

**Aplicações:** 9

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
t1 = 1.0
MEM[T1] = t1
HIST[t1]
# Linha 3
t2 = MEM[X_VAL]
t3 = 2
t4 = t2 ^ t3
t5 = 2.0
t6 = t4 | t5
MEM[T2] = t6
HIST[t6]
# Linha 4
t7 = MEM[X_VAL]
t8 = 4
t9 = t7 ^ t8
t10 = 24.0
t11 = t9 | t10
MEM[T3] = t11
HIST[t11]
# Linha 5
t12 = MEM[X_VAL]
t13 = 6
t14 = t12 ^ t13
t15 = 24.0
t16 = t14 | t15
t17 = 30.0
t18 = t16 | t17
MEM[T4] = t18
HIST[t18]
# Linha 6
t19 = MEM[T1]
t20 = MEM[T2]
t21 = t19 - t20
t22 = MEM[T3]
t23 = t21 + t22
t24 = MEM[T4]
t25 = t23 - t24
MEM[FINAL_COS] = t25
HIST[t25]
# Linha 7
t26 = MEM[FINAL_COS]
HIST[t26]
t27 = PRINT[t26]
```

### TAC Otimizado

```
# Linha 1
MEM[X_VAL] = 0.5
HIST[0.5]
# Linha 2
MEM[T1] = 1.0
HIST[1.0]
# Linha 3
t2 = MEM[X_VAL]
t4 = t2 ^ 2
t6 = t4 | 2.0
MEM[T2] = t6
HIST[t6]
# Linha 4
t7 = MEM[X_VAL]
t9 = t7 ^ 4
t11 = t9 | 24.0
MEM[T3] = t11
HIST[t11]
# Linha 5
t12 = MEM[X_VAL]
t14 = t12 ^ 6
t16 = t14 | 24.0
t18 = t16 | 30.0
MEM[T4] = t18
HIST[t18]
# Linha 6
t19 = MEM[T1]
t20 = MEM[T2]
t21 = t19 - t20
t22 = MEM[T3]
t23 = t21 + t22
t24 = MEM[T4]
t25 = t23 - t24
MEM[FINAL_COS] = t25
HIST[t25]
# Linha 7
t26 = MEM[FINAL_COS]
HIST[t26]
t27 = PRINT[t26]
```

