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