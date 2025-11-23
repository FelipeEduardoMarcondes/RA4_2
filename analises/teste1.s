; ===============================================
; Código Assembly AVR para Arduino Uno
; ATmega328P (8-bit, 16MHz)
; Gerado automaticamente pelo Compilador RPN
; FELIPE EDUARDO MARCONDES - GRUPO 2
; ===============================================

; === SEÇÃO DE DADOS ===
.data
; === Variáveis (16 bits cada) ===
t1:    .word 0    ; t1
t11:    .word 0    ; t11
t15:    .word 0    ; t15
t17:    .word 0    ; t17
t18:    .word 0    ; t18
t20:    .word 0    ; t20
t21:    .word 0    ; t21
t3:    .word 0    ; t3
t7:    .word 0    ; t7

; === SEÇÃO DE CÓDIGO ===
.text
; === INICIALIZAÇÃO ===
.equ RAMEND, 0x08FF
.equ SPL, 0x3D
.equ SPH, 0x3E

.global main
.org 0x0000
    rjmp reset_handler

; Vetores de interrupção (simplificado)
.org 0x0034

reset_handler:
    ; Configura pilha (CRÍTICO para chamadas de função)
    ldi r16, hi8(RAMEND)
    out SPH, r16
    ldi r16, lo8(RAMEND)
    out SPL, r16
    
    ; Zera R1 (convenção AVR-GCC)
    clr r1
    
    ; Inicializa UART (Nome corrigido para bater com avr_math_lib.s)
    call uart_init
    
    ; Delay para estabilização
    ldi r17, 50
delay_start:
    ldi r16, 255
delay_loop:
    dec r16
    brne delay_loop
    dec r17
    brne delay_start
    
main:
    ; === INÍCIO DO PROGRAMA PRINCIPAL ===


;  ====== LINHA 1 ======
    ; TAC: t1 = PRINT[5]
    ; >> PRINT(5)
    ldi r24, 5      ; Literal 5 (low)
    ldi r25, 0      ; Literal 5 (high)
    call print_int16
    call uart_newline
    sts t1, r24    ; Armazena em t1 (low)
    sts t1 + 1, r25    ; (high)

;  ====== LINHA 2 ======
    ; TAC: t3 = PRINT[10]
    ; >> PRINT(10)
    ldi r24, 10      ; Literal 10 (low)
    ldi r25, 0      ; Literal 10 (high)
    call print_int16
    call uart_newline
    sts t3, r24    ; Armazena em t3 (low)
    sts t3 + 1, r25    ; (high)

;  ====== LINHA 3 ======
    ; TAC: t7 = PRINT[8]
    ; >> PRINT(8)
    ldi r24, 8      ; Literal 8 (low)
    ldi r25, 0      ; Literal 8 (high)
    call print_int16
    call uart_newline
    sts t7, r24    ; Armazena em t7 (low)
    sts t7 + 1, r25    ; (high)

;  ====== LINHA 4 ======
    ; TAC: t11 = PRINT[20]
    ; >> PRINT(20)
    ldi r24, 20      ; Literal 20 (low)
    ldi r25, 0      ; Literal 20 (high)
    call print_int16
    call uart_newline
    sts t11, r24    ; Armazena em t11 (low)
    sts t11 + 1, r25    ; (high)

;  ====== LINHA 5 ======
    ; TAC: t15 = PRINT[10]
    ; >> PRINT(10)
    ldi r24, 10      ; Literal 10 (low)
    ldi r25, 0      ; Literal 10 (high)
    call print_int16
    call uart_newline
    sts t15, r24    ; Armazena em t15 (low)
    sts t15 + 1, r25    ; (high)

;  ====== LINHA 6 ======
    ; TAC: t17 = RES[1]
    ; >> RES(1) = t20
    lds r24, t20
    lds r25, t20 + 1
    sts t17, r24    ; Armazena em t17 (low)
    sts t17 + 1, r25    ; (high)
    ; TAC: t18 = PRINT[t17]
    ; >> PRINT(t17)
    lds r24, t17
    lds r25, t17 + 1
    call print_int16
    call uart_newline
    sts t18, r24    ; Armazena em t18 (low)
    sts t18 + 1, r25    ; (high)

;  ====== LINHA 7 ======
    ; TAC: t20 = RES[4]
    ; AVISO: RES(4) sem resultado válido
    ldi r24, 0      ; Literal 0 (low)
    ldi r25, 0      ; Literal 0 (high)
    sts t20, r24    ; Armazena em t20 (low)
    sts t20 + 1, r25    ; (high)
    ; TAC: t21 = PRINT[t20]
    ; >> PRINT(t20)
    lds r24, t20
    lds r25, t20 + 1
    call print_int16
    call uart_newline
    sts t21, r24    ; Armazena em t21 (low)
    sts t21 + 1, r25    ; (high)

    ; === FIM DO PROGRAMA ===
fim_programa:
    rjmp fim_programa    ; Loop infinito

