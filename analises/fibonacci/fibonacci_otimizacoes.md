# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 49
- **Instruções otimizadas:** 41
- **Redução:** 8 instruções (16.3%)

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

**Aplicações:** 6

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

**Aplicações:** 8

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
# Linha 2
t1 = 1
MEM[B] = t1
# Linha 3
t2 = 0
MEM[I] = t2
# Linha 4
t3 = 23
MEM[N] = t3
# Linha 5
t4 = MEM[A]
# Linha 6
t5 = MEM[B]
# Linha 7
L0:
t6 = MEM[I]
t7 = MEM[N]
t8 = t6 < t7
ifFalse t8 goto L1
t9 = MEM[A]
t10 = MEM[B]
t11 = t9 + t10
MEM[TEMP] = t11
t12 = MEM[B]
MEM[A] = t12
t13 = t11 + t12
t14 = MEM[TEMP]
MEM[B] = t14
t15 = MEM[I]
t16 = 1
t17 = t15 + t16
MEM[I] = t17
t18 = t14 + t17
t19 = t13 + t18
t20 = 0
t21 = t19 > t20
ifFalse t21 goto L2
t23 = MEM[B]
t22 = t23
goto L3
L2:
t24 = MEM[B]
t22 = t24
L3:
goto L0
L1:
```

### TAC Otimizado

```
# Linha 1
MEM[A] = 0
# Linha 2
MEM[B] = 1
# Linha 3
MEM[I] = 0
# Linha 4
MEM[N] = 23
# Linha 5
t4 = MEM[A]
# Linha 6
t5 = MEM[B]
# Linha 7
L0:
t6 = MEM[I]
t7 = MEM[N]
t8 = t6 < t7
ifFalse t8 goto L1
t9 = MEM[A]
t10 = MEM[B]
t11 = t9 + t10
MEM[TEMP] = t11
t12 = MEM[B]
MEM[A] = t12
t13 = t11 + t12
t14 = MEM[TEMP]
MEM[B] = t14
t15 = MEM[I]
t17 = t15 + 1
MEM[I] = t17
t18 = t14 + t17
t19 = t13 + t18
t21 = t19 > 0
ifFalse t21 goto L2
t23 = MEM[B]
goto L3
L2:
t24 = MEM[B]
L3:
goto L0
L1:
```

