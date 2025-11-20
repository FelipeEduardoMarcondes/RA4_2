# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 926
- **Instruções otimizadas:** 529
- **Redução:** 397 instruções (42.9%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 9

**Descrição:** Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

### Constant Propagation

**Aplicações:** 137

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

**Aplicações:** 397

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
t0 = 100
MEM[X] = t0
# Linha 2
t1 = 50
MEM[Y] = t1
# Linha 3
t2 = 25
MEM[Z] = t2
# Linha 4
t3 = 3.14159
MEM[PI] = t3
# Linha 5
t4 = 2.71828
MEM[E] = t4
# Linha 6
t5 = 4
t6 = RES[t5]
# Linha 7
t7 = MEM[X]
...
```

### TAC Otimizado (primeiras 20 linhas)

```
# Linha 1
MEM[X] = 100
# Linha 2
MEM[Y] = 50
# Linha 3
MEM[Z] = 25
# Linha 4
MEM[PI] = 3.14159
# Linha 5
MEM[E] = 2.71828
# Linha 6
t6 = RES[4]
# Linha 7
t7 = MEM[X]
t8 = MEM[Y]
t10 = MEM[Z]
# Linha 8
t12 = MEM[X]
t13 = MEM[Y]
t15 = MEM[Z]
...
```

