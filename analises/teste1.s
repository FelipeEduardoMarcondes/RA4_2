; Seção de Dados
.data
A: .byte 2
B: .byte 2
C: .byte 2
MAX: .byte 2
N: .byte 2
t10: .byte 2
t11: .byte 2
t12: .byte 2
t13: .byte 2
t14: .byte 2
t15: .byte 2
t16: .byte 2
t18: .byte 2
t19: .byte 2
t22: .byte 2
t24: .byte 2
t3: .byte 2
t4: .byte 2
t5: .byte 2
t6: .byte 2
t9: .byte 2

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
    ; TAC: MEM[A] = 0
    ldi r24, 0
    ldi r25, 0
    sts A, r24
    sts A + 1, r25
;  Linha 2
    ; TAC: MEM[B] = 1
    ldi r24, 100
    ldi r25, 0
    sts B, r24
    sts B + 1, r25
;  Linha 3
    ; TAC: MEM[N] = 2
    ldi r24, 200
    ldi r25, 0
    sts N, r24
    sts N + 1, r25
;  Linha 4
    ; TAC: t3 = MEM[A]
    lds r24, A
    lds r25, A + 1
    sts t3, r24
    sts t3 + 1, r25
    ; TAC: t4 = RES[t3]
    lds r24, t3
    lds r25, t3 + 1
    call print_uint16
    sts t4, r24
    sts t4 + 1, r25
;  Linha 5
    ; TAC: t5 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t5, r24
    sts t5 + 1, r25
    ; TAC: t6 = RES[t5]
    lds r24, t5
    lds r25, t5 + 1
    call print_uint16
    sts t6, r24
    sts t6 + 1, r25
;  Linha 6
    ; TAC: MEM[MAX] = 24
    ldi r24, 96
    ldi r25, 9
    sts MAX, r24
    sts MAX + 1, r25
;  Linha 7
    ; TAC: L0:
L0:
    ; TAC: t9 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t9, r24
    sts t9 + 1, r25
    ; TAC: t10 = MEM[MAX]
    lds r24, MAX
    lds r25, MAX + 1
    sts t10, r24
    sts t10 + 1, r25
    ; TAC: t11 = t9 < t10
    lds r24, t9
    lds r25, t9 + 1
    lds r22, t10
    lds r23, t10 + 1
    cp r24, r22
    cpc r25, r23
    brge L_SKIP_85
    rjmp L_TRUE_85
L_SKIP_85:
    ldi r24, 0
    ldi r25, 0
    rjmp L_END_85
L_TRUE_85:
    ldi r24, 1
    ldi r25, 0
L_END_85:
    sts t11, r24
    sts t11 + 1, r25
    ; TAC: ifFalse t11 goto L1
    lds r24, t11
    lds r25, t11 + 1
    or r24, r25
    brne L_NO_JUMP_103
    rjmp L1
L_NO_JUMP_103:
    ; TAC: t12 = MEM[A]
    lds r24, A
    lds r25, A + 1
    sts t12, r24
    sts t12 + 1, r25
    ; TAC: t13 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t13, r24
    sts t13 + 1, r25
    ; TAC: t14 = t12 + t13
    lds r24, t12
    lds r25, t12 + 1
    lds r22, t13
    lds r23, t13 + 1
    add r24, r22
    adc r25, r23
    sts t14, r24
    sts t14 + 1, r25
    ; TAC: MEM[C] = t14
    lds r24, t14
    lds r25, t14 + 1
    sts C, r24
    sts C + 1, r25
    ; TAC: t15 = MEM[C]
    lds r24, C
    lds r25, C + 1
    sts t15, r24
    sts t15 + 1, r25
    ; TAC: t16 = RES[t15]
    lds r24, t15
    lds r25, t15 + 1
    call print_uint16
    sts t16, r24
    sts t16 + 1, r25
    ; TAC: t18 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t18, r24
    sts t18 + 1, r25
    ; TAC: MEM[A] = t18
    lds r24, t18
    lds r25, t18 + 1
    sts A, r24
    sts A + 1, r25
    ; TAC: t19 = MEM[C]
    lds r24, C
    lds r25, C + 1
    sts t19, r24
    sts t19 + 1, r25
    ; TAC: MEM[B] = t19
    lds r24, t19
    lds r25, t19 + 1
    sts B, r24
    sts B + 1, r25
    ; TAC: t22 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t22, r24
    sts t22 + 1, r25
    ; TAC: t24 = t22 + 1
    lds r24, t22
    lds r25, t22 + 1
    ldi r22, 100
    ldi r23, 0
    add r24, r22
    adc r25, r23
    sts t24, r24
    sts t24 + 1, r25
    ; TAC: MEM[N] = t24
    lds r24, t24
    lds r25, t24 + 1
    sts N, r24
    sts N + 1, r25
    ; TAC: goto L0
    rjmp L0
    ; TAC: L1:
L1:
fim_programa:
    rjmp fim_programa
