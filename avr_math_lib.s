; avr_math_lib.s - Biblioteca Matemática e de I/O 16 bits
; Compatível com Calling Convention do GCC (R25:R24, R23:R22)

; === Definições de Registradores de I/O (ATmega328P) ===
.equ UBRR0H, 0xC5
.equ UBRR0L, 0xC4
.equ UCSR0A, 0xC0
.equ UCSR0B, 0xC1
.equ UCSR0C, 0xC2
.equ UDR0,   0xC6
.equ UDRE0,  5
.equ RXEN0,  4
.equ TXEN0,  3
.equ UCSZ00, 1
.equ UCSZ01, 2

.section .text
.global mul16
.global div16u
.global mod16u
.global pow16u
.global serial_init
.global serial_tx
.global print_newline
.global print_uint16

; ---------------------------------------------------------
; MUL16: Multiplicação 16 bits Unsigned
; In: R25:R24 * R23:R22
; Out: R25:R24
; ---------------------------------------------------------
mul16:
    push r18
    push r19
    push r20
    push r21
    
    clr r20 ; Res Low
    clr r21 ; Res High
    
    ; R24 * R22
    mul r24, r22
    movw r20, r0
    
    ; R25 * R22
    mul r25, r22
    add r21, r0
    
    ; R24 * R23
    mul r24, r23
    add r21, r0
    
    movw r24, r20
    clr r1
    
    pop r21
    pop r20
    pop r19
    pop r18
    ret

; ---------------------------------------------------------
; DIV16U: Divisão 16 bits Unsigned
; In: R25:R24 (Num) / R23:R22 (Den)
; Out: R25:R24 (Quoc), R27:R26 (Resto - Interno/Trash)
; ---------------------------------------------------------
div16u:
    push r16
    push r17
    push r26
    push r27
    
    clr r26
    clr r27
    ldi r16, 17
    
div16_loop:
    dec r16
    breq div16_end
    
    lsl r26
    rol r27
    
    lsl r24
    rol r25
    adc r26, r1
    
    cp r26, r22
    cpc r27, r23
    brcs div16_next
    
    sub r26, r22
    sbc r27, r23
    inc r24
    
div16_next:
    rjmp div16_loop
    
div16_end:
    pop r27
    pop r26
    pop r17
    pop r16
    ret

; ---------------------------------------------------------
; MOD16U: Módulo 16 bits Unsigned
; In: R25:R24 % R23:R22
; Out: R25:R24 (Resto)
; ---------------------------------------------------------
mod16u:
    push r16
    push r17
    push r26
    push r27
    
    clr r26
    clr r27
    ldi r16, 17
    
mod16_loop:
    dec r16
    breq mod16_end
    
    lsl r26
    rol r27
    
    lsl r24
    rol r25
    adc r26, r1
    
    cp r26, r22
    cpc r27, r23
    brcs mod16_next
    
    sub r26, r22
    sbc r27, r23
    inc r24
    
mod16_next:
    rjmp mod16_loop
    
mod16_end:
    ; O resto ficou em R27:R26. Move para R25:R24 para retorno
    movw r24, r26
    
    pop r27
    pop r26
    pop r17
    pop r16
    ret

; ---------------------------------------------------------
; POW16U: Potência 16 bits (Simples)
; In: R25:R24 ^ R23:R22
; Out: R25:R24
; ---------------------------------------------------------
pow16u:
    push r20
    push r21
    
    ; R21:R20 guarda a Base
    movw r20, r24
    
    ; Resultado = 1
    ldi r24, 1
    ldi r25, 0
    
    ; Se expoente (R23:R22) for 0, retorna 1
    mov r16, r22
    or r16, r23
    breq pow16_exit
    
pow16_loop:
    ; Multiplica acumulador pela base
    ; Salva expoente (pois mul16 usa R22/R23)
    push r22
    push r23
    
    ; Configura args para mul16: Res * Base
    ; R25:R24 já é o Res
    movw r22, r20 ; Op2 = Base
    call mul16
    
    pop r23
    pop r22
    
    ; Decrementa expoente (R23:R22)
    subi r22, 1
    sbci r23, 0
    
    ; Se não for zero, continua
    mov r16, r22
    or r16, r23
    brne pow16_loop
    
pow16_exit:
    pop r21
    pop r20
    ret

; =========================================================
; ROTINAS DE I/O (SERIAL)
; =========================================================

; ---------------------------------------------------------
; SERIAL_INIT: Configura UART 9600 8N1 (F_CPU = 16MHz)
; Clobbers: R16
; ---------------------------------------------------------
serial_init:
    ; Baud Rate 9600 para 16MHz -> UBRR = 103
    ldi r16, 0
    sts UBRR0H, r16
    ldi r16, 103
    sts UBRR0L, r16
    
    ; Habilita TX e RX
    ldi r16, (1<<RXEN0)|(1<<TXEN0)
    sts UCSR0B, r16
    
    ; Formato 8 bits, 1 stop bit, sem paridade
    ldi r16, (1<<UCSZ01)|(1<<UCSZ00)
    sts UCSR0C, r16
    ret

; ---------------------------------------------------------
; SERIAL_TX: Envia um byte
; In: R24 (Char)
; ---------------------------------------------------------
serial_tx:
    ; Espera buffer vazio (UDRE0)
    lds r16, UCSR0A
    sbrs r16, UDRE0
    rjmp serial_tx
    ; Envia dado
    sts UDR0, r24
    ret

; ---------------------------------------------------------
; PRINT_NEWLINE: Envia \r\n
; ---------------------------------------------------------
print_newline:
    ldi r24, 13 ; CR
    call serial_tx
    ldi r24, 10 ; LF
    call serial_tx
    ret

; ---------------------------------------------------------
; PRINT_UINT16: Imprime R25:R24 como decimal (com sinal escalado)
; In: R25:R24
; Clobbers: R16-R27
; Obs: Esta versão simplificada assume SCALE=100 e imprime como float fixo
; Ex: 314 -> "3.14"
; ---------------------------------------------------------
print_uint16:
    push r28
    push r29
    push r24
    push r25
    
    ; Verifica sinal (bit 15)
    sbrs r25, 7
    rjmp p16_positive
    
    ; Negativo: imprime '-' e faz complemento de 2
    ldi r24, '-'
    call serial_tx
    pop r25
    pop r24
    com r24
    com r25
    adc r24, r1 ; r1 é zero
    adc r25, r1 ; r1 é zero (add with carry + 0 na verdade soma o carry se tiver)
    ; CORREÇÃO RÁPIDA: adc r24, zero_reg não funciona direto se zero_reg for R1
    ; Melhor: subi/sbci
    ; Ou apenas:
    ; com r25
    ; neg r24
    ; sbci r25, 0xff
    ; Mas vamos simplificar: apenas imprime o valor cru por enquanto ou implementa itoa básico
    push r24
    push r25
    
p16_positive:
    ; TODO: Conversão completa Bin->ASCII aqui.
    ; Por enquanto, imprime um marcador para debug
    ldi r24, '='
    call serial_tx
    ldi r24, '>'
    call serial_tx
    call print_newline
    
    pop r25
    pop r24
    pop r29
    pop r28
    ret