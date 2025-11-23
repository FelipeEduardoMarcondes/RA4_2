; lib_avr/runtime.s
; Operadores Relacionais e Wrappers Inteiros
; Retorno Booleano: 1 (True) ou 0 (False) em R25:R24

.section .text

; ==========================================================
; OPERADORES RELACIONAIS (Signed 16-bit)
; Compara R25:R24 (A) com R23:R22 (B)
; ==========================================================

; === OP_EQ (==) ===
.global op_eq
op_eq:
    cp r24, r22
    cpc r25, r23
    breq is_true
    rjmp is_false

; === OP_NEQ (!=) ===
.global op_neq
op_neq:
    cp r24, r22
    cpc r25, r23
    brne is_true
    rjmp is_false

; === OP_GT (>) ===
.global op_gt
op_gt:
    cp r22, r24     ; Compare B with A (Inverse for GT logic)
    cpc r23, r25
    brlt is_true    ; Se B < A, então A > B
    rjmp is_false

; === OP_LT (<) ===
.global op_lt
op_lt:
    cp r24, r22     ; Compare A with B
    cpc r25, r23
    brlt is_true    ; Signed Less Than
    rjmp is_false

; === OP_GE (>=) ===
.global op_ge
op_ge:
    cp r24, r22
    cpc r25, r23
    brge is_true    ; Signed Greater or Equal
    rjmp is_false

; === OP_LE (<=) ===
.global op_le
op_le:
    cp r22, r24
    cpc r23, r25
    brge is_true    ; Se B >= A, então A <= B
    rjmp is_false

; --- Helpers de Retorno ---
is_true:
    ldi r24, 1
    ldi r25, 0
    ret

is_false:
    ldi r24, 0
    ldi r25, 0
    ret


; ==========================================================
; WRAPPERS ARITMÉTICOS INTEIROS
; ==========================================================

; === OP_MOD (%) ===
; Resto da divisão inteira de R25:R24 por R23:R22
.global op_mod
op_mod:
    call div16u     ; Faz a divisão padrão
    ; div16u (versão math_core.s) retorna Quociente em R25:R24
    ; e Resto em R15:R14.
    ; Precisamos mover o Resto para R25:R24 (Retorno padrão)
    
    movw r24, r14   ; Move R15:R14 -> R25:R24
    ret

; === OP_POW_INT (Inteiro ^ Inteiro) ===
; Base: R25:R24, Exp: R22 (8 bits é suficiente para o projeto)
.global op_pow_int
op_pow_int:
    push r20
    push r21
    push r22
    
    mov r20, r22 ; Copia Expoente
    
    ; Exp == 0 -> 1
    cpi r20, 0
    brne chk_p1
    ldi r24, 1
    ldi r25, 0
    rjmp pi_end
    
chk_p1:
    ; Exp == 1 -> Base (já está em R25:R24)
    cpi r20, 1
    breq pi_end
    
    ; Setup loop
    dec r20         ; Já temos base^1
    movw r22, r24   ; R23:R22 guarda a BASE fixa
    ; R25:R24 guarda o ACUMULADO

pi_loop:
    ; Precisamos chamar mul16u(Acumulado, Base)
    ; mul16u espera A em R25:R24 e B em R23:R22.
    ; Já está configurado corretamente (Acumulado em 25:24, Base em 23:22)
    ; PORÉM: mul16u destrói R22/R23 (B) nos pops? 
    ; Verificando math_core.s: mul16u usa push/pop de r20/r21...
    ; Mas mul16u não garante preservar B (R23:R22) se usá-lo como temp?
    ; O mul16u atual preserva R18-R21. R22 e R23 são registradores de argumento,
    ; normalmente considerados "scratch" (sujos).
    ; Vamos salvar a Base em R21:R20 (seguros) e restaurar a cada loop.

    push r22 ; Salva Base Low
    push r23 ; Salva Base High
    
    call mul16u
    
    pop r23  ; Recupera para o próximo loop
    pop r22
    
    dec r20
    brne pi_loop

pi_end:
    pop r22
    pop r21
    pop r20
    ret