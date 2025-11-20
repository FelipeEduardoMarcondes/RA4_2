# Relatório de Geração de Assembly AVR

**Gerado automaticamente**

## Estatísticas

- **Instruções TAC:** 55
- **Instruções Assembly:** 128
- **Razão:** 2.33 instruções Assembly por TAC

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
A: .byte 2  ; 0x0102
B: .byte 2  ; 0x0104
C: .byte 2  ; 0x0106
N: .byte 2  ; 0x0108
M: .byte 2  ; 0x010A
K: .byte 2  ; 0x010C
PI: .byte 2  ; 0x010E

; Seção de código
.text
; Prólogo do programa
.include "m328Pdef.inc"

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
; Linha 2
; Linha 3
; Linha 4
; Linha 5
    ; TAC: MEM[X] = 5
    ; AVISO: Instrução não mapeada: MEM[X] = 5
; Linha 6
    ; TAC: t13 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

; Linha 7
    ; TAC: MEM[A] = 10
    ; AVISO: Instrução não mapeada: MEM[A] = 10
; Linha 8
    ; TAC: MEM[B] = 20
    ; AVISO: Instrução não mapeada: MEM[B] = 20
; Linha 9
    ; TAC: MEM[UNUSED] = 99
    ; AVISO: Instrução não mapeada: MEM[UNUSED] = 99
; Linha 10
...
```
