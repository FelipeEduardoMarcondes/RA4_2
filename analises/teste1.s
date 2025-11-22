; Seção de Dados
.data

; Seção de Código
.text
; Definições de Hardware (ATmega328P)
.equ RAMEND, 0x08FF
.equ SPL, 0x3D
.equ SPH, 0x3E

.global main
.org 0x0000
    rjmp main

main:
    ; Inicializar pilha (Stack Pointer) usando sintaxe GNU (hi8/lo8)
    ldi r16, hi8(RAMEND)
    out SPH, r16
    ldi r16, lo8(RAMEND)
    out SPL, r16
    ; R1 deve ser zero para rotinas GCC
    clr r1

;  Linha 1
;  Linha 2
;  Linha 3
;  Linha 4
fim_programa:
    rjmp fim_programa
