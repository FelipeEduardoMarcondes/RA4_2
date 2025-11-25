.section .bss
    .lcomm A, 2
    .lcomm B, 2
    .lcomm I, 2
    .lcomm N, 2
    .lcomm TEMP, 2
    .lcomm t1, 2
    .lcomm t10, 2
    .lcomm t11, 2
    .lcomm t12, 2
    .lcomm t13, 2
    .lcomm t14, 2
    .lcomm t15, 2
    .lcomm t16, 2
    .lcomm t17, 2
    .lcomm t18, 2
    .lcomm t19, 2
    .lcomm t20, 2
    .lcomm t21, 2
    .lcomm t22, 2
    .lcomm t24, 2
    .lcomm t25, 2
    .lcomm t26, 2
    .lcomm t28, 2
    .lcomm t29, 2
    .lcomm t3, 2
    .lcomm t30, 2
    .lcomm t31, 2
    .lcomm t32, 2
    .lcomm t5, 2
    .lcomm t7, 2
    .lcomm t8, 2
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
    ; TAC: MEM[A] = 0
    ldi r24, 0
    ldi r25, 0
    sts A, r24
    sts A + 1, r25
    ; TAC: t1 = PRINT[0]
    ldi r24, 0
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t1, r24
    sts t1 + 1, r25
    ; TAC: MEM[B] = 1
    ldi r24, 1
    ldi r25, 0
    sts B, r24
    sts B + 1, r25
    ; TAC: t3 = PRINT[1]
    ldi r24, 1
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t3, r24
    sts t3 + 1, r25
    ; TAC: MEM[I] = 0
    ldi r24, 0
    ldi r25, 0
    sts I, r24
    sts I + 1, r25
    ; TAC: t5 = PRINT[0]
    ldi r24, 0
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t5, r24
    sts t5 + 1, r25
    ; TAC: MEM[N] = 23
    ldi r24, 23
    ldi r25, 0
    sts N, r24
    sts N + 1, r25
    ; TAC: t7 = PRINT[23]
    ldi r24, 23
    ldi r25, 0
    call res_save
    call print_int16
    call uart_newline
    sts t7, r24
    sts t7 + 1, r25
    ; TAC: t8 = MEM[A]
    lds r24, A
    lds r25, A + 1
    sts t8, r24
    sts t8 + 1, r25
    ; TAC: t9 = PRINT[t8]
    lds r24, t8
    lds r25, t8 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t9, r24
    sts t9 + 1, r25
    ; TAC: t10 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t10, r24
    sts t10 + 1, r25
    ; TAC: t11 = PRINT[t10]
    lds r24, t10
    lds r25, t10 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t11, r24
    sts t11 + 1, r25
L0:
    ; TAC: t13 = MEM[I]
    lds r24, I
    lds r25, I + 1
    sts t13, r24
    sts t13 + 1, r25
    ; TAC: t14 = MEM[N]
    lds r24, N
    lds r25, N + 1
    sts t14, r24
    sts t14 + 1, r25
    ; TAC: t15 = t13 < t14
    lds r24, t13
    lds r25, t13 + 1
    lds r22, t14
    lds r23, t14 + 1
    call op_lt
    sts t15, r24
    sts t15 + 1, r25
    ; TAC: ifFalse t15 goto L1
    lds r24, t15
    lds r25, t15 + 1
    or r24, r25
    brne _skip_jmp_0
    rjmp L1
_skip_jmp_0:
    ; TAC: t16 = MEM[A]
    lds r24, A
    lds r25, A + 1
    sts t16, r24
    sts t16 + 1, r25
    ; TAC: t17 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t17, r24
    sts t17 + 1, r25
    ; TAC: t18 = t16 + t17
    lds r24, t16
    lds r25, t16 + 1
    lds r22, t17
    lds r23, t17 + 1
    add r24, r22
    adc r25, r23
    sts t18, r24
    sts t18 + 1, r25
    ; TAC: MEM[TEMP] = t18
    lds r24, t18
    lds r25, t18 + 1
    sts TEMP, r24
    sts TEMP + 1, r25
    ; TAC: t19 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t19, r24
    sts t19 + 1, r25
    ; TAC: MEM[A] = t19
    lds r24, t19
    lds r25, t19 + 1
    sts A, r24
    sts A + 1, r25
    ; TAC: t20 = t18 + t19
    lds r24, t18
    lds r25, t18 + 1
    lds r22, t19
    lds r23, t19 + 1
    add r24, r22
    adc r25, r23
    sts t20, r24
    sts t20 + 1, r25
    ; TAC: t21 = MEM[TEMP]
    lds r24, TEMP
    lds r25, TEMP + 1
    sts t21, r24
    sts t21 + 1, r25
    ; TAC: MEM[B] = t21
    lds r24, t21
    lds r25, t21 + 1
    sts B, r24
    sts B + 1, r25
    ; TAC: t22 = MEM[I]
    lds r24, I
    lds r25, I + 1
    sts t22, r24
    sts t22 + 1, r25
    ; TAC: t24 = t22 + 1
    lds r24, t22
    lds r25, t22 + 1
    ldi r22, 1
    ldi r23, 0
    add r24, r22
    adc r25, r23
    sts t24, r24
    sts t24 + 1, r25
    ; TAC: MEM[I] = t24
    lds r24, t24
    lds r25, t24 + 1
    sts I, r24
    sts I + 1, r25
    ; TAC: t25 = t21 + t24
    lds r24, t21
    lds r25, t21 + 1
    lds r22, t24
    lds r23, t24 + 1
    add r24, r22
    adc r25, r23
    sts t25, r24
    sts t25 + 1, r25
    ; TAC: t26 = t20 + t25
    lds r24, t20
    lds r25, t20 + 1
    lds r22, t25
    lds r23, t25 + 1
    add r24, r22
    adc r25, r23
    sts t26, r24
    sts t26 + 1, r25
    ; TAC: t28 = t26 > 0
    lds r24, t26
    lds r25, t26 + 1
    ldi r22, 0
    ldi r23, 0
    call op_gt
    sts t28, r24
    sts t28 + 1, r25
    ; TAC: ifFalse t28 goto L2
    lds r24, t28
    lds r25, t28 + 1
    or r24, r25
    brne _skip_jmp_1
    rjmp L2
_skip_jmp_1:
    ; TAC: t30 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t30, r24
    sts t30 + 1, r25
    ; TAC: t29 = t30
    lds r24, t30
    lds r25, t30 + 1
    sts t29, r24
    sts t29 + 1, r25
    ; TAC: goto L3
    rjmp L3
L2:
    ; TAC: t31 = MEM[B]
    lds r24, B
    lds r25, B + 1
    sts t31, r24
    sts t31 + 1, r25
    ; TAC: t29 = t31
    lds r24, t31
    lds r25, t31 + 1
    sts t29, r24
    sts t29 + 1, r25
L3:
    ; TAC: t12 = t29
    lds r24, t29
    lds r25, t29 + 1
    sts t12, r24
    sts t12 + 1, r25
    ; TAC: goto L0
    rjmp L0
L1:
    ; TAC: t32 = PRINT[t12]
    lds r24, t12
    lds r25, t12 + 1
    call res_save
    call print_int16
    call uart_newline
    sts t32, r24
    sts t32 + 1, r25
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
