# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 29
- **Instruções otimizadas:** 16
- **Redução:** 13 instruções (44.8%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 3

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

**Aplicações:** 13

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
t0 = 5
t1 = PRINT[t0]
# Linha 2
t2 = 10
t3 = PRINT[t2]
# Linha 3
t4 = 5
t5 = 3
t6 = t4 + t5
t7 = PRINT[t6]
# Linha 4
t8 = 10
t9 = 2
t10 = t8 * t9
t11 = PRINT[t10]
# Linha 5
t12 = 100
t13 = 10
t14 = t12 / t13
t15 = PRINT[t14]
# Linha 6
t16 = 1
t17 = RES[t16]
t18 = PRINT[t17]
# Linha 7
t19 = 4
t20 = RES[t19]
t21 = PRINT[t20]
```

### TAC Otimizado

```
# Linha 1
t1 = PRINT[5]
# Linha 2
t3 = PRINT[10]
# Linha 3
t7 = PRINT[8]
# Linha 4
t11 = PRINT[20]
# Linha 5
t15 = PRINT[10]
# Linha 6
t17 = RES[1]
t18 = PRINT[t17]
# Linha 7
t20 = RES[4]
t21 = PRINT[t20]
```

