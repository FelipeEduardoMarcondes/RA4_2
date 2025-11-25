# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 63
- **Instruções otimizadas:** 54
- **Redução:** 9 instruções (14.3%)

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

**Aplicações:** 10

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
t0 = 0
MEM[A] = t0
HIST[t0]
# Linha 2
t1 = 1
MEM[B] = t1
HIST[t1]
# Linha 3
t2 = 0
MEM[I] = t2
HIST[t2]
# Linha 4
t3 = 23
MEM[N] = t3
HIST[t3]
# Linha 5
t4 = MEM[A]
HIST[t4]
t5 = PRINT[t4]
# Linha 6
t6 = MEM[B]
HIST[t6]
t7 = PRINT[t6]
# Linha 7
L0:
t9 = MEM[I]
t10 = MEM[N]
t11 = t9 < t10
ifFalse t11 goto L1
t12 = MEM[A]
t13 = MEM[B]
t14 = t12 + t13
MEM[TEMP] = t14
t15 = MEM[B]
MEM[A] = t15
t16 = t14 + t15
t17 = MEM[TEMP]
MEM[B] = t17
t18 = MEM[I]
t19 = 1
t20 = t18 + t19
MEM[I] = t20
t21 = t17 + t20
t22 = t16 + t21
t23 = 0
t24 = t22 > t23
ifFalse t24 goto L2
t26 = MEM[B]
t25 = t26
goto L3
L2:
t27 = MEM[B]
t25 = t27
L3:
t8 = t25
goto L0
L1:
HIST[t8]
# Linha 8
t28 = MEM[B]
HIST[t28]
t29 = PRINT[t28]
```

### TAC Otimizado

```
# Linha 1
MEM[A] = 0
HIST[0]
# Linha 2
MEM[B] = 1
HIST[1]
# Linha 3
MEM[I] = 0
HIST[0]
# Linha 4
MEM[N] = 23
HIST[23]
# Linha 5
t4 = MEM[A]
HIST[t4]
t5 = PRINT[t4]
# Linha 6
t6 = MEM[B]
HIST[t6]
t7 = PRINT[t6]
# Linha 7
L0:
t9 = MEM[I]
t10 = MEM[N]
t11 = t9 < t10
ifFalse t11 goto L1
t12 = MEM[A]
t13 = MEM[B]
t14 = t12 + t13
MEM[TEMP] = t14
t15 = MEM[B]
MEM[A] = t15
t16 = t14 + t15
t17 = MEM[TEMP]
MEM[B] = t17
t18 = MEM[I]
t20 = t18 + 1
MEM[I] = t20
t21 = t17 + t20
t22 = t16 + t21
t24 = t22 > 0
ifFalse t24 goto L2
t26 = MEM[B]
goto L3
L2:
t27 = MEM[B]
L3:
goto L0
L1:
HIST[t8]
# Linha 8
t28 = MEM[B]
HIST[t28]
t29 = PRINT[t28]
```

