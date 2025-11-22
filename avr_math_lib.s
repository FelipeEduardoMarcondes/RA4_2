; avr_math_lib.s - Biblioteca Matemática 16 bits
; Compatível com Calling Convention do GCC (R25:R24, R23:R22)

.section .text
.global mul16
.global div16u
.global mod16u
.global pow16u

; ---------------------------------------------------------
; MUL16: Multiplicação 16 bits Unsigned
; In: R25:R24 * R23:R22
; Out: R25:R24
; ---------------------------------------------------------
mul16:
    push r18
    push r19
    push r20
    push r21
    
    clr r20 ; Res Low
    clr r21 ; Res High
    
    ; R24 * R22
    mul r24, r22
    movw r20, r0
    
    ; R25 * R22
    mul r25, r22
    add r21, r0
    
    ; R24 * R23
    mul r24, r23
    add r21, r0
    
    movw r24, r20
    clr r1
    
    pop r21
    pop r20
    pop r19
    pop r18
    ret

; ---------------------------------------------------------
; DIV16U: Divisão 16 bits Unsigned
; In: R25:R24 (Num) / R23:R22 (Den)
; Out: R25:R24 (Quoc), R27:R26 (Resto - Interno/Trash)
; ---------------------------------------------------------
div16u:
    push r16
    push r17
    push r26
    push r27
    
    clr r26
    clr r27
    ldi r16, 17
    
div16_loop:
    dec r16
    breq div16_end
    
    lsl r26
    rol r27
    
    lsl r24
    rol r25
    adc r26, r1
    
    cp r26, r22
    cpc r27, r23
    brcs div16_next
    
    sub r26, r22
    sbc r27, r23
    inc r24
    
div16_next:
    rjmp div16_loop
    
div16_end:
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
    
    clr r26
    clr r27
    ldi r16, 17
    
mod16_loop:
    dec r16
    breq mod16_end
    
    lsl r26
    rol r27
    
    lsl r24
    rol r25
    adc r26, r1
    
    cp r26, r22
    cpc r27, r23
    brcs mod16_next
    
    sub r26, r22
    sbc r27, r23
    inc r24
    
mod16_next:
    rjmp mod16_loop
    
mod16_end:
    ; O resto ficou em R27:R26. Move para R25:R24 para retorno
    movw r24, r26
    
    pop r27
    pop r26
    pop r17
    pop r16
    ret

; ---------------------------------------------------------
; POW16U: Potência 16 bits (Simples)
; In: R25:R24 ^ R23:R22
; Out: R25:R24
; ---------------------------------------------------------
pow16u:
    push r20
    push r21
    
    ; R21:R20 guarda a Base
    movw r20, r24
    
    ; Resultado = 1
    ldi r24, 1
    ldi r25, 0
    
    ; Se expoente (R23:R22) for 0, retorna 1
    mov r16, r22
    or r16, r23
    breq pow16_exit
    
pow16_loop:
    ; Multiplica acumulador pela base
    ; Salva expoente (pois mul16 usa R22/R23)
    push r22
    push r23
    
    ; Configura args para mul16: Res * Base
    ; R25:R24 já é o Res
    movw r22, r20 ; Op2 = Base
    call mul16
    
    pop r23
    pop r22
    
    ; Decrementa expoente (R23:R22)
    ; CORREÇÃO: sbiw não funciona em r22. Usamos subi/sbci.
    subi r22, 1
    sbci r23, 0
    
    ; Se não for zero, continua
    ; Para testar se r23:r22 é zero, fazemos OR
    mov r16, r22
    or r16, r23
    brne pow16_loop
    
pow16_exit:
    pop r21
    pop r20
    ret