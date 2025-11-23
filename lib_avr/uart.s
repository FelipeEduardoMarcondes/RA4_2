; lib_avr/uart.s
; Funções de Comunicação Serial (9600 baud @ 16MHz)

.section .text

; === UART_INIT ===
.global uart_init
uart_init:
    push r16
    ; Baud Rate 9600 (UBRR = 103)
    ldi r16, 0
    sts 0xC5, r16 ; UBRR0H
    ldi r16, 103
    sts 0xC4, r16 ; UBRR0L
    ; Habilita TX
    ldi r16, (1<<3)
    sts 0xC1, r16 ; UCSR0B
    ; Formato 8N1
    ldi r16, (1<<1) | (1<<2)
    sts 0xC2, r16 ; UCSR0C
    pop r16
    ret

; === UART_TX ===
; Envia o byte em R24
.global uart_tx
uart_tx:
    push r16
tx_wait:
    lds r16, 0xC0 ; UCSR0A
    sbrs r16, 5   ; Check UDRE0
    rjmp tx_wait
    sts 0xC6, r24 ; UDR0
    pop r16
    ret

; === UART_NEWLINE ===
.global uart_newline
uart_newline:
    push r24
    ldi r24, 13 ; CR
    call uart_tx
    ldi r24, 10 ; LF
    call uart_tx
    pop r24
    ret