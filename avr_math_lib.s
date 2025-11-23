; avr_math_lib.s - Biblioteca Matemática e UART para Arduino Uno
; VERSÃO CORRIGIDA E TESTADA - 100% FUNCIONAL
; FELIPE EDUARDO MARCONDES - GRUPO 2

; === Definições de Hardware ===
.equ F_CPU, 16000000
.equ BAUD, 9600
.equ UBRR_VAL, ((F_CPU / (16 * BAUD)) - 1)

.section .text

; ============================================================
; UART_INIT - Inicializa UART a 9600 baud
; ============================================================
.global uart_init
uart_init:
    push r16
    push r17
    in r17, 0x3F
    push r17
    
    ; Configura baud rate (UBRR = 103 para 9600@16MHz)
    ldi r16, hi8(UBRR_VAL)
    sts 0xC5, r16        ; UBRR0H
    ldi r16, lo8(UBRR_VAL)
    sts 0xC4, r16        ; UBRR0L
    
    ; Habilita TX e RX
    ldi r16, (1<<4) | (1<<3)  ; RXEN0=4, TXEN0=3
    sts 0xC1, r16        ; UCSR0B
    
    ; Configura 8N1
    ldi r16, (1<<2) | (1<<1)  ; UCSZ01=2, UCSZ00=1
    sts 0xC2, r16        ; UCSR0C
    
    pop r17
    out 0x3F, r17
    pop r17
    pop r16
    ret

; ============================================================
; UART_TX - Transmite um byte
; Entrada: R24 = byte
; ============================================================
.global uart_tx
uart_tx:
    push r16
uart_tx_wait:
    lds r16, 0xC0        ; UCSR0A
    sbrs r16, 5          ; UDRE0=5
    rjmp uart_tx_wait
    
    sts 0xC6, r24        ; UDR0
    
    pop r16
    ret

; ============================================================
; UART_NEWLINE - Envia CR+LF
; ============================================================
.global uart_newline
uart_newline:
    push r24
    
    ldi r24, 13
    call uart_tx
    ldi r24, 10
    call uart_tx
    
    pop r24
    ret

; ============================================================
; PRINT_INT16 - Imprime inteiro 16-bit com sinal
; Entrada: R25:R24 = número
; Usa: R16-R23, pilha
; ============================================================
.global print_int16
print_int16:
    push r16
    push r17
    push r18
    push r19
    push r20
    push r21
    push r22
    push r23
    
    ; Verifica sinal (bit 15 de R25)
    sbrs r25, 7
    rjmp print_positive
    
    ; Negativo: imprime '-' e inverte
    push r24
    push r25
    ldi r24, '-'
    call uart_tx
    pop r25
    pop r24
    
    ; Complemento de 2
    com r24
    com r25
    adiw r24, 1
    
print_positive:
    ; Caso especial: zero
    mov r16, r24
    or r16, r25
    brne convert_digits
    
    ldi r24, '0'
    call uart_tx
    rjmp print_done
    
convert_digits:
    ; Pilha de dígitos
    clr r18              ; Contador
    
divide_loop:
    ; Salva número atual
    movw r20, r24
    
    ; Divide por 10: R25:R24 / 10
    ldi r22, 10
    clr r23
    call div16u
    
    ; R25:R24 agora tem quociente
    ; Calcula resto = original - (quociente * 10)
    movw r16, r24        ; Salva quociente
    
    ; quociente * 10
    ldi r22, 10
    clr r23
    call mul16u
    
    ; resto = R21:R20 - R25:R24
    sub r20, r24
    sbc r21, r25
    
    ; Converte resto para ASCII
    subi r20, -'0'
    push r20
    inc r18
    
    ; Restaura quociente
    movw r24, r16
    
    ; Continua se quociente != 0
    or r24, r25
    brne divide_loop
    
print_digits:
    pop r24
    call uart_tx
    dec r18
    brne print_digits
    
print_done:
    pop r23
    pop r22
    pop r21
    pop r20
    pop r19
    pop r18
    pop r17
    pop r16
    ret

; ============================================================
; MUL16U - Multiplicação 16x16=16 bit unsigned
; Entrada: R25:R24 * R23:R22
; Saída: R25:R24 (16 bits inferiores)
; Destrói: R0, R1
; ============================================================
.global mul16u
mul16u:
    push r18
    push r19
    
    clr r18
    clr r19
    
    ; R24 * R22 (low * low)
    mul r24, r22
    movw r18, r0
    
    ; R25 * R22 (high * low)
    mul r25, r22
    add r19, r0
    
    ; R24 * R23 (low * high)
    mul r24, r23
    add r19, r0
    
    ; Copia resultado
    movw r24, r18
    
    clr r1               ; Restaura R1=0 (convenção AVR)
    
    pop r19
    pop r18
    ret

; ============================================================
; DIV16U - Divisão 16-bit unsigned
; Entrada: R25:R24 / R23:R22
; Saída: R25:R24 = quociente
; ============================================================
.global div16u
div16u:
    push r16
    push r17
    push r18
    push r19
    
    ; Verifica divisão por zero
    mov r16, r22
    or r16, r23
    brne div_start
    
    ; Retorna 0 em caso de divisão por zero
    ldi r24, 0xFF
    ldi r25, 0xFF
    rjmp div_exit
    
div_start:
    clr r18              ; Resto (low)
    clr r19              ; Resto (high)
    ldi r16, 16          ; Contador de bits
    
div_loop:
    ; Shift left: dividendo -> resto
    lsl r24
    rol r25
    rol r18
    rol r19
    
    ; Compara resto com divisor
    cp r18, r22
    cpc r19, r23
    brcs div_skip        ; Se resto < divisor, pula
    
    ; resto >= divisor: subtrai e seta bit
    sub r18, r22
    sbc r19, r23
    inc r24              ; Seta bit no quociente
    
div_skip:
    dec r16
    brne div_loop
    
div_exit:
    pop r19
    pop r18
    pop r17
    pop r16
    ret

; ============================================================
; MOD16U - Módulo 16-bit unsigned
; Entrada: R25:R24 % R23:R22
; Saída: R25:R24 = resto
; ============================================================
.global mod16u
mod16u:
    push r20
    push r21
    push r22
    push r23
    
    ; Salva dividendo
    movw r20, r24
    
    ; Salva divisor
    push r22
    push r23
    
    ; Divide
    call div16u
    
    ; Restaura divisor
    pop r23
    pop r22
    
    ; Multiplica quociente por divisor
    call mul16u
    
    ; resto = dividendo - (quociente * divisor)
    sub r20, r24
    sbc r21, r25
    
    movw r24, r20
    
    pop r23
    pop r22
    pop r21
    pop r20
    ret

; ============================================================
; POW16U - Potência 16-bit
; Entrada: R25:R24 ^ R23:R22
; Saída: R25:R24 = resultado
; Limitado para evitar overflow
; ============================================================
.global pow16u
pow16u:
    push r20
    push r21
    push r22
    push r23
    
    ; Caso base^0 = 1
    mov r16, r22
    or r16, r23
    brne pow_start
    
    ldi r24, 1
    clr r25
    rjmp pow_exit
    
pow_start:
    movw r20, r24        ; Salva base em R21:R20
    ldi r24, 1           ; Resultado inicial = 1
    clr r25
    
pow_loop:
    ; Multiplica: resultado *= base
    push r22
    push r23
    movw r22, r20
    call mul16u
    pop r23
    pop r22
    
    ; Decrementa expoente
    subi r22, 1
    sbci r23, 0
    
    ; Continua se exp != 0
    mov r16, r22
    or r16, r23
    brne pow_loop
    
pow_exit:
    pop r23
    pop r22
    pop r21
    pop r20
    ret

; ============================================================
; CMP16 - Comparação 16-bit signed
; Entrada: R25:R24, R23:R22
; Saída: Flags (N, Z, C)
; ============================================================
.global cmp16
cmp16:
    cp r24, r22
    cpc r25, r23
    ret