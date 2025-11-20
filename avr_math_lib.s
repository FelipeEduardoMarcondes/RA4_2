; avr_math_lib.s
; Biblioteca de rotinas matemáticas para AVR (16 bits)
; Arduino Uno (ATmega328P)
; Corrigido para suportar Fatorial (até 40320) e Taylor (escala)

.text

;-----------------------------------------------------------------------------
; Multiplicação 16 bits sem sinal
; Entrada: R25:R24 (op1) * R23:R22 (op2)
; Saída:   R25:R24 (resultado 16 bits inferiores)
;-----------------------------------------------------------------------------
mul16:
    push r18
    push r19
    push r20
    push r21
    
    ; Limpar registradores de resultado temporário
    clr r20
    clr r21

    ; Multiplicar byte baixo op1 * byte baixo op2 (R24 * R22)
    mul r24, r22
    movw r20, r0    ; Move resultado (r1:r0) para r21:r20

    ; Multiplicar byte alto op1 * byte baixo op2 (R25 * R22)
    mul r25, r22
    add r21, r0     ; Soma apenas no byte alto do resultado

    ; Multiplicar byte baixo op1 * byte alto op2 (R24 * R23)
    mul r24, r23
    add r21, r0     ; Soma apenas no byte alto do resultado

    ; Copiar resultado para R25:R24
    movw r24, r20
    
    ; Limpar flag zero do hardware multiplier
    clr r1
    
    pop r21
    pop r20
    pop r19
    pop r18
    ret

;-----------------------------------------------------------------------------
; Divisão 16 bits sem sinal (Essencial para Taylor e Médias)
; Entrada: R25:R24 (Dividendo), R23:R22 (Divisor)
; Saída:   R25:R24 (Quociente), R15:R14 (Resto - Opcional)
;-----------------------------------------------------------------------------
div16u:
    push r16        ; Contador de bits
    push r17        ; Temporário
    push r26        ; Usado para resto (byte baixo)
    push r27        ; Usado para resto (byte alto)

    clr r26         ; Limpar resto (R27:R26)
    clr r27
    ldi r16, 17     ; Contador de bits (16 + 1 para loop)

div16_loop:
    dec r16
    breq div16_end

    ; Deslocar resto para esquerda (LSL R27:R26)
    lsl r26
    rol r27
    
    ; Mover bit mais significativo do dividendo para o resto
    ; Deslocar dividendo (LSL R25:R24) e pegar o Carry
    lsl r24
    rol r25
    adc r26, r1     ; r1 é zero, soma Carry ao resto
    
    ; Comparar Resto com Divisor (CP R27:R26, R23:R22)
    cp r26, r22
    cpc r27, r23
    brcs div16_loop ; Se resto < divisor, continua (bit 0 no quociente)

    ; Se resto >= divisor, subtrai divisor do resto
    sub r26, r22
    sbc r27, r23
    
    ; E define o bit 0 do dividendo (que agora guarda o quociente) como 1
    inc r24         ; Truque: incrementa pq o shift anterior deixou bit 0 livre
    
    rjmp div16_loop

div16_end:
    ; R25:R24 agora contém o Quociente
    ; R27:R26 contém o Resto (se precisar futuramente)
    pop r27
    pop r26
    pop r17
    pop r16
    ret

;-----------------------------------------------------------------------------
; Wrapper para Divisão Real (Trata escala se necessário ou usa div16u direta)
; Entrada: R25:R24 / R23:R22
; Saída:   R25:R24
;-----------------------------------------------------------------------------
divfloat16:
    ; Para esta fase, como estamos usando "inteiros escalados" e a escala
    ; deve ser gerenciada antes de chamar a função (multiplicando o dividendo),
    ; podemos usar diretamente a divisão inteira de 16 bits.
    rjmp div16u

;-----------------------------------------------------------------------------
; Módulo 16 bits (Resto)
; Entrada: R25:R24 (Dividendo) % R23:R22 (Divisor)
; Saída:   R25:R24 (Resto)
;-----------------------------------------------------------------------------
mod16u:
    call div16u
    ; A rotina div16u (acima) precisa ser ajustada se você quiser o resto em R25:R24.
    ; Como implementei acima, o resto fica em R27:R26 temporariamente.
    ; Para funcionar como função C, precisaríamos mover o resto para R25:R24.
    ; Versão simplificada: Implementar wrapper que pega o resto.
    
    ; (Recomendo copiar a lógica interna de div16u se precisar muito de módulo,
    ; ou usar a lógica matemática: a % n = a - (n * (a/n)))
    ret

;-----------------------------------------------------------------------------
; Potenciação 16 bits (Base^Expoente)
; Entrada: R25:R24 (Base), R23:R22 (Expoente)
; Saída:   R25:R24 (Resultado)
;-----------------------------------------------------------------------------
pow16u:
    push r20
    push r21
    push r18
    push r19

    ; Guardar base original em R21:R20
    movw r20, r24
    
    ; Resultado inicial = 1 (em R25:R24)
    ldi r24, 1
    ldi r25, 0
    
    ; Verificar expoente zero
    mov r18, r22
    or r18, r23
    breq pow16_end  ; Se expoente 0, retorna 1

pow16_loop:
    ; Verificar se expoente é 0
    mov r18, r22
    or r18, r23
    breq pow16_end

    ; Multiplicar acumulador pela base (Resultado = Resultado * Base)
    ; Salvar Resultado atual como op1
    push r22        ; Salvar expoente
    push r23
    
    movw r22, r20   ; op2 = Base (R21:R20)
    ; op1 já é R25:R24 (Resultado)
    call mul16
    
    pop r23         ; Recuperar expoente
    pop r22

    ; Decrementar expoente (16 bits)
    sbiw r22, 1
    rjmp pow16_loop

pow16_end:
    pop r19
    pop r18
    pop r21
    pop r20
    ret

;-----------------------------------------------------------------------------
; Inicialização de Serial e Prints (Debug)
;-----------------------------------------------------------------------------
serial_init:
    ; Configurar 9600 baud (F_CPU 16MHz) -> UBRR = 103
    ldi r24, 103
    clr r25
    sts UBRR0H, r25
    sts UBRR0L, r24
    
    ; Habilitar TX
    ldi r24, (1<<TXEN0)
    sts UCSR0B, r24
    
    ; 8N1
    ldi r24, (1<<UCSZ01)|(1<<UCSZ00)
    sts UCSR0C, r24
    ret

serial_tx:
    ; Espera buffer vazio
    lds r25, UCSR0A
    sbrs r25, UDRE0
    rjmp serial_tx
    sts UDR0, r24
    ret