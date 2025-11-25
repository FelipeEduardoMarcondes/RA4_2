# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 16
- **Instruções otimizadas:** 15
- **Redução:** 1 instruções (6.2%)

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

**Aplicações:** 2

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

**Aplicações:** 1

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
t0 = 6666
MEM[A] = t0
t1 = PRINT[t0]
# Linha 2
t2 = MEM[A]
t3 = PRINT[t2]
# Linha 3
t4 = MEM[A]
t5 = PRINT[t4]
# Linha 4
t6 = MEM[A]
t7 = PRINT[t6]
# Linha 5
t8 = MEM[A]
t9 = PRINT[t8]
```

### TAC Otimizado

```
# Linha 1
MEM[A] = 6666
t1 = PRINT[6666]
# Linha 2
t2 = MEM[A]
t3 = PRINT[t2]
# Linha 3
t4 = MEM[A]
t5 = PRINT[t4]
# Linha 4
t6 = MEM[A]
t7 = PRINT[t6]
# Linha 5
t8 = MEM[A]
t9 = PRINT[t8]
```

