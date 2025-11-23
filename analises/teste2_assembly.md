# Relatório de Geração de Assembly AVR

**Gerado automaticamente**

## Arquitetura

- **Processador:** ATmega328P (Arduino Uno)
- **Arquitetura:** AVR 8-bit Load-Store
- **Precisão Numérica:** 16-bit signed integers
- **Comunicação:** Serial UART 9600 baud

## Estatísticas

- **Instruções TAC:** 732
- **Linhas Assembly:** 9466

## TAC Otimizado (primeiras 30 linhas)

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
MEM[PI] = 3.14159
t7 = PRINT[3.14159]
# Linha 5
MEM[E] = 2.71828
t9 = PRINT[2.71828]
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
...
```

## Assembly Gerado (primeiras 80 linhas)

```asm
; Seção de Dados
.data
A: .byte 2
AREA: .byte 2
B: .byte 2
C: .byte 2
CONTADOR: .byte 2
D: .byte 2
DELTA: .byte 2
E: .byte 2
F: .byte 2
FAT: .byte 2
I: .byte 2
LIMITE: .byte 2
N: .byte 2
PI: .byte 2
QUASE_VOL: .byte 2
R: .byte 2
SOMA: .byte 2
TEMP: .byte 2
VOLUME: .byte 2
X: .byte 2
Y: .byte 2
Z: .byte 2
t1: .byte 2
t101: .byte 2
t102: .byte 2
t104: .byte 2
t105: .byte 2
t106: .byte 2
t107: .byte 2
t108: .byte 2
t109: .byte 2
t11: .byte 2
t110: .byte 2
t111: .byte 2
t112: .byte 2
t113: .byte 2
t114: .byte 2
t116: .byte 2
t117: .byte 2
t119: .byte 2
t12: .byte 2
t120: .byte 2
t121: .byte 2
t122: .byte 2
t124: .byte 2
t125: .byte 2
t127: .byte 2
t128: .byte 2
t129: .byte 2
t13: .byte 2
t130: .byte 2
t131: .byte 2
t132: .byte 2
t133: .byte 2
t134: .byte 2
t136: .byte 2
t137: .byte 2
t14: .byte 2
t145: .byte 2
t146: .byte 2
t147: .byte 2
t148: .byte 2
t149: .byte 2
t15: .byte 2
t151: .byte 2
t152: .byte 2
t153: .byte 2
t154: .byte 2
t156: .byte 2
t157: .byte 2
t158: .byte 2
t16: .byte 2
t160: .byte 2
t161: .byte 2
t163: .byte 2
t164: .byte 2
t165: .byte 2
t166: .byte 2
...
```
