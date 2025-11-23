; lib_avr/math_core.s
; Matemática Unsigned (Base)

.section .text

; === MUL16U (16x16 -> 16) ===
.global mul16u
mul16u:
    push r18
    push r19
    push r20
    push r21
    movw r18, r24
    movw r20, r22
    mul r18, r20
    movw r24, r0
    mul r19, r20
    add r25, r0
    mul r18, r21
    add r25, r0
    clr r1
    pop r21
    pop r20
    pop r19
    pop r18
    ret

; === MUL16_32 (16x16 -> 32) ===
.global mul16_32
mul16_32:
    push r16
    push r17
    push r18
    push r19
    push r20
    push r21
    
    movw r18, r24       ; A
    movw r20, r22       ; B
    
    clr r22 ; Res Byte 0
    clr r23 ; Res Byte 1
    clr r24 ; Res Byte 2
    clr r25 ; Res Byte 3
    
    ; A0*B0
    mul r18, r20
    movw r22, r0
    
    ; A0*B1
    mul r18, r21
    add r23, r0
    adc r24, r1
    ldi r16, 0
    adc r25, r16
    
    ; A1*B0
    mul r19, r20
    add r23, r0
    adc r24, r1
    adc r25, r16
    
    ; A1*B1
    mul r19, r21
    add r24, r0
    adc r25, r1
    
    clr r1
    pop r21
    pop r20
    pop r19
    pop r18
    pop r17
    pop r16
    ret

; === DIV32U (32 / 32 -> 32) ===
; Dividendo: R25:R22 (Retorna Quociente aqui)
; Divisor:   R21:R18
; Modifica:  R14-R17 (Resto), R26
.global div32u
div32u:
    push r26
    
    ; Limpa Resto
    clr r14
    clr r15
    clr r16
    clr r17
    
    ldi r26, 32     ; 32 bits exatos

div32_loop:
    ; Shift Dividendo/Quociente (R25:R22)
    lsl r22
    rol r23
    rol r24
    rol r25
    
    ; Shift Resto (R17:R14)
    rol r14
    rol r15
    rol r16
    rol r17
    
    ; Compara Resto com Divisor
    cp r14, r18
    cpc r15, r19
    cpc r16, r20
    cpc r17, r21
    brcs div32_next ; Se Carry Set (Resto < Div), não subtrai
    
    ; Subtrai (Resto - Divisor)
    sub r14, r18
    sbc r15, r19
    sbc r16, r20
    sbc r17, r21
    
    ; Seta bit 0 do Quociente
    inc r22

div32_next:
    dec r26
    brne div32_loop
    
    pop r26
    ret

; === DIV16U (16 / 16 -> 16) ===
.global div16u
div16u:
    push r16
    push r17
    push r26
    push r27
    movw r26, r24       
    movw r16, r22       
    mov r14, r16
    or r14, r17
    brne d16_run
    ldi r24, 0xFF
    ldi r25, 0xFF
    rjmp d16_end
d16_run:
    clr r24
    clr r25
    clr r14
    clr r15
    ldi r18, 16
d16_loop:
    lsl r24
    rol r25
    lsl r26
    rol r27
    rol r14
    rol r15
    cp r14, r16
    cpc r15, r17
    brcs d16_next
    sub r14, r16
    sbc r15, r17
    inc r24
d16_next:
    dec r18
    brne d16_loop
d16_end:
    pop r27
    pop r26
    pop r17
    pop r16
    ret