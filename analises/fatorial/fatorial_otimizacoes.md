# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 25
- **Instruções otimizadas:** 21
- **Redução:** 4 instruções (16.0%)

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

**Aplicações:** 5

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

**Aplicações:** 4

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
MEM[N] = t0
t1 = PRINT[t0]
# Linha 2
t2 = 1
MEM[FAT] = t2
t3 = PRINT[t2]
# Linha 3
L0:
t5 = MEM[N]
t6 = 1
t7 = t5 > t6
ifFalse t7 goto L1
t8 = MEM[FAT]
t9 = MEM[N]
t10 = t8 * t9
MEM[FAT] = t10
t4 = t10
goto L0
L1:
t11 = PRINT[t4]
# Linha 4
t12 = MEM[FAT]
t13 = PRINT[t12]
```

### TAC Otimizado

```
# Linha 1
MEM[N] = 5
t1 = PRINT[5]
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
t4 = t10
goto L0
L1:
t11 = PRINT[t4]
# Linha 4
t12 = MEM[FAT]
t13 = PRINT[t12]
```

