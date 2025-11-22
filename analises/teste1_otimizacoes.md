# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 45
- **Instruções otimizadas:** 35
- **Redução:** 10 instruções (22.2%)

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

**Aplicações:** 10

**Descrição:** Remove código que não afeta o resultado do programa.

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

### TAC Original (primeiras 20 linhas)

```
# Linha 1
t0 = 0
MEM[A] = t0
# Linha 2
t1 = 1
MEM[B] = t1
# Linha 3
t2 = 2
MEM[N] = t2
# Linha 4
t3 = MEM[A]
t4 = RES[t3]
# Linha 5
t5 = MEM[B]
t6 = RES[t5]
# Linha 6
t7 = 24
MEM[MAX] = t7
# Linha 7
L0:
...
```

### TAC Otimizado (primeiras 20 linhas)

```
# Linha 1
MEM[A] = 0
# Linha 2
MEM[B] = 1
# Linha 3
MEM[N] = 2
# Linha 4
t3 = MEM[A]
t4 = RES[t3]
# Linha 5
t5 = MEM[B]
t6 = RES[t5]
# Linha 6
MEM[MAX] = 24
# Linha 7
L0:
t9 = MEM[N]
t10 = MEM[MAX]
t11 = t9 < t10
ifFalse t11 goto L1
...
```

