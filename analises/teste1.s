; Seção de Dados
.data
t1: .byte 2
t11: .byte 2
t15: .byte 2
t17: .byte 2
t18: .byte 2
t20: .byte 2
t21: .byte 2
t3: .byte 2
t7: .byte 2

; Seção de Código
.text
; Definições de Hardware (ATmega328P)
.equ RAMEND, 0x08FF
.equ SPL, 0x3D
.equ SPH, 0x3E

.global main
.org 0x0000
    rjmp main

main:
    ; Inicializar pilha
    ldi r16, hi8(RAMEND)
    out SPH, r16
    ldi r16, lo8(RAMEND)
    out SPL, r16
    clr r1
    ; Inicializar Serial (9600 baud)
    call serial_init

;  Linha 1
    ; TAC: t1 = PRINT[5]
    lds r24, PRINT[5]
    lds r25, PRINT[5] + 1
    sts t1, r24
    sts t1 + 1, r25
;  Linha 2
    ; TAC: t3 = PRINT[10]
    lds r24, PRINT[10]
    lds r25, PRINT[10] + 1
    sts t3, r24
    sts t3 + 1, r25
;  Linha 3
    ; TAC: t7 = PRINT[8]
    lds r24, PRINT[8]
    lds r25, PRINT[8] + 1
    sts t7, r24
    sts t7 + 1, r25
;  Linha 4
    ; TAC: t11 = PRINT[20]
    lds r24, PRINT[20]
    lds r25, PRINT[20] + 1
    sts t11, r24
    sts t11 + 1, r25
;  Linha 5
    ; TAC: t15 = PRINT[10]
    lds r24, PRINT[10]
    lds r25, PRINT[10] + 1
    sts t15, r24
    sts t15 + 1, r25
;  Linha 6
    ; TAC: t17 = RES[1]
    ldi r24, 1
    ldi r25, 0
    ; Recupera resultado da linha 5 (t21)
    lds r24, t21
    lds r25, t21 + 1
    call print_int16
    sts t17, r24
    sts t17 + 1, r25
    ; TAC: t18 = PRINT[t17]
    lds r24, PRINT[t17]
    lds r25, PRINT[t17] + 1
    sts t18, r24
    sts t18 + 1, r25
;  Linha 7
    ; TAC: t20 = RES[4]
    ldi r24, 4
    ldi r25, 0
    ; Recupera resultado da linha 3 (t11)
    lds r24, t11
    lds r25, t11 + 1
    call print_int16
    sts t20, r24
    sts t20 + 1, r25
    ; TAC: t21 = PRINT[t20]
    lds r24, PRINT[t20]
    lds r25, PRINT[t20] + 1
    sts t21, r24
    sts t21 + 1, r25
fim_programa:
    rjmp fim_programa
