# Relatório de Geração de Assembly AVR

**Gerado automaticamente**

## Estatísticas

- **Instruções TAC:** 529
- **Instruções Assembly:** 1500
- **Razão:** 2.84 instruções Assembly por TAC

## Convenções de Registradores

| Registrador | Uso |
|-------------|-----|
| R0-R1 | Resultado de MUL, R1 sempre zero |
| R16-R23 | Variáveis temporárias |
| R24-R25 | Parâmetros e retorno |
| R26-R27 (X) | Ponteiro de dados |
| R28-R29 (Y) | Frame pointer |
| R30-R31 (Z) | Ponteiro de pilha |

## Mapeamento TAC → Assembly

### Operações Aritméticas

```
TAC: t1 = t2 + t3
ASM: mov r16, r17
     add r16, r18

TAC: t1 = t2 * t3
ASM: mul r17, r18
     mov r16, r0
```

### Acesso à Memória

```
TAC: t1 = MEM[X]
ASM: lds r16, X

TAC: MEM[X] = t1
ASM: sts X, r16
```

### Saltos e Rótulos

```
TAC: goto L1
ASM: rjmp L1

TAC: ifFalse t1 goto L1
ASM: cpi r16, 0
     breq L1
```

## Código Assembly Completo

```asm
; Seção de dados
.data
X: .byte 2  ; 0x0100
Y: .byte 2  ; 0x0102
Z: .byte 2  ; 0x0104
PI: .byte 2  ; 0x0106
E: .byte 2  ; 0x0108
I: .byte 2  ; 0x010A
CONTADOR: .byte 2  ; 0x010C
A: .byte 2  ; 0x010E
B: .byte 2  ; 0x0110
C: .byte 2  ; 0x0112
D: .byte 2  ; 0x0114
F: .byte 2  ; 0x0116
N: .byte 2  ; 0x0118
SOMA: .byte 2  ; 0x011A
DELTA: .byte 2  ; 0x011C
R: .byte 2  ; 0x011E
AREA: .byte 2  ; 0x0120
TEMP: .byte 2  ; 0x0122
QUASE_VOL: .byte 2  ; 0x0124
VOLUME: .byte 2  ; 0x0126
FAT: .byte 2  ; 0x0128
LIMITE: .byte 2  ; 0x012A

; Seção de código
.text
; Prólogo do programa

.org 0x0000
    rjmp main

main:
    ; Inicializar pilha
    ldi r16, high(RAMEND)
    out SPH, r16
    ldi r16, low(RAMEND)
    out SPL, r16

    ; Inicializar registradores
    clr r1              ; R1 sempre zero (convenção AVR-GCC)

; Linha 1
    ; TAC: MEM[X] = 100
    ldi r16, 100
    sts X, r16  ; Armazenar em 0x0100

; Linha 2
    ; TAC: MEM[Y] = 50
    ldi r16, 50
...
```
