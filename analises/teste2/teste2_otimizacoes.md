# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 176
- **Instruções otimizadas:** 142
- **Redução:** 34 instruções (19.3%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 2

**Descrição:** Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

### Constant Propagation

**Aplicações:** 36

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

**Aplicações:** 34

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
t0 = 100
MEM[X] = t0
t1 = PRINT[t0]
# Linha 2
t2 = 50
MEM[Y] = t2
t3 = PRINT[t2]
# Linha 3
t4 = 25
MEM[Z] = t4
t5 = PRINT[t4]
# Linha 4
t6 = 3.14
MEM[PI] = t6
t7 = PRINT[t6]
# Linha 5
t8 = 2.71
MEM[E] = t8
t9 = PRINT[t8]
# Linha 6
t10 = 4
t11 = RES[t10]
t12 = PRINT[t11]
# Linha 7
t13 = MEM[X]
t14 = MEM[Y]
t15 = t13 + t14
t16 = MEM[Z]
t17 = t15 - t16
t18 = PRINT[t17]
# Linha 8
t19 = MEM[X]
t20 = MEM[Y]
t21 = t19 * t20
t22 = MEM[Z]
t23 = t21 / t22
t24 = PRINT[t23]
# Linha 9
t25 = 10
MEM[A] = t25
t26 = PRINT[t25]
# Linha 10
t27 = 5
MEM[B] = t27
t28 = PRINT[t27]
# Linha 11
t29 = 2
MEM[C] = t29
t30 = PRINT[t29]
# Linha 12
t31 = MEM[A]
t32 = MEM[B]
t33 = t31 + t32
t34 = MEM[C]
t35 = t33 - t34
t36 = PRINT[t35]
# Linha 13
t37 = MEM[A]
t38 = MEM[B]
t39 = t37 * t38
t40 = MEM[C]
t41 = t39 / t40
t42 = PRINT[t41]
# Linha 14
t43 = MEM[A]
t44 = 2
t45 = t43 ^ t44
t46 = MEM[B]
t47 = 2
t48 = t46 ^ t47
t49 = t45 + t48
t50 = PRINT[t49]
# Linha 15
t51 = MEM[E]
t52 = MEM[A]
t53 = MEM[B]
t54 = t52 | t53
t55 = t51 + t54
t56 = PRINT[t55]
# Linha 16
t57 = 1
t58 = 3
t59 = t57 | t58
t60 = PRINT[t59]
# Linha 17
t61 = 22
t62 = 7
t63 = t61 | t62
t64 = PRINT[t63]
# Linha 18
t65 = MEM[A]
t66 = MEM[B]
t67 = t65 > t66
ifFalse t67 goto L0
t69 = 1
t68 = t69
goto L1
L0:
t70 = 0
t68 = t70
L1:
t71 = PRINT[t68]
# Linha 19
t72 = MEM[A]
t73 = MEM[B]
t74 = t72 < t73
ifFalse t74 goto L2
t76 = 1
t75 = t76
goto L3
L2:
t77 = 0
t75 = t77
L3:
t78 = PRINT[t75]
# Linha 20
t79 = MEM[A]
t80 = MEM[B]
t81 = t79 % t80
t82 = MEM[C]
t83 = t81 + t82
t84 = PRINT[t83]
# Linha 21
t85 = MEM[A]
t86 = 5
t87 = t85 > t86
ifFalse t87 goto L4
t89 = MEM[A]
t90 = 1
t91 = t89 - t90
t88 = t91
goto L5
L4:
t92 = MEM[A]
t93 = 1
t94 = t92 + t93
t88 = t94
L5:
t95 = PRINT[t88]
# Linha 22
t96 = MEM[B]
t97 = MEM[C]
t98 = t96 == t97
ifFalse t98 goto L6
t100 = 1
t99 = t100
goto L7
L6:
t101 = -1
t99 = t101
L7:
t102 = PRINT[t99]
# Linha 23
t103 = 0
MEM[I] = t103
t104 = PRINT[t103]
# Linha 24
L8:
t106 = MEM[I]
t107 = 5
t108 = t106 < t107
ifFalse t108 goto L9
t109 = MEM[I]
t110 = 1
t111 = t109 + t110
MEM[I] = t111
t112 = MEM[I]
t113 = t111 + t112
t105 = t113
goto L8
L9:
t114 = PRINT[t105]
# Linha 25
t115 = MEM[I]
t116 = PRINT[t115]
```

### TAC Otimizado

```
# Linha 1
MEM[X] = 100
t1 = PRINT[100]
# Linha 2
MEM[Y] = 50
t3 = PRINT[50]
# Linha 3
MEM[Z] = 25
t5 = PRINT[25]
# Linha 4
MEM[PI] = 3.14
t7 = PRINT[3.14]
# Linha 5
MEM[E] = 2.71
t9 = PRINT[2.71]
# Linha 6
t11 = RES[4]
t12 = PRINT[t11]
# Linha 7
t13 = MEM[X]
t14 = MEM[Y]
t15 = t13 + t14
t16 = MEM[Z]
t17 = t15 - t16
t18 = PRINT[t17]
# Linha 8
t19 = MEM[X]
t20 = MEM[Y]
t21 = t19 * t20
t22 = MEM[Z]
t23 = t21 / t22
t24 = PRINT[t23]
# Linha 9
MEM[A] = 10
t26 = PRINT[10]
# Linha 10
MEM[B] = 5
t28 = PRINT[5]
# Linha 11
MEM[C] = 2
t30 = PRINT[2]
# Linha 12
t31 = MEM[A]
t32 = MEM[B]
t33 = t31 + t32
t34 = MEM[C]
t35 = t33 - t34
t36 = PRINT[t35]
# Linha 13
t37 = MEM[A]
t38 = MEM[B]
t39 = t37 * t38
t40 = MEM[C]
t41 = t39 / t40
t42 = PRINT[t41]
# Linha 14
t43 = MEM[A]
t45 = t43 ^ 2
t46 = MEM[B]
t48 = t46 ^ 2
t49 = t45 + t48
t50 = PRINT[t49]
# Linha 15
t51 = MEM[E]
t52 = MEM[A]
t53 = MEM[B]
t54 = t52 | t53
t55 = t51 + t54
t56 = PRINT[t55]
# Linha 16
t60 = PRINT[0.3333333333333333]
# Linha 17
t64 = PRINT[3.142857142857143]
# Linha 18
t65 = MEM[A]
t66 = MEM[B]
ifFalse t67 goto L0
t68 = 1
goto L1
L0:
t68 = 0
L1:
t71 = PRINT[t68]
# Linha 19
t72 = MEM[A]
t73 = MEM[B]
ifFalse t74 goto L2
t75 = 1
goto L3
L2:
t75 = 0
L3:
t78 = PRINT[t75]
# Linha 20
t79 = MEM[A]
t80 = MEM[B]
t81 = t79 % t80
t82 = MEM[C]
t83 = t81 + t82
t84 = PRINT[t83]
# Linha 21
t85 = MEM[A]
ifFalse t87 goto L4
t89 = MEM[A]
t91 = t89 - 1
t88 = t91
goto L5
L4:
t92 = MEM[A]
t94 = t92 + 1
t88 = t94
L5:
t95 = PRINT[t88]
# Linha 22
t96 = MEM[B]
t97 = MEM[C]
ifFalse t98 goto L6
t99 = 1
goto L7
L6:
t99 = -1
L7:
t102 = PRINT[t99]
# Linha 23
MEM[I] = 0
t104 = PRINT[0]
# Linha 24
L8:
t106 = MEM[I]
ifFalse t108 goto L9
t109 = MEM[I]
t111 = t109 + 1
MEM[I] = t111
t112 = MEM[I]
t113 = t111 + t112
t105 = t113
goto L8
L9:
t114 = PRINT[t105]
# Linha 25
t115 = MEM[I]
t116 = PRINT[t115]
```

