; lib_avr/math_inteiro.s
.section .text

; === DIV16S ===
; Redireciona para div16u (ignora sinal para suportar uint16 até 65535)
.global div16s
div16s:
    call div16u
    ret

; === PRINT_INT16 (Unsigned) ===
.global print_int16
print_int16:
    push r24
    push r25
    push r16
    
    ; Se for zero, imprime '0' direto
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

; Recursão para imprimir dígitos
p_rec:
    ; Verifica se num == 0
    mov r16, r24
    or r16, r25
    breq p_ret

    push r24
    push r25
    
    ldi r22, 10
    ldi r23, 0
    call div16u     ; R25:R24 = Quociente, R15:R14 = Resto
    
    push r14        ; Salva o resto (dígito atual) na pilha
    call p_rec      ; Chama recursão com o quociente
    pop r24         ; Recupera o resto da pilha para R24
    
    subi r24, -'0'  ; Converte para ASCII
    call uart_tx    ; Imprime
    
    pop r25
    pop r24
p_ret:
    ret