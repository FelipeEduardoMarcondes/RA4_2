; lib_avr/math_fixed.s
; Aritmética Q8.8 (Ponto Fixo)

.section .text

; === FX_MUL (Multiplicação Q8.8) ===
.global fx_mul
fx_mul:
    push r20
    push r21
    push r16
    
    clr r16
    sbrs r25, 7
    rjmp chk_b_mul
    inc r16
    call fx_neg_a_local
chk_b_mul:
    sbrs r23, 7
    rjmp do_mul
    inc r16
    call fx_neg_b_local

do_mul:
    call mul16_32       ; R25..R22
    mov r25, r24
    mov r24, r23
    
    sbrs r16, 0
    rjmp mul_end
    call fx_neg_a_local

mul_end:
    pop r16
    pop r21
    pop r20
    ret

; === FX_DIV (Divisão Q8.8) ===
.global fx_div
fx_div:
    ; Salva contexto completo
    push r14
    push r15
    push r16
    push r17
    push r18
    push r19
    push r20
    push r21
    push r28

    ; 1. Calcula Sinal
    clr r28
    sbrs r25, 7
    rjmp div_check_b
    inc r28
    call fx_neg_a_local
div_check_b:
    sbrs r23, 7
    rjmp div_setup
    inc r28
    call fx_neg_b_local

div_setup:
    ; 2. Configura Divisor (B) em R21:R18
    mov r18, r22  ; B Low
    mov r19, r23  ; B High
    clr r20       ; Zero
    clr r21       ; Zero

    ; 3. Configura Dividendo (A) << 8 em R25:R22
    ; Entrada A: R25:R24
    mov r22, r25  ; Temp High
    
    mov r23, r24  ; A Low -> Byte 1
    mov r24, r22  ; A High -> Byte 2
    clr r22       ; Byte 0 = 0
    clr r25       ; Byte 3 = 0
    
    ; 4. Executa Divisão 32 bits
    call div32u   ; Quociente em R25:R22
    

    
    movw r24, r22 ; Copia R23:R22 para R25:R24
    
    ; 6. Aplica Sinal
    sbrs r28, 0
    rjmp div_restore
    call fx_neg_a_local

div_restore:
    pop r28
    pop r21
    pop r20
    pop r19
    pop r18
    pop r17
    pop r16
    pop r15
    pop r14
    ret

; === FX_POW (Potência) ===
.global fx_pow
fx_pow:
    push r20
    push r21
    push r22 ; Exp
    push r26
    push r27
    
    mov r26, r22
    
    cpi r26, 0
    brne pow_chk_1
    ldi r24, 0x00
    ldi r25, 0x01 ; 1.0
    rjmp pow_ret

pow_chk_1:
    cpi r26, 1
    breq pow_ret
    
    movw r20, r24 ; Base fixa
    dec r26

pow_loop:
    movw r22, r20
    call fx_mul
    dec r26
    brne pow_loop

pow_ret:
    pop r27
    pop r26
    pop r22
    pop r21
    pop r20
    ret

; Auxiliares
fx_neg_a_local:
    com r25
    neg r24
    sbci r25, 0xFF
    ret

fx_neg_b_local:
    com r23
    neg r22
    sbci r23, 0xFF
    ret

; === FX_PRINT ===
.global fx_print
fx_print:
    push r24
    push r25
    push r22
    push r23
    push r16
    
    sbrs r25, 7
    rjmp pr_int
    push r24
    ldi r24, '-'
    call uart_tx
    pop r24
    call fx_neg_a_local

pr_int:
    push r24
    mov r24, r25
    ldi r25, 0
    call print_int16
    pop r24
    
    push r24
    ldi r24, '.'
    call uart_tx
    pop r24
    
    ; Fração
    mov r22, r24
    ldi r23, 0
    mov r24, r22
    ldi r25, 0
    
    ldi r22, lo8(1000)
    ldi r23, hi8(1000)
    call mul16_32
    
    mov r25, r24
    mov r24, r23
    
    ; Padding
    ldi r16, 0
    cpi r24, 100
    cpc r25, r16
    brsh check_10
    push r24
    ldi r24, '0'
    call uart_tx
    pop r24

check_10:
    ldi r16, 0
    cpi r24, 10
    cpc r25, r16
    brsh do_print_frac
    push r24
    ldi r24, '0'
    call uart_tx
    pop r24

do_print_frac:
    call print_int16
    
    pop r16
    pop r23
    pop r22
    pop r25
    pop r24
    ret