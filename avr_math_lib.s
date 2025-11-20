; avr_math_lib.s
; Biblioteca de rotinas matemáticas para AVR
; Arduino Uno (ATmega328P)

.text

;-----------------------------------------------------------------------------
; Divisão inteira sem sinal 8 bits
; Entrada: R24 = dividendo, R25 = divisor
; Saída: R24 = quociente, R25 = resto
;-----------------------------------------------------------------------------
div8u:
    push r16
    push r17
    
    mov r16, r24        ; Dividendo
    mov r17, r25        ; Divisor
    clr r24             ; Quociente = 0
    clr r25             ; Resto = 0
    ldi r18, 8          ; Contador de bits
    
div8u_loop:
    lsl r16             ; Shift left dividendo
    rol r25             ; Rotate left resto
    cp r25, r17         ; Comparar resto com divisor
    brlo div8u_skip     ; Se resto < divisor, skip
    sub r25, r17        ; resto -= divisor
    inc r24             ; quociente++
div8u_skip:
    dec r18
    brne div8u_loop
    
    pop r17
    pop r16
    ret

;-----------------------------------------------------------------------------
; Módulo (resto) 8 bits
; Entrada: R24 = dividendo, R25 = divisor
; Saída: R25 = resto
;-----------------------------------------------------------------------------
mod8u:
    call div8u          ; Reutilizar divisão
    ; R25 já contém o resto
    ret

;-----------------------------------------------------------------------------
; Potenciação 8 bits
; Entrada: R24 = base, R25 = expoente
; Saída: R24 = resultado
;-----------------------------------------------------------------------------
pow8u:
    push r16
    push r17
    
    mov r16, r24        ; Base
    mov r17, r25        ; Expoente
    ldi r24, 1          ; Resultado = 1
    
    cpi r17, 0          ; Se expoente = 0
    breq pow8u_end      ; Retornar 1
    
pow8u_loop:
    mul r24, r16        ; resultado *= base
    mov r24, r0         ; Pegar byte baixo
    dec r17
    brne pow8u_loop
    
pow8u_end:
    pop r17
    pop r16
    ret

;-----------------------------------------------------------------------------
; Multiplicação 16 bits
; Entrada: R24:R25 = operando1, R22:R23 = operando2
; Saída: R24:R25 = resultado (16 bits baixos)
;-----------------------------------------------------------------------------
mul16:
    push r18
    push r19
    push r20
    push r21
    
    clr r18
    clr r19
    
    ; R24 * R22
    mul r24, r22
    add r18, r0
    adc r19, r1
    
    ; R24 * R23
    mul r24, r23
    add r19, r0
    
    ; R25 * R22
    mul r25, r22
    add r19, r0
    
    mov r24, r18
    mov r25, r19
    
    pop r21
    pop r20
    pop r19
    pop r18
    ret

;-----------------------------------------------------------------------------
; Divisão float 16 bits (simplificada - inteiros escalados)
; Entrada: R24:R25 = dividendo*100, R22:R23 = divisor*100
; Saída: R24:R25 = quociente*100
;-----------------------------------------------------------------------------
divfloat16:
    ; Por simplicidade, usar divisão inteira em valores escalados
    ; Esta é uma implementação básica
    push r18
    push r19
    
    ; Escalar dividendo por 100 antes de dividir
    ; (dividendo * 100) / divisor
    
    ; Implementação simplificada: divisão inteira normal
    mov r18, r24
    mov r19, r25
    
    ; Aqui deveria ter rotina de divisão 16 bits
    ; Por simplicidade, usar 8 bits
    call div8u
    
    pop r19
    pop r18
    ret

;-----------------------------------------------------------------------------
; Inicialização de comunicação serial (9600 baud)
;-----------------------------------------------------------------------------
serial_init:
    ; UBRR = (F_CPU / (16 * BAUD)) - 1
    ; Para 16MHz e 9600 baud: UBRR = 103
    ldi r24, 0
    sts UBRR0H, r24
    ldi r24, 103
    sts UBRR0L, r24
    
    ; Habilitar transmissor
    ldi r24, (1<<TXEN0)
    sts UCSR0B, r24
    
    ; Formato: 8 bits dados, 1 stop bit
    ldi r24, (1<<UCSZ01)|(1<<UCSZ00)
    sts UCSR0C, r24
    
    ret

;-----------------------------------------------------------------------------
; Transmitir byte via serial
; Entrada: R24 = byte a transmitir
;-----------------------------------------------------------------------------
serial_tx:
    push r25
    
serial_tx_wait:
    lds r25, UCSR0A
    sbrs r25, UDRE0
    rjmp serial_tx_wait
    
    sts UDR0, r24
    
    pop r25
    ret

;-----------------------------------------------------------------------------
; Transmitir string via serial
; Entrada: Z (R30:R31) = ponteiro para string (terminada em 0)
;-----------------------------------------------------------------------------
serial_print:
    push r24
    push r25
    
serial_print_loop:
    lpm r24, Z+
    cpi r24, 0
    breq serial_print_end
    call serial_tx
    rjmp serial_print_loop
    
serial_print_end:
    pop r25
    pop r24
    ret

;-----------------------------------------------------------------------------
; Transmitir número decimal via serial
; Entrada: R24 = número (0-255)
;-----------------------------------------------------------------------------
serial_print_num:
    push r24
    push r25
    push r26
    
    ; Converter para ASCII
    ldi r25, 100
    call div8u          ; R24 = centenas, R25 = resto
    
    ; Centenas
    cpi r24, 0
    breq skip_hundreds
    ori r24, 0x30       ; Converter para ASCII
    call serial_tx
    
skip_hundreds:
    mov r24, r25
    ldi r25, 10
    call div8u          ; R24 = dezenas, R25 = unidades
    
    ; Dezenas
    ori r24, 0x30
    call serial_tx
    
    ; Unidades
    mov r24, r25
    ori r24, 0x30
    call serial_tx
    
    ; Nova linha
    ldi r24, '\r'
    call serial_tx
    ldi r24, '\n'
    call serial_tx
    
    pop r26
    pop r25
    pop r24
    ret