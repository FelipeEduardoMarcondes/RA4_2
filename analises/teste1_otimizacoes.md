# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 16
- **Instruções otimizadas:** 4
- **Redução:** 12 instruções (75.0%)

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

**Aplicações:** 4

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

**Aplicações:** 12

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
t6 = 4.5
t7 = 5.2
t8 = t6 * t7
# Linha 4
t9 = 100
t10 = 12
t11 = t9 | t10
```

### TAC Otimizado (primeiras 20 linhas)

```
# Linha 1
# Linha 2
# Linha 3
# Linha 4
```

