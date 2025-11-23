; avr_math_lib.s - Biblioteca Matemática e de I/O 16 bits (VERSÃO CORRIGIDA)
; FELIPE EDUARDO MARCONDES - GRUPO 2

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
.global print_int16
.global print_string

; ---------------------------------------------------------
; SERIAL_INIT: Configura UART 9600 8N1 (F_CPU = 16MHz)
; ---------------------------------------------------------
serial_init:
    ; Desabilita interrupções durante configuração
    cli
    
    ; Configura baud rate: UBRR = (F_CPU / (16 * BAUD)) - 1
    ; Para 9600: UBRR = (16000000 / (16 * 9600)) - 1 = 103
    ldi r16, 0
    sts UBRR0H, r16
    ldi r16, 103
    sts UBRR0L, r16
    
    ; Habilita transmissor e receptor
    ldi r16, (1<<RXEN0)|(1<<TXEN0)
    sts UCSR0B, r16
    
    ; Configura 8 bits de dados, sem paridade, 1 stop bit
    ldi r16, (1<<UCSZ01)|(1<<UCSZ00)
    sts UCSR0C, r16
    
    ; Reabilita interrupções
    sei
    
    ; Pequeno delay para estabilização (≈65ms)
    ldi r17, 255
init_delay_outer:
    ldi r16, 255
init_delay_inner:
    dec r16
    brne init_delay_inner
    dec r17
    brne init_delay_outer
    
    ret

; ---------------------------------------------------------
; SERIAL_TX: Envia um byte pela serial
; In: R24 (byte a enviar)
; Preserva: Todos os registradores exceto R16
; ---------------------------------------------------------
serial_tx:
    push r16
serial_tx_wait:
    lds r16, UCSR0A
    sbrs r16, UDRE0      ; Espera buffer vazio
    rjmp serial_tx_wait
    sts UDR0, r24        ; Envia byte
    pop r16
    ret

; ---------------------------------------------------------
; PRINT_NEWLINE: Envia CR+LF (\r\n)
; ---------------------------------------------------------
print_newline:
    push r24
    ldi r24, 13          ; CR
    call serial_tx
    ldi r24, 10          ; LF
    call serial_tx
    pop r24
    ret

; ---------------------------------------------------------
; PRINT_STRING: Imprime string terminada em NULL da memória de programa
; In: Z (R31:R30) = ponteiro para string na flash
; ---------------------------------------------------------
print_string:
    push r24
    push r30
    push r31
print_string_loop:
    lpm r24, Z+          ; Carrega byte da flash
    tst r24              ; Verifica NULL
    breq print_string_end
    call serial_tx
    rjmp print_string_loop
print_string_end:
    pop r31
    pop r30
    pop r24
    ret

; ---------------------------------------------------------
; PRINT_INT16: Imprime R25:R24 como decimal signed (SIMPLIFICADO)
; In: R25:R24 (número de 16 bits com sinal)
; Usa: Buffer na pilha, registradores R16-R23
; ---------------------------------------------------------
print_int16:
    push r16
    push r17
    push r18
    push r19
    push r20
    push r21
    push r22
    push r23
    
    ; Salva valor original
    movw r22, r24
    
    ; Verifica sinal (bit 15 de R25)
    sbrs r25, 7
    rjmp print_int16_positive
    
    ; Número negativo: imprime '-'
    push r24
    ldi r24, '-'
    call serial_tx
    pop r24
    
    ; Faz complemento de 2 (negação)
    com r24
    com r25
    subi r24, 0xFF       ; Adiciona 1 (low byte)
    sbci r25, 0xFF       ; Carry para high byte
    
print_int16_positive:
    ; Agora R25:R24 contém valor absoluto
    
    ; Inicializa pilha de dígitos
    ldi r18, 0           ; Contador de dígitos
    
    ; Caso especial: zero
    mov r16, r24
    or r16, r25
    brne print_int16_convert
    
    ; Imprime "0"
    ldi r24, '0'
    call serial_tx
    rjmp print_int16_done
    
print_int16_convert:
    ; Loop de divisão por 10
    ; R25:R24 = número atual
    ; R21:R20 = quociente
    ; R19 = resto
    
print_int16_div_loop:
    ; Divide R25:R24 por 10
    ; Usa divisão simplificada
    
    ; Salva dividendo
    push r24
    push r25
    
    ; Divisor = 10
    ldi r22, 10
    ldi r23, 0
    
    ; Chama função de divisão
    call div16u
    ; Resultado (quociente) fica em R25:R24
    
    ; Multiplica quociente por 10 para calcular resto
    movw r20, r24        ; Salva quociente
    ldi r22, 10
    ldi r23, 0
    call mul16
    ; R25:R24 = quociente * 10
    
    ; Calcula resto = dividendo - (quociente * 10)
    pop r17              ; High byte original
    pop r16              ; Low byte original
    sub r16, r24
    sbc r17, r25
    ; R16 agora contém o resto (0-9)
    
    ; Converte resto para ASCII e salva na pilha
    subi r16, -'0'
    push r16
    inc r18              ; Incrementa contador
    
    ; Restaura quociente
    movw r24, r20
    
    ; Se quociente != 0, continua dividindo
    mov r16, r24
    or r16, r25
    brne print_int16_div_loop
    
print_int16_print_digits:
    ; Imprime dígitos da pilha (ordem reversa)
    pop r24
    call serial_tx
    dec r18
    brne print_int16_print_digits
    
print_int16_done:
    pop r23
    pop r22
    pop r21
    pop r20
    pop r19
    pop r18
    pop r17
    pop r16
    ret

; ---------------------------------------------------------
; MUL16: Multiplicação 16 bits Unsigned
; In: R25:R24 * R23:R22
; Out: R25:R24 (resultado, apenas 16 bits inferiores)
; ---------------------------------------------------------
mul16:
    push r18
    push r19
    push r20
    push r21
    
    clr r20
    clr r21
    
    ; R24 (low A) * R22 (low B)
    mul r24, r22
    movw r20, r0
    
    ; R25 (high A) * R22 (low B)
    mul r25, r22
    add r21, r0
    
    ; R24 (low A) * R23 (high B)
    mul r24, r23
    add r21, r0
    
    movw r24, r20
    clr r1               ; Restaura R1 = 0
    
    pop r21
    pop r20
    pop r19
    pop r18
    ret

; ---------------------------------------------------------
; DIV16U: Divisão 16 bits Unsigned
; In: R25:R24 (Numerador) / R23:R22 (Denominador)
; Out: R25:R24 (Quociente)
; ---------------------------------------------------------
div16u:
    push r16
    push r17
    push r26
    push r27
    
    ; Verifica divisão por zero
    mov r16, r22
    or r16, r23
    brne div16u_start
    
    ; Divisão por zero: retorna 0
    clr r24
    clr r25
    rjmp div16u_exit
    
div16u_start:
    clr r26              ; Acumulador (resto)
    clr r27
    ldi r16, 17          ; Contador (16 bits + 1)
    
div16u_loop:
    dec r16
    breq div16u_end
    
    ; Desloca resto para esquerda
    lsl r26
    rol r27
    
    ; Desloca quociente para esquerda e traz bit do numerador
    lsl r24
    rol r25
    adc r26, r1          ; Adiciona carry ao resto
    
    ; Compara resto com denominador
    cp r26, r22
    cpc r27, r23
    brcs div16u_next     ; Se resto < denominador, pula
    
    ; resto >= denominador: subtrai e seta bit do quociente
    sub r26, r22
    sbc r27, r23
    inc r24              ; Seta bit menos significativo do quociente
    
div16u_next:
    rjmp div16u_loop
    
div16u_end:
div16u_exit:
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
    
    ; Verifica divisão por zero
    mov r16, r22
    or r16, r23
    brne mod16u_start
    
    ; Módulo por zero: retorna 0
    clr r24
    clr r25
    rjmp mod16u_exit
    
mod16u_start:
    clr r26
    clr r27
    ldi r16, 17
    
mod16u_loop:
    dec r16
    breq mod16u_end
    
    lsl r26
    rol r27
    
    lsl r24
    rol r25
    adc r26, r1
    
    cp r26, r22
    cpc r27, r23
    brcs mod16u_next
    
    sub r26, r22
    sbc r27, r23
    inc r24
    
mod16u_next:
    rjmp mod16u_loop
    
mod16u_end:
    movw r24, r26        ; Retorna o resto
    
mod16u_exit:
    pop r27
    pop r26
    pop r17
    pop r16
    ret

; ---------------------------------------------------------
; POW16U: Potência 16 bits (base ^ expoente)
; In: R25:R24 (base) ^ R23:R22 (expoente)
; Out: R25:R24 (resultado)
; ---------------------------------------------------------
pow16u:
    push r20
    push r21
    push r22
    push r23
    
    ; Verifica expoente = 0
    mov r16, r22
    or r16, r23
    brne pow16u_start
    
    ; Qualquer número elevado a 0 = 1
    ldi r24, 1
    ldi r25, 0
    rjmp pow16u_exit
    
pow16u_start:
    movw r20, r24        ; Salva base em R21:R20
    
    ldi r24, 1           ; Resultado inicial = 1
    ldi r25, 0
    
pow16u_loop:
    ; Multiplica resultado pela base
    push r22
    push r23
    
    movw r22, r20        ; R23:R22 = base
    call mul16           ; R25:R24 *= base
    
    pop r23
    pop r22
    
    ; Decrementa expoente
    subi r22, 1
    sbci r23, 0
    
    ; Verifica se expoente chegou a zero
    mov r16, r22
    or r16, r23
    brne pow16u_loop
    
pow16u_exit:
    pop r23
    pop r22
    pop r21
    pop r20
    ret