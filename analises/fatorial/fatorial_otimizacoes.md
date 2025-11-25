# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 67
- **Instruções otimizadas:** 52
- **Redução:** 15 instruções (22.4%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 1

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

**Aplicações:** 15

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
t0 = 1
MEM[N] = t0
t1 = PRINT[t0]
# Linha 2
t2 = 1
MEM[FAT] = t2
t3 = PRINT[t2]
# Linha 3
L0:
t5 = MEM[N]
t6 = 8
t7 = t5 <= t6
ifFalse t7 goto L1
t8 = MEM[FAT]
t9 = MEM[N]
t10 = t8 * t9
MEM[FAT] = t10
t11 = MEM[N]
t12 = 1
t13 = t11 + t12
MEM[N] = t13
t14 = t10 * t13
t4 = t14
goto L0
L1:
t15 = PRINT[t4]
# Linha 4
t16 = MEM[FAT]
MEM[RESULTADO] = t16
t17 = PRINT[t16]
# Linha 5
t18 = 1
MEM[NUM] = t18
t19 = PRINT[t18]
# Linha 6
t20 = 1
MEM[FATORIAL1] = t20
t21 = PRINT[t20]
# Linha 7
t22 = 2
MEM[NUM] = t22
t23 = PRINT[t22]
# Linha 8
t24 = 1
t25 = 2
t26 = t24 * t25
t27 = PRINT[t26]
# Linha 9
t28 = 1
t29 = RES[t28]
MEM[FATORIAL2] = t29
t30 = PRINT[t29]
# Linha 10
t31 = 3
MEM[NUM] = t31
t32 = PRINT[t31]
# Linha 11
t33 = 2
t34 = MEM[FATORIAL2]
t35 = t33 * t34
t36 = PRINT[t35]
# Linha 12
t37 = 1
t38 = RES[t37]
MEM[FATORIAL3] = t38
t39 = PRINT[t38]
```

### TAC Otimizado

```
# Linha 1
MEM[N] = 1
t1 = PRINT[1]
# Linha 2
MEM[FAT] = 1
t3 = PRINT[1]
# Linha 3
L0:
t5 = MEM[N]
ifFalse t7 goto L1
t8 = MEM[FAT]
t9 = MEM[N]
t10 = t8 * t9
MEM[FAT] = t10
t11 = MEM[N]
t13 = t11 + 1
MEM[N] = t13
t14 = t10 * t13
t4 = t14
goto L0
L1:
t15 = PRINT[t4]
# Linha 4
t16 = MEM[FAT]
MEM[RESULTADO] = t16
t17 = PRINT[t16]
# Linha 5
MEM[NUM] = 1
t19 = PRINT[1]
# Linha 6
MEM[FATORIAL1] = 1
t21 = PRINT[1]
# Linha 7
MEM[NUM] = 2
t23 = PRINT[2]
# Linha 8
t27 = PRINT[2]
# Linha 9
t29 = RES[1]
MEM[FATORIAL2] = t29
t30 = PRINT[t29]
# Linha 10
MEM[NUM] = 3
t32 = PRINT[3]
# Linha 11
t34 = MEM[FATORIAL2]
t35 = 2 * t34
t36 = PRINT[t35]
# Linha 12
t38 = RES[1]
MEM[FATORIAL3] = t38
t39 = PRINT[t38]
```

