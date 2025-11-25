.section .bss
    .lcomm FAT, 2
    .lcomm FATORIAL1, 2
    .lcomm FATORIAL2, 2
    .lcomm FATORIAL3, 2
    .lcomm FATORIAL4, 2
    .lcomm FATORIAL5, 2
    .lcomm FATORIAL6, 2
    .lcomm FATORIAL7, 2
    .lcomm FATORIAL8, 2
    .lcomm N, 2
    .lcomm NUM, 2
    .lcomm RESULTADO, 2
    .lcomm t1, 2
    .lcomm t10, 2
    .lcomm t11, 2
    .lcomm t13, 2
    .lcomm t14, 2
    .lcomm t15, 2
    .lcomm t16, 2
    .lcomm t17, 2
    .lcomm t19, 2
    .lcomm t21, 2
    .lcomm t23, 2
    .lcomm t27, 2
    .lcomm t29, 2
    .lcomm t3, 2
    .lcomm t30, 2
    .lcomm t32, 2
    .lcomm t34, 2
    .lcomm t35, 2
    .lcomm t36, 2
    .lcomm t38, 2
    .lcomm t39, 2
    .lcomm t4, 2
    .lcomm t41, 2
    .lcomm t43, 2
    .lcomm t44, 2
    .lcomm t45, 2
    .lcomm t47, 2
    .lcomm t48, 2
    .lcomm t5, 2
    .lcomm t50, 2
    .lcomm t52, 2
    .lcomm t53, 2
    .lcomm t54, 2
    .lcomm t56, 2
    .lcomm t57, 2
    .lcomm t59, 2
    .lcomm t61, 2
    .lcomm t62, 2
    .lcomm t63, 2
    .lcomm t65, 2
    .lcomm t66, 2
    .lcomm t68, 2
    .lcomm t7, 2
    .lcomm t70, 2
    .lcomm t71, 2
    .lcomm t72, 2
    .lcomm t74, 2
    .lcomm t75, 2
    .lcomm t77, 2
    .lcomm t79, 2
    .lcomm t8, 2
    .lcomm t80, 2
    .lcomm t81, 2
    .lcomm t83, 2
    .lcomm t84, 2
    .lcomm t9, 2
.section .text
.global main
main:
    ; --- Setup Inicial ---
    clr r1
    ldi r16, 0x08
    out 0x3E, r16
    ldi r16, 0xFF
    out 0x3D, r16
    call uart_init
    call res_init
    ; TAC: MEM[N] = 1
    ldi r24, 1
    ldi r25, 0
    sts N, r24
    sts N + 1, r25
    ; TAC: t1 = PRINT[1]
    ldi r24, 1
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t1, r24
    sts t1 + 1, r25
    ; TAC: MEM[FAT] = 1
    ldi r24, 1
    ldi r25, 0
    sts FAT, r24
    sts FAT + 1, r25
    ; TAC: t3 = PRINT[1]
    ldi r24, 1
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t3, r24
    sts t3 + 1, r25
L0:
    ; TAC: t5 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t5, r24
    sts t5 + 1, r25
    ; TAC: t7 = t5 <= 8
    lds r24, t5
    lds r25, t5 + 1
    ldi r22, 8
    ldi r23, 0
    call op_le
    sts t7, r24
    sts t7 + 1, r25
    ; TAC: ifFalse t7 goto L1
    lds r24, t7
    lds r25, t7 + 1
    or r24, r25
    brne _skip_jmp_0
    rjmp L1
_skip_jmp_0:
    ; TAC: t8 = MEM[FAT]
    lds r24, FAT
    lds r25, FAT + 1
    sts t8, r24
    sts t8 + 1, r25
    ; TAC: t9 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t9, r24
    sts t9 + 1, r25
    ; TAC: t10 = t8 * t9
    lds r24, t8
    lds r25, t8 + 1
    lds r22, t9
    lds r23, t9 + 1
    call mul16u
    sts t10, r24
    sts t10 + 1, r25
    ; TAC: MEM[FAT] = t10
    lds r24, t10
    lds r25, t10 + 1
    sts FAT, r24
    sts FAT + 1, r25
    ; TAC: t11 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t11, r24
    sts t11 + 1, r25
    ; TAC: t13 = t11 + 1
    lds r24, t11
    lds r25, t11 + 1
    ldi r22, 1
    ldi r23, 0
    add r24, r22
    adc r25, r23
    sts t13, r24
    sts t13 + 1, r25
    ; TAC: MEM[N] = t13
    lds r24, t13
    lds r25, t13 + 1
    sts N, r24
    sts N + 1, r25
    ; TAC: t14 = t10 * t13
    lds r24, t10
    lds r25, t10 + 1
    lds r22, t13
    lds r23, t13 + 1
    call mul16u
    sts t14, r24
    sts t14 + 1, r25
    ; TAC: t4 = t14
    lds r24, t14
    lds r25, t14 + 1
    sts t4, r24
    sts t4 + 1, r25
    ; TAC: goto L0
    rjmp L0
L1:
    ; TAC: t15 = PRINT[t4]
    lds r24, t4
    lds r25, t4 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t15, r24
    sts t15 + 1, r25
    ; TAC: t16 = MEM[FAT]
    lds r24, FAT
    lds r25, FAT + 1
    sts t16, r24
    sts t16 + 1, r25
    ; TAC: MEM[RESULTADO] = t16
    lds r24, t16
    lds r25, t16 + 1
    sts RESULTADO, r24
    sts RESULTADO + 1, r25
    ; TAC: t17 = PRINT[t16]
    lds r24, t16
    lds r25, t16 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t17, r24
    sts t17 + 1, r25
    ; TAC: MEM[NUM] = 1
    ldi r24, 1
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t19 = PRINT[1]
    ldi r24, 1
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t19, r24
    sts t19 + 1, r25
    ; TAC: MEM[FATORIAL1] = 1
    ldi r24, 1
    ldi r25, 0
    sts FATORIAL1, r24
    sts FATORIAL1 + 1, r25
    ; TAC: t21 = PRINT[1]
    ldi r24, 1
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t21, r24
    sts t21 + 1, r25
    ; TAC: MEM[NUM] = 2
    ldi r24, 2
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t23 = PRINT[2]
    ldi r24, 2
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t23, r24
    sts t23 + 1, r25
    ; TAC: t27 = PRINT[2]
    ldi r24, 2
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t27, r24
    sts t27 + 1, r25
    ; TAC: t29 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t29, r24
    sts t29 + 1, r25
    ; TAC: MEM[FATORIAL2] = t29
    lds r24, t29
    lds r25, t29 + 1
    sts FATORIAL2, r24
    sts FATORIAL2 + 1, r25
    ; TAC: t30 = PRINT[t29]
    lds r24, t29
    lds r25, t29 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t30, r24
    sts t30 + 1, r25
    ; TAC: MEM[NUM] = 3
    ldi r24, 3
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t32 = PRINT[3]
    ldi r24, 3
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t32, r24
    sts t32 + 1, r25
    ; TAC: t34 = MEM[FATORIAL2]
    lds r24, FATORIAL2
    lds r25, FATORIAL2 + 1
    sts t34, r24
    sts t34 + 1, r25
    ; TAC: t35 = 2 * t34
    ldi r24, 2
    ldi r25, 0
    lds r22, t34
    lds r23, t34 + 1
    call mul16u
    sts t35, r24
    sts t35 + 1, r25
    ; TAC: t36 = PRINT[t35]
    lds r24, t35
    lds r25, t35 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t36, r24
    sts t36 + 1, r25
    ; TAC: t38 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t38, r24
    sts t38 + 1, r25
    ; TAC: MEM[FATORIAL3] = t38
    lds r24, t38
    lds r25, t38 + 1
    sts FATORIAL3, r24
    sts FATORIAL3 + 1, r25
    ; TAC: t39 = PRINT[t38]
    lds r24, t38
    lds r25, t38 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t39, r24
    sts t39 + 1, r25
    ; TAC: MEM[NUM] = 4
    ldi r24, 4
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t41 = PRINT[4]
    ldi r24, 4
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t41, r24
    sts t41 + 1, r25
    ; TAC: t43 = MEM[FATORIAL3]
    lds r24, FATORIAL3
    lds r25, FATORIAL3 + 1
    sts t43, r24
    sts t43 + 1, r25
    ; TAC: t44 = 3 * t43
    ldi r24, 3
    ldi r25, 0
    lds r22, t43
    lds r23, t43 + 1
    call mul16u
    sts t44, r24
    sts t44 + 1, r25
    ; TAC: t45 = PRINT[t44]
    lds r24, t44
    lds r25, t44 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t45, r24
    sts t45 + 1, r25
    ; TAC: t47 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t47, r24
    sts t47 + 1, r25
    ; TAC: MEM[FATORIAL4] = t47
    lds r24, t47
    lds r25, t47 + 1
    sts FATORIAL4, r24
    sts FATORIAL4 + 1, r25
    ; TAC: t48 = PRINT[t47]
    lds r24, t47
    lds r25, t47 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t48, r24
    sts t48 + 1, r25
    ; TAC: MEM[NUM] = 5
    ldi r24, 5
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t50 = PRINT[5]
    ldi r24, 5
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t50, r24
    sts t50 + 1, r25
    ; TAC: t52 = MEM[FATORIAL4]
    lds r24, FATORIAL4
    lds r25, FATORIAL4 + 1
    sts t52, r24
    sts t52 + 1, r25
    ; TAC: t53 = 4 * t52
    ldi r24, 4
    ldi r25, 0
    lds r22, t52
    lds r23, t52 + 1
    call mul16u
    sts t53, r24
    sts t53 + 1, r25
    ; TAC: t54 = PRINT[t53]
    lds r24, t53
    lds r25, t53 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t54, r24
    sts t54 + 1, r25
    ; TAC: t56 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t56, r24
    sts t56 + 1, r25
    ; TAC: MEM[FATORIAL5] = t56
    lds r24, t56
    lds r25, t56 + 1
    sts FATORIAL5, r24
    sts FATORIAL5 + 1, r25
    ; TAC: t57 = PRINT[t56]
    lds r24, t56
    lds r25, t56 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t57, r24
    sts t57 + 1, r25
    ; TAC: MEM[NUM] = 6
    ldi r24, 6
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t59 = PRINT[6]
    ldi r24, 6
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t59, r24
    sts t59 + 1, r25
    ; TAC: t61 = MEM[FATORIAL5]
    lds r24, FATORIAL5
    lds r25, FATORIAL5 + 1
    sts t61, r24
    sts t61 + 1, r25
    ; TAC: t62 = 5 * t61
    ldi r24, 5
    ldi r25, 0
    lds r22, t61
    lds r23, t61 + 1
    call mul16u
    sts t62, r24
    sts t62 + 1, r25
    ; TAC: t63 = PRINT[t62]
    lds r24, t62
    lds r25, t62 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t63, r24
    sts t63 + 1, r25
    ; TAC: t65 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t65, r24
    sts t65 + 1, r25
    ; TAC: MEM[FATORIAL6] = t65
    lds r24, t65
    lds r25, t65 + 1
    sts FATORIAL6, r24
    sts FATORIAL6 + 1, r25
    ; TAC: t66 = PRINT[t65]
    lds r24, t65
    lds r25, t65 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t66, r24
    sts t66 + 1, r25
    ; TAC: MEM[NUM] = 7
    ldi r24, 7
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t68 = PRINT[7]
    ldi r24, 7
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t68, r24
    sts t68 + 1, r25
    ; TAC: t70 = MEM[FATORIAL6]
    lds r24, FATORIAL6
    lds r25, FATORIAL6 + 1
    sts t70, r24
    sts t70 + 1, r25
    ; TAC: t71 = 6 * t70
    ldi r24, 6
    ldi r25, 0
    lds r22, t70
    lds r23, t70 + 1
    call mul16u
    sts t71, r24
    sts t71 + 1, r25
    ; TAC: t72 = PRINT[t71]
    lds r24, t71
    lds r25, t71 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t72, r24
    sts t72 + 1, r25
    ; TAC: t74 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t74, r24
    sts t74 + 1, r25
    ; TAC: MEM[FATORIAL7] = t74
    lds r24, t74
    lds r25, t74 + 1
    sts FATORIAL7, r24
    sts FATORIAL7 + 1, r25
    ; TAC: t75 = PRINT[t74]
    lds r24, t74
    lds r25, t74 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t75, r24
    sts t75 + 1, r25
    ; TAC: MEM[NUM] = 8
    ldi r24, 8
    ldi r25, 0
    sts NUM, r24
    sts NUM + 1, r25
    ; TAC: t77 = PRINT[8]
    ldi r24, 8
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t77, r24
    sts t77 + 1, r25
    ; TAC: t79 = MEM[FATORIAL7]
    lds r24, FATORIAL7
    lds r25, FATORIAL7 + 1
    sts t79, r24
    sts t79 + 1, r25
    ; TAC: t80 = 7 * t79
    ldi r24, 7
    ldi r25, 0
    lds r22, t79
    lds r23, t79 + 1
    call mul16u
    sts t80, r24
    sts t80 + 1, r25
    ; TAC: t81 = PRINT[t80]
    lds r24, t80
    lds r25, t80 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t81, r24
    sts t81 + 1, r25
    ; TAC: t83 = RES[1]
    ldi r22, 1
    ldi r23, 0
    call res_fetch
    sts t83, r24
    sts t83 + 1, r25
    ; TAC: MEM[FATORIAL8] = t83
    lds r24, t83
    lds r25, t83 + 1
    sts FATORIAL8, r24
    sts FATORIAL8 + 1, r25
    ; TAC: t84 = PRINT[t83]
    lds r24, t83
    lds r25, t83 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t84, r24
    sts t84 + 1, r25
end_loop:
    rjmp end_loop

; === BIBLIOTECAS AVR ===

; === LIB: lib_avr/uart.s ===
; lib_avr/uart.s
; Funções de Comunicação Serial (9600 baud @ 16MHz)

.section .text

; === UART_INIT ===
.global uart_init
uart_init:
    push r16
    ; Baud Rate 9600 (UBRR = 103)
    ldi r16, 0
    sts 0xC5, r16 ; UBRR0H
    ldi r16, 103
    sts 0xC4, r16 ; UBRR0L
    ; Habilita TX
    ldi r16, (1<<3)
    sts 0xC1, r16 ; UCSR0B
    ; Formato 8N1
    ldi r16, (1<<1) | (1<<2)
    sts 0xC2, r16 ; UCSR0C
    pop r16
    ret

; === UART_TX ===
; Envia o byte em R24
.global uart_tx
uart_tx:
    push r16
tx_wait:
    lds r16, 0xC0 ; UCSR0A
    sbrs r16, 5   ; Check UDRE0
    rjmp tx_wait
    sts 0xC6, r24 ; UDR0
    pop r16
    ret

; === UART_NEWLINE ===
.global uart_newline
uart_newline:
    push r24
    ldi r24, 13 ; CR
    call uart_tx
    ldi r24, 10 ; LF
    call uart_tx
    pop r24
    ret

; === LIB: lib_avr/math_core.s ===
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

; === LIB: lib_avr/math_inteiro.s ===
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

; === LIB: lib_avr/runtime.s ===
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

; === LIB: lib_avr/storage.s ===
; lib_avr/storage.s
; Gerenciamento de Memória (RES e MEM)
; Roda no ATmega328P (2KB SRAM)

.section .bss
    ; --- Buffer para o histórico de RES ---
    ; Alocamos espaço para 100 resultados (200 bytes)
    ; Se o programa tiver mais de 100 linhas, ele sobrescreve ou trava (simples por enquanto)
    .lcomm res_buffer, 200 
    .lcomm res_count, 1    ; Contador de quantos resultados já salvamos (0 a 255)

    ; --- Memória de Variáveis (MEM) ---
    ; Vamos supor 26 variáveis possíveis (A-Z) ou apenas uma "MEM" genérica.
    ; O documento diz: "(V MEM): Armazena em uma memória".
    ; E "(MEM): Retorna o valor". Parece ser uma variável única ou poucas.
    ; Vamos alocar espaço para 1 variável genérica chamada MEM_VAL
    .lcomm mem_val, 2      ; 2 bytes para a variável MEM
    .lcomm mem_init, 1     ; Flag: 0 = não inicializada, 1 = inicializada

.section .text

; ==========================================================
; FUNÇÕES DE RES (Histórico)
; ==========================================================

; === RES_INIT ===
; Zera o contador de resultados no início do programa
.global res_init
res_init:
    push r16
    ldi r16, 0
    sts res_count, r16
    pop r16
    ret

; === RES_SAVE ===
; Salva o valor atual (R25:R24) no topo do histórico
; Deve ser chamado ao final de CADA expressão calculada
.global res_save
res_save:
    push r16
    push r30
    push r31
    
    ; 1. Pega o índice atual (res_count)
    lds r16, res_count
    
    ; 2. Calcula endereço: res_buffer + (index * 2)
    ldi r30, lo8(res_buffer)
    ldi r31, hi8(res_buffer)
    
    ; Adiciona (r16 * 2) ao Z
    add r30, r16
    adc r31, r1  ; r1 é zero
    add r30, r16 ; Adiciona de novo para multiplicar por 2
    adc r31, r1
    
    ; 3. Armazena R25:R24 na RAM
    st Z+, r24   ; Low byte
    st Z, r25    ; High byte
    
    ; 4. Incrementa contador
    lds r16, res_count
    inc r16
    sts res_count, r16
    
    pop r31
    pop r30
    pop r16
    ret

; === RES_FETCH ===
; Busca o resultado N linhas atrás
; Entrada: R22 (N - inteiro 8 bits)
; Saída:   R25:R24 (Valor recuperado)
.global res_fetch
res_fetch:
    push r16
    push r30
    push r31
    
    ; 1. Pega o total de resultados salvos
    lds r16, res_count
    
    ; 2. Calcula o índice alvo: (Count - N)
    ; Se N=1, queremos o anterior imediato (Count - 1)
    ; O comando diz "N linhas anteriores".
    ; Se N=1, é o último salvo.
    sub r16, r22
    
    ; Opcional: Verificar se r16 < 0 (Underflow/Erro)
    ; Por simplicidade, assumimos que o usuário não pede RES maior que o existente.
    ; Como o índice é 0-based no save, mas o count é incrementado, 
    ; se salvamos 1 item, count é 1. Se pedimos 1 RES, queremos indice 0.
    ; 1 - 1 = 0. Correto.
    
    ; 3. Calcula endereço: res_buffer + (target * 2)
    ldi r30, lo8(res_buffer)
    ldi r31, hi8(res_buffer)
    
    add r30, r16
    adc r31, r1
    add r30, r16
    adc r31, r1
    
    ; 4. Lê da RAM
    ld r24, Z+
    ld r25, Z
    
    pop r31
    pop r30
    pop r16
    ret

; ==========================================================
; FUNÇÕES DE MEM (Variável)
; ==========================================================

; === MEM_STORE ===
; Salva R25:R24 na variável MEM e marca como inicializada
.global mem_store
mem_store:
    push r16
    
    ; Salva valor
    sts mem_val, r24
    sts mem_val+1, r25
    
    ; Marca flag de inicialização
    ldi r16, 1
    sts mem_init, r16
    
    pop r16
    ret

; === MEM_LOAD ===
; Carrega o valor de MEM para R25:R24
; Se não inicializada, o comportamento é indefinido no Assembly 
; (o analisador semântico já deve ter barrado isso), 
; mas retornaremos 0 por segurança.
.global mem_load
mem_load:
    push r16
    
    ; Verifica se inicializada (Opcional, pois o Semântico garante)
    lds r16, mem_init
    cpi r16, 1
    breq do_load
    
    ; Se não, retorna 0
    ldi r24, 0
    ldi r25, 0
    rjmp end_mem_load

do_load:
    lds r24, mem_val
    lds r25, mem_val+1

end_mem_load:
    pop r16
    ret
