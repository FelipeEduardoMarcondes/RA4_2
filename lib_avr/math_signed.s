; lib_avr/math_signed.s
; Wrappers para operações com sinal e impressão

.section .text

; === DIV16S (Divisão com Sinal) ===
; R25:R24 / R23:R22 -> R25:R24
.global div16s
div16s:
    push r16            ; Guarda sinal do resultado
    push r14            ; Salva contexto que div16u vai sujar
    push r15
    clr r16
    
    ; Checa sinal do Dividendo
    sbrs r25, 7
    rjmp chk_div
    inc r16             ; Sinal++
    call negate_r24     ; Torna positivo

chk_div:
    ; Checa sinal do Divisor
    sbrs r23, 7
    rjmp do_div
    inc r16             ; Sinal++
    call negate_r22     ; Torna positivo

do_div:
    call div16u         ; Faz a divisão unsigned
    
    ; Se r16 for ímpar (1), o resultado é negativo
    sbrs r16, 0
    rjmp end_divs
    call negate_r24     ; Inverte resultado

end_divs:
    pop r15
    pop r14
    pop r16
    ret

negate_r24:
    com r25
    neg r24
    sbci r25, 0xFF
    ret

negate_r22:
    com r23
    neg r22
    sbci r23, 0xFF
    ret

; === PRINT_INT16 (Impressão Decimal) ===
.global print_int16
print_int16:
    push r24
    push r25
    push r16 ; Preserva registradores que usaremos
    
    ; Verifica se é 0 (caso especial simples)
    mov r16, r24
    or r16, r25
    brne check_sign
    ldi r24, '0'
    call uart_tx
    rjmp p_end

check_sign:
    sbrs r25, 7         ; Verifica sinal
    rjmp p_start_rec
    
    push r24
    ldi r24, '-'
    call uart_tx        ; Imprime '-'
    pop r24
    call negate_r24     ; Torna positivo

p_start_rec:
    call p_rec

p_end:
    pop r16
    pop r25
    pop r24
    ret

; Função recursiva interna
p_rec:
    ; Se o número for 0, retorna (fim da recursão)
    mov r16, r24
    or r16, r25
    breq p_ret

    push r24
    push r25
    
    ldi r22, 10
    ldi r23, 0
    call div16u     ; R25:R24 = Quociente, R15:R14 = Resto
    
    ; O resto (R14) é o dígito que queremos imprimir DEPOIS da recursão
    push r14        ; Salva o dígito na pilha

    call p_rec      ; Recursão com o Quociente (que já está em R25:R24)
    
    pop r24         ; Recupera o dígito (estava em R14)
    subi r24, -'0'  ; Converte para ASCII (add 48)
    call uart_tx
    
    pop r25
    pop r24
p_ret:
    ret
