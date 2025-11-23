# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 57
- **Instruções otimizadas:** 46
- **Redução:** 11 instruções (19.3%)

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

**Aplicações:** 11

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
t1 = PRINT[t0]
# Linha 2
t2 = 1
MEM[B] = t2
t3 = PRINT[t2]
# Linha 3
t4 = 0
MEM[I] = t4
t5 = PRINT[t4]
# Linha 4
t6 = 12
MEM[N] = t6
t7 = PRINT[t6]
# Linha 5
t8 = MEM[A]
t9 = PRINT[t8]
# Linha 6
t10 = MEM[B]
t11 = PRINT[t10]
# Linha 7
L0:
t13 = MEM[I]
t14 = MEM[N]
t15 = t13 < t14
ifFalse t15 goto L1
t16 = MEM[A]
t17 = MEM[B]
t18 = t16 + t17
MEM[TEMP] = t18
t19 = MEM[B]
MEM[A] = t19
t20 = t18 + t19
t21 = MEM[TEMP]
MEM[B] = t21
t22 = MEM[I]
t23 = 1
t24 = t22 + t23
MEM[I] = t24
t25 = t21 + t24
t26 = t20 + t25
t27 = 0
t28 = t26 > t27
ifFalse t28 goto L2
t30 = MEM[B]
t29 = t30
goto L3
L2:
t31 = MEM[B]
t29 = t31
L3:
t12 = t29
goto L0
L1:
t32 = PRINT[t12]
```

### TAC Otimizado

```
# Linha 1
MEM[A] = 0
t1 = PRINT[0]
# Linha 2
MEM[B] = 1
t3 = PRINT[1]
# Linha 3
MEM[I] = 0
t5 = PRINT[0]
# Linha 4
MEM[N] = 12
t7 = PRINT[12]
# Linha 5
t8 = MEM[A]
t9 = PRINT[t8]
# Linha 6
t10 = MEM[B]
t11 = PRINT[t10]
# Linha 7
L0:
t13 = MEM[I]
t14 = MEM[N]
ifFalse t15 goto L1
t16 = MEM[A]
t17 = MEM[B]
t18 = t16 + t17
MEM[TEMP] = t18
t19 = MEM[B]
MEM[A] = t19
t21 = MEM[TEMP]
MEM[B] = t21
t22 = MEM[I]
t24 = t22 + 1
MEM[I] = t24
ifFalse t28 goto L2
t30 = MEM[B]
t29 = t30
goto L3
L2:
t31 = MEM[B]
t29 = t31
L3:
t12 = t29
goto L0
L1:
t32 = PRINT[t12]
```

