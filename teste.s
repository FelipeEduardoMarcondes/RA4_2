; teste_manual.s
; Teste isolado da biblioteca matemática e serial

.equ RAMEND, 0x08FF
.equ SPL, 0x3D
.equ SPH, 0x3E

.global main

.text
main:
    ; 1. Configurar a Pilha (OBRIGATÓRIO no Arduino)
    ldi r16, hi8(RAMEND)
    out SPH, r16
    ldi r16, lo8(RAMEND)
    out SPL, r16

    ; 2. Inicializar Serial
    call uart_init

    ; 3. Testar envio de caractere simples 'A'
    ldi r24, 65      ; ASCII 'A'
    call uart_tx
    call uart_newline

    ; 4. Testar impressão de número (1234)
    ; 1234 em hex é 0x04D2
    ldi r24, 0xD2    ; Low byte
    ldi r25, 0x04    ; High byte
    call print_int16
    call uart_newline

    ; 5. Testar número negativo (-1234)
    ; -1234 em complemento de 2 (16 bits)
    ldi r24, 0x2E
    ldi r25, 0xFB
    call print_int16
    call uart_newline

fim:
    rjmp fim