; lib_avr/math_inteiro.s
; Biblioteca Alternativa para Inteiros Grandes (Unsigned)
; Substitui math_signed.s para os testes de Fibonacci/Fatorial

.section .text

; === DIV16S (Mantido apenas para compatibilidade de linkagem) ===
; Mas implementado como DIV16U (Unsigned)
.global div16s
div16s:
    call div16u
    ret

; === PRINT_INT16 (Versão Unsigned 0-65535) ===
; Ignora sinal para permitir imprimir até 65535 (ex: Fibo 24 = 46368)
.global print_int16
print_int16:
    push r24
    push r25
    push r16
    
    ; Caso especial: se for 0
    mov r16, r24
    or r16, r25
    brne p_start
    ldi r24, '0'
    call uart_tx
    rjmp p_end

p_start:
    call p_rec

p_end:
    pop r16
    pop r25
    pop r24
    ret

; Função recursiva de impressão
p_rec:
    mov r16, r24
    or r16, r25
    breq p_ret

    push r24
    push r25
    
    ldi r22, 10
    ldi r23, 0
    call div16u     ; Divisão SEM sinal
    
    push r14        ; Salva resto
    call p_rec      ; Recursão
    pop r24         ; Recupera resto
    
    subi r24, -'0'
    call uart_tx
    
    pop r25
    pop r24
p_ret:
    ret