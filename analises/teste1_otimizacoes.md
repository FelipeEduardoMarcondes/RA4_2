# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 46
- **Instruções otimizadas:** 39
- **Redução:** 7 instruções (15.2%)

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

**Aplicações:** 7

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
MEM[CONT] = t4
t5 = PRINT[t4]
# Linha 4
t6 = 0
MEM[TEMP] = t6
t7 = PRINT[t6]
# Linha 5
L0:
t9 = MEM[CONT]
t10 = 12
t11 = t9 < t10
ifFalse t11 goto L1
t12 = MEM[A]
t13 = MEM[B]
t14 = t12 + t13
MEM[TEMP] = t14
t15 = MEM[B]
MEM[A] = t15
t16 = MEM[TEMP]
MEM[B] = t16
t17 = MEM[CONT]
t18 = 1
t19 = t17 + t18
MEM[CONT] = t19
t20 = MEM[A]
t21 = t19 + t20
t22 = t16 + t21
t23 = t15 + t22
t24 = t14 + t23
t8 = t24
goto L0
L1:
t25 = PRINT[t8]
# Linha 6
t26 = MEM[A]
t27 = PRINT[t26]
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
MEM[CONT] = 0
t5 = PRINT[0]
# Linha 4
MEM[TEMP] = 0
t7 = PRINT[0]
# Linha 5
L0:
t9 = MEM[CONT]
ifFalse t11 goto L1
t12 = MEM[A]
t13 = MEM[B]
t14 = t12 + t13
MEM[TEMP] = t14
t15 = MEM[B]
MEM[A] = t15
t16 = MEM[TEMP]
MEM[B] = t16
t17 = MEM[CONT]
t19 = t17 + 1
MEM[CONT] = t19
t20 = MEM[A]
t21 = t19 + t20
t22 = t16 + t21
t23 = t15 + t22
t24 = t14 + t23
t8 = t24
goto L0
L1:
t25 = PRINT[t8]
# Linha 6
t26 = MEM[A]
t27 = PRINT[t26]
```

