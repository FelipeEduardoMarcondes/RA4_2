# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 31
- **Instruções otimizadas:** 25
- **Redução:** 6 instruções (19.4%)

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

**Aplicações:** 6

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
HIST[t0]
# Linha 2
t1 = 1
MEM[FAT] = t1
HIST[t1]
# Linha 3
L0:
t3 = MEM[N]
t4 = 8
t5 = t3 <= t4
ifFalse t5 goto L1
t6 = MEM[FAT]
t7 = MEM[N]
t8 = t6 * t7
MEM[FAT] = t8
t9 = MEM[N]
t10 = 1
t11 = t9 + t10
MEM[N] = t11
t12 = t8 * t11
t2 = t12
goto L0
L1:
HIST[t2]
# Linha 4
t13 = MEM[FAT]
HIST[t13]
t14 = PRINT[t13]
```

### TAC Otimizado

```
# Linha 1
MEM[N] = 1
HIST[1]
# Linha 2
MEM[FAT] = 1
HIST[1]
# Linha 3
L0:
t3 = MEM[N]
t5 = t3 <= 8
ifFalse t5 goto L1
t6 = MEM[FAT]
t7 = MEM[N]
t8 = t6 * t7
MEM[FAT] = t8
t9 = MEM[N]
t11 = t9 + 1
MEM[N] = t11
goto L0
L1:
HIST[t2]
# Linha 4
t13 = MEM[FAT]
HIST[t13]
t14 = PRINT[t13]
```

