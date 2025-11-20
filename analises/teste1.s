; Assembly AVR para Arduino Uno (ATmega328P)
; Gerado automaticamente

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
    ; TAC: t19 = MEM[A]
    lds r17, A  ; Carregar de 0x0102

    ; TAC: t20 = MEM[B]
    lds r18, B  ; Carregar de 0x0104

; Linha 11
    ; TAC: MEM[A] = 10
    ; AVISO: Instrução não mapeada: MEM[A] = 10
; Linha 12
    ; TAC: t23 = MEM[A]
    lds r19, A  ; Carregar de 0x0102

    ; TAC: MEM[B] = t23
    sts B, r19  ; Armazenar em 0x0104

; Linha 13
    ; TAC: t24 = MEM[B]
    lds r20, B  ; Carregar de 0x0104

    ; TAC: MEM[C] = t24
    sts C, r20  ; Armazenar em 0x0106

; Linha 14
    ; TAC: t25 = MEM[C]
    lds r21, C  ; Carregar de 0x0106

; Linha 15
; Linha 16
; Linha 17
; Linha 18
; Linha 19
; Linha 20
    ; TAC: ifFalse 1 goto L0
    ; AVISO: Instrução não mapeada: ifFalse 1 goto L0
    ; TAC: goto L1
    rjmp L1

L0:
L1:
; Linha 21
    ; TAC: MEM[N] = 1
    ; AVISO: Instrução não mapeada: MEM[N] = 1
; Linha 22
    ; TAC: t56 = MEM[N]
    lds r22, N  ; Carregar de 0x0108

    ; TAC: MEM[M] = t56
    sts M, r22  ; Armazenar em 0x010A

; Linha 23
    ; TAC: t57 = MEM[M]
    lds r23, M  ; Carregar de 0x010A

    ; TAC: MEM[K] = t57
    sts K, r23  ; Armazenar em 0x010C

; Linha 24
    ; TAC: t58 = MEM[K]
    lds r16, K  ; Carregar de 0x010C

; Linha 25
    ; TAC: MEM[PI] = 3.14
    ; AVISO: Instrução não mapeada: MEM[PI] = 3.14
; Linha 26
    ; TAC: t62 = MEM[PI]
    lds r17, PI  ; Carregar de 0x010E

; Linha 27
    ; TAC: t66 = RES[1]
    ; AVISO: Instrução não mapeada: t66 = RES[1]
; Linha 28
; Linha 29

fim:
    ; Loop infinito no final
    rjmp fim

