# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 118
- **Instruções otimizadas:** 55
- **Redução:** 63 instruções (53.4%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 4

**Descrição:** Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

### Constant Propagation

**Aplicações:** 29

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

**Aplicações:** 63

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
t0 = 2
t1 = 3
t2 = t0 + t1
# Linha 2
t3 = 10
t4 = 5
t5 = t3 - t4
# Linha 3
t6 = 4
t7 = 5
t8 = t6 * t7
# Linha 4
t9 = 100
t10 = 10
t11 = t9 / t10
# Linha 5
t12 = 5
MEM[X] = t12
# Linha 6
...
```

### TAC Otimizado (primeiras 20 linhas)

```
# Linha 1
# Linha 2
# Linha 3
# Linha 4
# Linha 5
MEM[X] = 5
# Linha 6
t13 = MEM[X]
# Linha 7
MEM[A] = 10
# Linha 8
MEM[B] = 20
# Linha 9
MEM[UNUSED] = 99
# Linha 10
t19 = MEM[A]
t20 = MEM[B]
# Linha 11
MEM[A] = 10
# Linha 12
...
```

