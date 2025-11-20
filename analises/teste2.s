; Assembly AVR para Arduino Uno (ATmega328P)
; Gerado automaticamente

; Seção de dados
.data
X: .byte 2  ; 0x0100
Y: .byte 2  ; 0x0102
Z: .byte 2  ; 0x0104
PI: .byte 2  ; 0x0106
E: .byte 2  ; 0x0108
I: .byte 2  ; 0x010A
CONTADOR: .byte 2  ; 0x010C
A: .byte 2  ; 0x010E
B: .byte 2  ; 0x0110
C: .byte 2  ; 0x0112
D: .byte 2  ; 0x0114
F: .byte 2  ; 0x0116
N: .byte 2  ; 0x0118
SOMA: .byte 2  ; 0x011A
DELTA: .byte 2  ; 0x011C
R: .byte 2  ; 0x011E
AREA: .byte 2  ; 0x0120
TEMP: .byte 2  ; 0x0122
QUASE_VOL: .byte 2  ; 0x0124
VOLUME: .byte 2  ; 0x0126
FAT: .byte 2  ; 0x0128
LIMITE: .byte 2  ; 0x012A

; Seção de código
.text
; Prólogo do programa
.include "m328Pdef.inc"

.org 0x0000
    rjmp main

main:
    ; Inicializar pilha
    ldi r16, high(RAMEND)
    out SPH, r16
    ldi r16, low(RAMEND)
    out SPL, r16

    ; Inicializar registradores
    clr r1              ; R1 sempre zero (convenção AVR-GCC)

; Linha 1
    ; TAC: MEM[X] = 100
    ldi r16, 100
    sts X, r16  ; Armazenar em 0x0100

; Linha 2
    ; TAC: MEM[Y] = 50
    ldi r16, 50
    sts Y, r16  ; Armazenar em 0x0102

; Linha 3
    ; TAC: MEM[Z] = 25
    ldi r16, 25
    sts Z, r16  ; Armazenar em 0x0104

; Linha 4
    ; TAC: MEM[PI] = 3.14159
    ldi r16, 3
    sts PI, r16  ; Armazenar em 0x0106

; Linha 5
    ; TAC: MEM[E] = 2.71828
    ldi r16, 2
    sts E, r16  ; Armazenar em 0x0108

; Linha 6
    ; TAC: t6 = RES[4]
    ; AVISO: Instrução não mapeada: t6 = RES[4]
; Linha 7
    ; TAC: t7 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t8 = MEM[Y]
    lds r17, Y  ; Carregar de 0x0102

    ; TAC: t10 = MEM[Z]
    lds r18, Z  ; Carregar de 0x0104

; Linha 8
    ; TAC: t12 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

    ; TAC: t13 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

    ; TAC: t15 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

; Linha 9
    ; TAC: t17 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t20 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

; Linha 10
    ; TAC: t24 = MEM[PI]
    lds r16, PI  ; Carregar de 0x0106

; Linha 11
    ; TAC: t29 = MEM[E]
    lds r17, E  ; Carregar de 0x0108

    ; TAC: t30 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: t31 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

; Linha 12
    ; TAC: t34 = MEM[X]
    lds r20, X  ; Carregar de 0x0100

    ; TAC: t35 = MEM[Y]
    lds r21, Y  ; Carregar de 0x0102

    ; TAC: t37 = MEM[Z]
    lds r22, Z  ; Carregar de 0x0104

; Linha 13
    ; TAC: t41 = MEM[X]
    lds r23, X  ; Carregar de 0x0100

    ; TAC: t42 = MEM[Y]
    lds r16, Y  ; Carregar de 0x0102

    ; TAC: t44 = MEM[Z]
    lds r17, Z  ; Carregar de 0x0104

; Linha 14
    ; TAC: t46 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: t47 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t48 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

; Linha 15
    ; TAC: t53 = MEM[PI]
    lds r21, PI  ; Carregar de 0x0106

    ; TAC: t54 = MEM[E]
    lds r22, E  ; Carregar de 0x0108

    ; TAC: t55 = t53 > t54
    mov r23, r21
    cp r21, r22   ; Comparar r21 com r22
    cp r22, r21
    brlt cmp_true_2356826846192
    ldi r23, 0        ; Falso
    rjmp cmp_end_2356826846192
cmp_true_2356826846192:
    ldi r23, 1        ; Verdadeiro
cmp_end_2356826846192:

    ; TAC: ifFalse t55 goto L0
    cpi r23, 0         ; Comparar com zero
    breq L0         ; Saltar se zero (falso)

    ; TAC: goto L1
    rjmp L1

L0:
L1:
; Linha 16
    ; TAC: t59 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t60 = MEM[Y]
    lds r17, Y  ; Carregar de 0x0102

    ; TAC: t62 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t63 = MEM[Z]
    lds r19, Z  ; Carregar de 0x0104

; Linha 17
    ; TAC: t66 = MEM[X]
    lds r20, X  ; Carregar de 0x0100

    ; TAC: t67 = MEM[Y]
    lds r21, Y  ; Carregar de 0x0102

    ; TAC: t69 = MEM[Z]
    lds r22, Z  ; Carregar de 0x0104

; Linha 18
    ; TAC: t71 = MEM[X]
    lds r23, X  ; Carregar de 0x0100

; Linha 19
    ; TAC: t76 = MEM[Z]
    lds r16, Z  ; Carregar de 0x0104

; Linha 20
    ; TAC: t82 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t85 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

; Linha 21
    ; TAC: t88 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

    ; TAC: t89 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

    ; TAC: t91 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

; Linha 22
    ; TAC: t93 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t96 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

; Linha 23
    ; TAC: t100 = MEM[Z]
    lds r16, Z  ; Carregar de 0x0104

    ; TAC: t103 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

; Linha 24
    ; TAC: t107 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: t108 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t110 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

; Linha 25
; Linha 26
    ; TAC: t121 = MEM[X]
    lds r21, X  ; Carregar de 0x0100

    ; TAC: t122 = MEM[Y]
    lds r22, Y  ; Carregar de 0x0102

    ; TAC: t124 = MEM[Z]
    lds r23, Z  ; Carregar de 0x0104

; Linha 27
    ; TAC: t128 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t130 = t128 > 50
    ldi r25, 50
    mov r17, r16
    cp r16, r25   ; Comparar r16 com r25
    cp r25, r16
    brlt cmp_true_2356826842160
    ldi r17, 0        ; Falso
    rjmp cmp_end_2356826842160
cmp_true_2356826842160:
    ldi r17, 1        ; Verdadeiro
cmp_end_2356826842160:

    ; TAC: ifFalse t130 goto L2
    cpi r17, 0         ; Comparar com zero
    breq L2         ; Saltar se zero (falso)

    ; TAC: t132 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: goto L3
    rjmp L3

L2:
    ; TAC: t135 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

L3:
; Linha 28
    ; TAC: t138 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

    ; TAC: t139 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

    ; TAC: t140 = t138 == t139
    mov r22, r20
    cp r20, r21   ; Comparar r20 com r21
    breq cmp_true_2356826841968
    ldi r22, 0        ; Falso
    rjmp cmp_end_2356826841968
cmp_true_2356826841968:
    ldi r22, 1        ; Verdadeiro
cmp_end_2356826841968:

    ; TAC: ifFalse t140 goto L4
    cpi r22, 0         ; Comparar com zero
    breq L4         ; Saltar se zero (falso)

    ; TAC: goto L5
    rjmp L5

L4:
L5:
; Linha 29
    ; TAC: t144 = MEM[X]
    lds r23, X  ; Carregar de 0x0100

    ; TAC: t145 = MEM[Y]
    lds r16, Y  ; Carregar de 0x0102

    ; TAC: t146 = t144 > t145
    mov r17, r23
    cp r23, r16   ; Comparar r23 com r16
    cp r16, r23
    brlt cmp_true_2356826843744
    ldi r17, 0        ; Falso
    rjmp cmp_end_2356826843744
cmp_true_2356826843744:
    ldi r17, 1        ; Verdadeiro
cmp_end_2356826843744:

    ; TAC: ifFalse t146 goto L6
    cpi r17, 0         ; Comparar com zero
    breq L6         ; Saltar se zero (falso)

    ; TAC: t148 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: goto L7
    rjmp L7

L6:
    ; TAC: t149 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

L7:
; Linha 30
    ; TAC: t150 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

    ; TAC: t152 = t150 != 0
    ldi r25, 0
    mov r21, r20
    cp r20, r25   ; Comparar r20 com r25
    brne cmp_true_2356826845520
    ldi r21, 0        ; Falso
    rjmp cmp_end_2356826845520
cmp_true_2356826845520:
    ldi r21, 1        ; Verdadeiro
cmp_end_2356826845520:

    ; TAC: ifFalse t152 goto L8
    cpi r21, 0         ; Comparar com zero
    breq L8         ; Saltar se zero (falso)

    ; TAC: t154 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t155 = MEM[Z]
    lds r23, Z  ; Carregar de 0x0104

    ; TAC: goto L9
    rjmp L9

L8:
L9:
; Linha 31
    ; TAC: t158 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t159 = MEM[Y]
    lds r17, Y  ; Carregar de 0x0102

    ; TAC: t160 = t158 + t159
    mov r18, r16
    add r18, r17

    ; TAC: t162 = t160 < 100
    ldi r25, 100
    mov r19, r18
    cp r18, r25   ; Comparar r18 com r25
    brlt cmp_true_2356826848352
    ldi r19, 0        ; Falso
    rjmp cmp_end_2356826848352
cmp_true_2356826848352:
    ldi r19, 1        ; Verdadeiro
cmp_end_2356826848352:

    ; TAC: ifFalse t162 goto L10
    cpi r19, 0         ; Comparar com zero
    breq L10         ; Saltar se zero (falso)

    ; TAC: goto L11
    rjmp L11

L10:
L11:
; Linha 32
    ; TAC: MEM[I] = 0
    ldi r16, 0
    sts I, r16  ; Armazenar em 0x010A

; Linha 33
L12:
    ; TAC: t168 = MEM[I]
    lds r20, I  ; Carregar de 0x010A

    ; TAC: t170 = t168 < 10
    ldi r25, 10
    mov r21, r20
    cp r20, r25   ; Comparar r20 com r25
    brlt cmp_true_2356826839520
    ldi r21, 0        ; Falso
    rjmp cmp_end_2356826839520
cmp_true_2356826839520:
    ldi r21, 1        ; Verdadeiro
cmp_end_2356826839520:

    ; TAC: ifFalse t170 goto L13
    cpi r21, 0         ; Comparar com zero
    breq L13         ; Saltar se zero (falso)

    ; TAC: t171 = MEM[I]
    lds r22, I  ; Carregar de 0x010A

    ; TAC: t173 = t171 + 1
    ldi r25, 1
    mov r23, r22
    add r23, r25

    ; TAC: MEM[I] = t173
    sts I, r23  ; Armazenar em 0x010A

    ; TAC: goto L12
    rjmp L12

L13:
; Linha 34
    ; TAC: t174 = MEM[I]
    lds r16, I  ; Carregar de 0x010A

; Linha 35
    ; TAC: MEM[CONTADOR] = 1
    ldi r16, 1
    sts CONTADOR, r16  ; Armazenar em 0x010C

; Linha 36
L14:
    ; TAC: t177 = MEM[CONTADOR]
    lds r17, CONTADOR  ; Carregar de 0x010C

    ; TAC: t179 = t177 <= 5
    ldi r25, 5
    mov r18, r17
    cp r17, r25   ; Comparar r17 com r25
    brge cmp_true_2356826848832
    ldi r18, 0        ; Falso
    rjmp cmp_end_2356826848832
cmp_true_2356826848832:
    ldi r18, 1        ; Verdadeiro
cmp_end_2356826848832:

    ; TAC: ifFalse t179 goto L15
    cpi r18, 0         ; Comparar com zero
    breq L15         ; Saltar se zero (falso)

    ; TAC: t180 = MEM[CONTADOR]
    lds r19, CONTADOR  ; Carregar de 0x010C

    ; TAC: t182 = t180 * 2
    ldi r25, 2
    mov r20, r19
    mul r19, r25  ; Mult 8x8=16 bits em R1:R0
    mov r20, r0       ; Pegar byte baixo

    ; TAC: MEM[CONTADOR] = t182
    sts CONTADOR, r20  ; Armazenar em 0x010C

    ; TAC: goto L14
    rjmp L14

L15:
; Linha 37
    ; TAC: t183 = MEM[CONTADOR]
    lds r21, CONTADOR  ; Carregar de 0x010C

; Linha 38
; Linha 39
    ; TAC: t191 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t192 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

; Linha 40
    ; TAC: t196 = MEM[PI]
    lds r16, PI  ; Carregar de 0x0106

    ; TAC: t199 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

; Linha 41
    ; TAC: t201 = MEM[E]
    lds r18, E  ; Carregar de 0x0108

    ; TAC: t202 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

; Linha 42
    ; TAC: t206 = MEM[X]
    lds r20, X  ; Carregar de 0x0100

    ; TAC: t207 = MEM[Y]
    lds r21, Y  ; Carregar de 0x0102

    ; TAC: t209 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t210 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

; Linha 43
    ; TAC: t213 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t216 = MEM[Y]
    lds r17, Y  ; Carregar de 0x0102

; Linha 44
    ; TAC: t222 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: t223 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t225 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

    ; TAC: t226 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

; Linha 45
    ; TAC: t229 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

    ; TAC: t232 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

    ; TAC: t236 = MEM[Z]
    lds r16, Z  ; Carregar de 0x0104

; Linha 46
    ; TAC: t240 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t241 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t243 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

    ; TAC: t244 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

; Linha 47
    ; TAC: t247 = MEM[X]
    lds r21, X  ; Carregar de 0x0100

    ; TAC: t248 = MEM[Y]
    lds r22, Y  ; Carregar de 0x0102

    ; TAC: t250 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

    ; TAC: t251 = MEM[Z]
    lds r16, Z  ; Carregar de 0x0104

; Linha 48
    ; TAC: t254 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t255 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t257 = MEM[Z]
    lds r19, Z  ; Carregar de 0x0104

; Linha 49
    ; TAC: t261 = MEM[X]
    lds r20, X  ; Carregar de 0x0100

    ; TAC: t264 = MEM[Y]
    lds r21, Y  ; Carregar de 0x0102

    ; TAC: t268 = MEM[Z]
    lds r22, Z  ; Carregar de 0x0104

; Linha 50
    ; TAC: t272 = MEM[PI]
    lds r23, PI  ; Carregar de 0x0106

    ; TAC: t273 = MEM[X]
    lds r16, X  ; Carregar de 0x0100

    ; TAC: t277 = MEM[E]
    lds r17, E  ; Carregar de 0x0108

    ; TAC: t278 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

; Linha 51
    ; TAC: t283 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

    ; TAC: t284 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

    ; TAC: t286 = MEM[Y]
    lds r21, Y  ; Carregar de 0x0102

    ; TAC: t287 = MEM[Z]
    lds r22, Z  ; Carregar de 0x0104

; Linha 52
    ; TAC: t290 = MEM[X]
    lds r23, X  ; Carregar de 0x0100

    ; TAC: t293 = MEM[Y]
    lds r16, Y  ; Carregar de 0x0102

; Linha 53
    ; TAC: t297 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t298 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t302 = MEM[Z]
    lds r19, Z  ; Carregar de 0x0104

    ; TAC: t303 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

; Linha 54
    ; TAC: t308 = MEM[X]
    lds r21, X  ; Carregar de 0x0100

    ; TAC: t311 = MEM[Y]
    lds r22, Y  ; Carregar de 0x0102

; Linha 55
    ; TAC: MEM[A] = 1
    ldi r16, 1
    sts A, r16  ; Armazenar em 0x010E

; Linha 56
    ; TAC: MEM[B] = 2
    ldi r16, 2
    sts B, r16  ; Armazenar em 0x0110

; Linha 57
    ; TAC: MEM[C] = 3
    ldi r16, 3
    sts C, r16  ; Armazenar em 0x0112

; Linha 58
    ; TAC: MEM[D] = 4
    ldi r16, 4
    sts D, r16  ; Armazenar em 0x0114

; Linha 59
    ; TAC: MEM[F] = 5
    ldi r16, 5
    sts F, r16  ; Armazenar em 0x0116

; Linha 60
    ; TAC: t322 = MEM[A]
    lds r23, A  ; Carregar de 0x010E

    ; TAC: t323 = MEM[B]
    lds r16, B  ; Carregar de 0x0110

    ; TAC: t325 = MEM[C]
    lds r17, C  ; Carregar de 0x0112

    ; TAC: t327 = MEM[D]
    lds r18, D  ; Carregar de 0x0114

    ; TAC: t329 = MEM[F]
    lds r19, F  ; Carregar de 0x0116

; Linha 61
    ; TAC: t331 = MEM[A]
    lds r20, A  ; Carregar de 0x010E

    ; TAC: t332 = MEM[B]
    lds r21, B  ; Carregar de 0x0110

    ; TAC: t334 = MEM[C]
    lds r22, C  ; Carregar de 0x0112

    ; TAC: t336 = MEM[D]
    lds r23, D  ; Carregar de 0x0114

    ; TAC: t338 = MEM[F]
    lds r16, F  ; Carregar de 0x0116

; Linha 62
    ; TAC: t340 = MEM[F]
    lds r17, F  ; Carregar de 0x0116

    ; TAC: t341 = MEM[D]
    lds r18, D  ; Carregar de 0x0114

    ; TAC: t343 = MEM[C]
    lds r19, C  ; Carregar de 0x0112

    ; TAC: t345 = MEM[B]
    lds r20, B  ; Carregar de 0x0110

    ; TAC: t347 = MEM[A]
    lds r21, A  ; Carregar de 0x010E

; Linha 63
    ; TAC: t349 = MEM[A]
    lds r22, A  ; Carregar de 0x010E

    ; TAC: t350 = MEM[B]
    lds r23, B  ; Carregar de 0x0110

    ; TAC: t352 = MEM[C]
    lds r16, C  ; Carregar de 0x0112

    ; TAC: t354 = MEM[D]
    lds r17, D  ; Carregar de 0x0114

    ; TAC: t356 = MEM[F]
    lds r18, F  ; Carregar de 0x0116

; Linha 64
    ; TAC: t358 = MEM[A]
    lds r19, A  ; Carregar de 0x010E

    ; TAC: t359 = MEM[B]
    lds r20, B  ; Carregar de 0x0110

    ; TAC: t360 = t358 < t359
    mov r21, r19
    cp r19, r20   ; Comparar r19 com r20
    brlt cmp_true_2356827523664
    ldi r21, 0        ; Falso
    rjmp cmp_end_2356827523664
cmp_true_2356827523664:
    ldi r21, 1        ; Verdadeiro
cmp_end_2356827523664:

    ; TAC: ifFalse t360 goto L16
    cpi r21, 0         ; Comparar com zero
    breq L16         ; Saltar se zero (falso)

    ; TAC: t362 = MEM[C]
    lds r22, C  ; Carregar de 0x0112

    ; TAC: t363 = MEM[D]
    lds r23, D  ; Carregar de 0x0114

    ; TAC: t364 = t362 < t363
    mov r16, r22
    cp r22, r23   ; Comparar r22 com r23
    brlt cmp_true_2356827523952
    ldi r16, 0        ; Falso
    rjmp cmp_end_2356827523952
cmp_true_2356827523952:
    ldi r16, 1        ; Verdadeiro
cmp_end_2356827523952:

    ; TAC: ifFalse t364 goto L18
    cpi r16, 0         ; Comparar com zero
    breq L18         ; Saltar se zero (falso)

    ; TAC: goto L19
    rjmp L19

L18:
L19:
    ; TAC: goto L17
    rjmp L17

L16:
L17:
; Linha 65
    ; TAC: t369 = MEM[A]
    lds r17, A  ; Carregar de 0x010E

    ; TAC: t371 = t369 > 0
    ldi r25, 0
    mov r18, r17
    cp r17, r25   ; Comparar r17 com r25
    cp r25, r17
    brlt cmp_true_2356827524288
    ldi r18, 0        ; Falso
    rjmp cmp_end_2356827524288
cmp_true_2356827524288:
    ldi r18, 1        ; Verdadeiro
cmp_end_2356827524288:

    ; TAC: ifFalse t371 goto L20
    cpi r18, 0         ; Comparar com zero
    breq L20         ; Saltar se zero (falso)

    ; TAC: t373 = MEM[B]
    lds r19, B  ; Carregar de 0x0110

    ; TAC: t375 = t373 > 0
    ldi r25, 0
    mov r20, r19
    cp r19, r25   ; Comparar r19 com r25
    cp r25, r19
    brlt cmp_true_2356827524480
    ldi r20, 0        ; Falso
    rjmp cmp_end_2356827524480
cmp_true_2356827524480:
    ldi r20, 1        ; Verdadeiro
cmp_end_2356827524480:

    ; TAC: ifFalse t375 goto L22
    cpi r20, 0         ; Comparar com zero
    breq L22         ; Saltar se zero (falso)

    ; TAC: t377 = MEM[A]
    lds r21, A  ; Carregar de 0x010E

    ; TAC: t378 = MEM[B]
    lds r22, B  ; Carregar de 0x0110

    ; TAC: goto L23
    rjmp L23

L22:
    ; TAC: t380 = MEM[A]
    lds r23, A  ; Carregar de 0x010E

    ; TAC: t381 = MEM[B]
    lds r16, B  ; Carregar de 0x0110

L23:
    ; TAC: goto L21
    rjmp L21

L20:
L21:
; Linha 66
; Linha 67
; Linha 68
; Linha 69
; Linha 70
; Linha 71
    ; TAC: t400 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

; Linha 72
    ; TAC: t403 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t404 = MEM[Z]
    lds r19, Z  ; Carregar de 0x0104

; Linha 73
    ; TAC: t407 = MEM[A]
    lds r20, A  ; Carregar de 0x010E

    ; TAC: t408 = MEM[B]
    lds r21, B  ; Carregar de 0x0110

; Linha 74
    ; TAC: t412 = MEM[A]
    lds r22, A  ; Carregar de 0x010E

    ; TAC: t413 = MEM[B]
    lds r23, B  ; Carregar de 0x0110

    ; TAC: t415 = MEM[C]
    lds r16, C  ; Carregar de 0x0112

; Linha 75
    ; TAC: t417 = MEM[A]
    lds r17, A  ; Carregar de 0x010E

    ; TAC: t418 = MEM[B]
    lds r18, B  ; Carregar de 0x0110

    ; TAC: t420 = MEM[C]
    lds r19, C  ; Carregar de 0x0112

; Linha 76
    ; TAC: t422 = MEM[A]
    lds r20, A  ; Carregar de 0x010E

    ; TAC: t423 = MEM[B]
    lds r21, B  ; Carregar de 0x0110

    ; TAC: t425 = MEM[C]
    lds r22, C  ; Carregar de 0x0112

    ; TAC: t427 = MEM[D]
    lds r23, D  ; Carregar de 0x0114

; Linha 77
    ; TAC: t429 = MEM[A]
    lds r16, A  ; Carregar de 0x010E

    ; TAC: t430 = MEM[B]
    lds r17, B  ; Carregar de 0x0110

    ; TAC: t432 = MEM[C]
    lds r18, C  ; Carregar de 0x0112

    ; TAC: t434 = MEM[D]
    lds r19, D  ; Carregar de 0x0114

; Linha 78
    ; TAC: MEM[N] = 10
    ldi r16, 10
    sts N, r16  ; Armazenar em 0x0118

; Linha 79
L24:
    ; TAC: t438 = MEM[N]
    lds r20, N  ; Carregar de 0x0118

    ; TAC: t440 = t438 > 0
    ldi r25, 0
    mov r21, r20
    cp r20, r25   ; Comparar r20 com r25
    cp r25, r20
    brlt cmp_true_2356827527120
    ldi r21, 0        ; Falso
    rjmp cmp_end_2356827527120
cmp_true_2356827527120:
    ldi r21, 1        ; Verdadeiro
cmp_end_2356827527120:

    ; TAC: ifFalse t440 goto L25
    cpi r21, 0         ; Comparar com zero
    breq L25         ; Saltar se zero (falso)

    ; TAC: t441 = MEM[N]
    lds r22, N  ; Carregar de 0x0118

    ; TAC: t443 = t441 - 1
    ldi r25, 1
    mov r23, r22
    sub r23, r25

    ; TAC: MEM[N] = t443
    sts N, r23  ; Armazenar em 0x0118

    ; TAC: goto L24
    rjmp L24

L25:
; Linha 80
    ; TAC: t444 = MEM[N]
    lds r16, N  ; Carregar de 0x0118

; Linha 81
    ; TAC: MEM[SOMA] = 0
    ldi r16, 0
    sts SOMA, r16  ; Armazenar em 0x011A

; Linha 82
    ; TAC: MEM[I] = 1
    ldi r16, 1
    sts I, r16  ; Armazenar em 0x010A

; Linha 83
L26:
    ; TAC: t448 = MEM[I]
    lds r17, I  ; Carregar de 0x010A

    ; TAC: t450 = t448 <= 10
    ldi r25, 10
    mov r18, r17
    cp r17, r25   ; Comparar r17 com r25
    brge cmp_true_2356827527840
    ldi r18, 0        ; Falso
    rjmp cmp_end_2356827527840
cmp_true_2356827527840:
    ldi r18, 1        ; Verdadeiro
cmp_end_2356827527840:

    ; TAC: ifFalse t450 goto L27
    cpi r18, 0         ; Comparar com zero
    breq L27         ; Saltar se zero (falso)

    ; TAC: t451 = MEM[SOMA]
    lds r19, SOMA  ; Carregar de 0x011A

    ; TAC: t452 = MEM[I]
    lds r20, I  ; Carregar de 0x010A

    ; TAC: t453 = t451 + t452
    mov r21, r19
    add r21, r20

    ; TAC: MEM[SOMA] = t453
    sts SOMA, r21  ; Armazenar em 0x011A

    ; TAC: t454 = MEM[I]
    lds r22, I  ; Carregar de 0x010A

    ; TAC: t456 = t454 + 1
    ldi r25, 1
    mov r23, r22
    add r23, r25

    ; TAC: MEM[I] = t456
    sts I, r23  ; Armazenar em 0x010A

    ; TAC: goto L26
    rjmp L26

L27:
; Linha 84
    ; TAC: t458 = MEM[SOMA]
    lds r16, SOMA  ; Carregar de 0x011A

; Linha 85
    ; TAC: t459 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t460 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t462 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t464 = MEM[X]
    lds r20, X  ; Carregar de 0x0100

; Linha 86
    ; TAC: t466 = MEM[X]
    lds r21, X  ; Carregar de 0x0100

    ; TAC: t467 = MEM[Y]
    lds r22, Y  ; Carregar de 0x0102

    ; TAC: t469 = MEM[Y]
    lds r23, Y  ; Carregar de 0x0102

; Linha 87
; Linha 88
    ; TAC: t480 = MEM[PI]
    lds r16, PI  ; Carregar de 0x0106

; Linha 89
    ; TAC: t486 = MEM[PI]
    lds r17, PI  ; Carregar de 0x0106

; Linha 90
; Linha 91
; Linha 92
    ; TAC: t500 = MEM[X]
    lds r18, X  ; Carregar de 0x0100

    ; TAC: t501 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t502 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

; Linha 93
    ; TAC: t505 = MEM[A]
    lds r21, A  ; Carregar de 0x010E

    ; TAC: t506 = MEM[B]
    lds r22, B  ; Carregar de 0x0110

    ; TAC: t510 = MEM[C]
    lds r23, C  ; Carregar de 0x0112

    ; TAC: t511 = MEM[D]
    lds r16, D  ; Carregar de 0x0114

; Linha 94
    ; TAC: t518 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t519 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

    ; TAC: t521 = MEM[Y]
    lds r19, Y  ; Carregar de 0x0102

    ; TAC: t522 = MEM[Z]
    lds r20, Z  ; Carregar de 0x0104

    ; TAC: t525 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

    ; TAC: t526 = MEM[X]
    lds r22, X  ; Carregar de 0x0100

; Linha 95
    ; TAC: t529 = MEM[PI]
    lds r23, PI  ; Carregar de 0x0106

    ; TAC: t530 = MEM[E]
    lds r16, E  ; Carregar de 0x0108

    ; TAC: t532 = MEM[E]
    lds r17, E  ; Carregar de 0x0108

    ; TAC: t533 = MEM[PI]
    lds r18, PI  ; Carregar de 0x0106

; Linha 96
    ; TAC: t536 = MEM[A]
    lds r19, A  ; Carregar de 0x010E

    ; TAC: t537 = MEM[B]
    lds r20, B  ; Carregar de 0x0110

    ; TAC: t539 = MEM[C]
    lds r21, C  ; Carregar de 0x0112

    ; TAC: t541 = MEM[D]
    lds r22, D  ; Carregar de 0x0114

    ; TAC: t542 = MEM[F]
    lds r23, F  ; Carregar de 0x0116

    ; TAC: t544 = MEM[A]
    lds r16, A  ; Carregar de 0x010E

; Linha 97
    ; TAC: MEM[A] = 1.0
    ldi r16, 1
    sts A, r16  ; Armazenar em 0x010E

; Linha 98
    ; TAC: MEM[B] = 5.0
    ldi r16, 5
    sts B, r16  ; Armazenar em 0x0110

; Linha 99
    ; TAC: MEM[C] = 2.0
    ldi r16, 2
    sts C, r16  ; Armazenar em 0x0112

; Linha 100
    ; TAC: t550 = MEM[B]
    lds r17, B  ; Carregar de 0x0110

    ; TAC: t551 = MEM[B]
    lds r18, B  ; Carregar de 0x0110

    ; TAC: t554 = MEM[A]
    lds r19, A  ; Carregar de 0x010E

; Linha 101
    ; TAC: t557 = MEM[DELTA]
    lds r20, DELTA  ; Carregar de 0x011C

    ; TAC: t558 = RES[t557]
    ; RES[t557] - histórico não implementado
    ldi r21, 0    ; Placeholder

; Linha 102
; Linha 103
; Linha 104
; Linha 105
; Linha 106
; Linha 107
    ; TAC: t564 = MEM[DELTA]
    lds r22, DELTA  ; Carregar de 0x011C

    ; TAC: t566 = t564 < 0
    ldi r25, 0
    mov r23, r22
    cp r22, r25   ; Comparar r22 com r25
    brlt cmp_true_2356827532160
    ldi r23, 0        ; Falso
    rjmp cmp_end_2356827532160
cmp_true_2356827532160:
    ldi r23, 1        ; Verdadeiro
cmp_end_2356827532160:

    ; TAC: ifFalse t566 goto L28
    cpi r23, 0         ; Comparar com zero
    breq L28         ; Saltar se zero (falso)

    ; TAC: goto L29
    rjmp L29

L28:
L29:
; Linha 108
    ; TAC: MEM[R] = 10
    ldi r16, 10
    sts R, r16  ; Armazenar em 0x011E

; Linha 109
    ; TAC: MEM[PI] = 3.14159
    ldi r16, 3
    sts PI, r16  ; Armazenar em 0x0106

; Linha 110
    ; TAC: t572 = MEM[PI]
    lds r16, PI  ; Carregar de 0x0106

    ; TAC: t573 = MEM[R]
    lds r17, R  ; Carregar de 0x011E

    ; TAC: t575 = MEM[R]
    lds r18, R  ; Carregar de 0x011E

; Linha 111
    ; TAC: t577 = MEM[AREA]
    lds r19, AREA  ; Carregar de 0x0120

    ; TAC: t578 = RES[t577]
    ; RES[t577] - histórico não implementado
    ldi r20, 0    ; Placeholder

; Linha 112
    ; TAC: t582 = MEM[PI]
    lds r21, PI  ; Carregar de 0x0106

; Linha 113
    ; TAC: t584 = MEM[TEMP]
    lds r22, TEMP  ; Carregar de 0x0122

    ; TAC: t585 = RES[t584]
    ; RES[t584] - histórico não implementado
    ldi r23, 0    ; Placeholder

; Linha 114
    ; TAC: t586 = MEM[TEMP]
    lds r16, TEMP  ; Carregar de 0x0122

    ; TAC: t587 = MEM[R]
    lds r17, R  ; Carregar de 0x011E

    ; TAC: t589 = MEM[R]
    lds r18, R  ; Carregar de 0x011E

; Linha 115
    ; TAC: t591 = MEM[QUASE_VOL]
    lds r19, QUASE_VOL  ; Carregar de 0x0124

    ; TAC: t592 = RES[t591]
    ; RES[t591] - histórico não implementado
    ldi r20, 0    ; Placeholder

; Linha 116
    ; TAC: t593 = MEM[QUASE_VOL]
    lds r21, QUASE_VOL  ; Carregar de 0x0124

    ; TAC: t594 = MEM[R]
    lds r22, R  ; Carregar de 0x011E

; Linha 117
    ; TAC: t596 = MEM[VOLUME]
    lds r23, VOLUME  ; Carregar de 0x0126

    ; TAC: t597 = RES[t596]
    ; RES[t596] - histórico não implementado
    ldi r16, 0    ; Placeholder

; Linha 118
    ; TAC: MEM[X] = 10
    ldi r16, 10
    sts X, r16  ; Armazenar em 0x0100

; Linha 119
    ; TAC: MEM[Y] = 20
    ldi r16, 20
    sts Y, r16  ; Armazenar em 0x0102

; Linha 120
    ; TAC: MEM[Z] = 30
    ldi r16, 30
    sts Z, r16  ; Armazenar em 0x0104

; Linha 121
    ; TAC: t601 = MEM[X]
    lds r17, X  ; Carregar de 0x0100

    ; TAC: t602 = MEM[Y]
    lds r18, Y  ; Carregar de 0x0102

; Linha 122
    ; TAC: t604 = MEM[X]
    lds r19, X  ; Carregar de 0x0100

    ; TAC: t605 = MEM[Y]
    lds r20, Y  ; Carregar de 0x0102

; Linha 123
    ; TAC: t607 = MEM[Z]
    lds r21, Z  ; Carregar de 0x0104

    ; TAC: t609 = RES[1]
    ; AVISO: Instrução não mapeada: t609 = RES[1]
; Linha 124
    ; TAC: t611 = MEM[Z]
    lds r22, Z  ; Carregar de 0x0104

    ; TAC: t613 = RES[2]
    ; AVISO: Instrução não mapeada: t613 = RES[2]
; Linha 125
    ; TAC: t615 = MEM[X]
    lds r23, X  ; Carregar de 0x0100

    ; TAC: t616 = MEM[Y]
    lds r16, Y  ; Carregar de 0x0102

    ; TAC: t618 = MEM[Z]
    lds r17, Z  ; Carregar de 0x0104

    ; TAC: t622 = MEM[A]
    lds r18, A  ; Carregar de 0x010E

    ; TAC: t623 = MEM[B]
    lds r19, B  ; Carregar de 0x0110

    ; TAC: t625 = MEM[C]
    lds r20, C  ; Carregar de 0x0112

; Linha 126
    ; TAC: MEM[I] = 5
    ldi r16, 5
    sts I, r16  ; Armazenar em 0x010A

; Linha 127
    ; TAC: MEM[FAT] = 1
    ldi r16, 1
    sts FAT, r16  ; Armazenar em 0x0128

; Linha 128
L30:
    ; TAC: t633 = MEM[I]
    lds r21, I  ; Carregar de 0x010A

    ; TAC: t635 = t633 > 0
    ldi r25, 0
    mov r22, r21
    cp r21, r25   ; Comparar r21 com r25
    cp r25, r21
    brlt cmp_true_2356827535472
    ldi r22, 0        ; Falso
    rjmp cmp_end_2356827535472
cmp_true_2356827535472:
    ldi r22, 1        ; Verdadeiro
cmp_end_2356827535472:

    ; TAC: ifFalse t635 goto L31
    cpi r22, 0         ; Comparar com zero
    breq L31         ; Saltar se zero (falso)

    ; TAC: t636 = MEM[FAT]
    lds r23, FAT  ; Carregar de 0x0128

    ; TAC: t637 = MEM[I]
    lds r16, I  ; Carregar de 0x010A

    ; TAC: t638 = t636 * t637
    mov r17, r23
    mul r23, r16  ; Mult 8x8=16 bits em R1:R0
    mov r17, r0       ; Pegar byte baixo

    ; TAC: MEM[FAT] = t638
    sts FAT, r17  ; Armazenar em 0x0128

    ; TAC: t639 = MEM[I]
    lds r18, I  ; Carregar de 0x010A

    ; TAC: t641 = t639 - 1
    ldi r25, 1
    mov r19, r18
    sub r19, r25

    ; TAC: MEM[I] = t641
    sts I, r19  ; Armazenar em 0x010A

    ; TAC: goto L30
    rjmp L30

L31:
; Linha 129
    ; TAC: t643 = MEM[FAT]
    lds r20, FAT  ; Carregar de 0x0128

; Linha 130
    ; TAC: t644 = MEM[FAT]
    lds r21, FAT  ; Carregar de 0x0128

    ; TAC: t646 = t644 > 100
    ldi r25, 100
    mov r22, r21
    cp r21, r25   ; Comparar r21 com r25
    cp r25, r21
    brlt cmp_true_2356827536336
    ldi r22, 0        ; Falso
    rjmp cmp_end_2356827536336
cmp_true_2356827536336:
    ldi r22, 1        ; Verdadeiro
cmp_end_2356827536336:

    ; TAC: ifFalse t646 goto L32
    cpi r22, 0         ; Comparar com zero
    breq L32         ; Saltar se zero (falso)

    ; TAC: t648 = MEM[AREA]
    lds r23, AREA  ; Carregar de 0x0120

    ; TAC: goto L33
    rjmp L33

L32:
    ; TAC: t649 = MEM[VOLUME]
    lds r16, VOLUME  ; Carregar de 0x0126

L33:
; Linha 131
    ; TAC: MEM[LIMITE] = 100
    ldi r16, 100
    sts LIMITE, r16  ; Armazenar em 0x012A

; Linha 132
    ; TAC: MEM[CONTADOR] = 0
    ldi r16, 0
    sts CONTADOR, r16  ; Armazenar em 0x010C

; Linha 133
    ; TAC: MEM[SOMA] = 0
    ldi r16, 0
    sts SOMA, r16  ; Armazenar em 0x011A

; Linha 134
L34:
    ; TAC: t654 = MEM[CONTADOR]
    lds r17, CONTADOR  ; Carregar de 0x010C

    ; TAC: t655 = MEM[LIMITE]
    lds r18, LIMITE  ; Carregar de 0x012A

    ; TAC: t656 = t654 < t655
    mov r19, r17
    cp r17, r18   ; Comparar r17 com r18
    brlt cmp_true_2356827537008
    ldi r19, 0        ; Falso
    rjmp cmp_end_2356827537008
cmp_true_2356827537008:
    ldi r19, 1        ; Verdadeiro
cmp_end_2356827537008:

    ; TAC: ifFalse t656 goto L35
    cpi r19, 0         ; Comparar com zero
    breq L35         ; Saltar se zero (falso)

    ; TAC: t657 = MEM[SOMA]
    lds r20, SOMA  ; Carregar de 0x011A

    ; TAC: t658 = MEM[CONTADOR]
    lds r21, CONTADOR  ; Carregar de 0x010C

    ; TAC: t659 = t657 + t658
    mov r22, r20
    add r22, r21

    ; TAC: MEM[SOMA] = t659
    sts SOMA, r22  ; Armazenar em 0x011A

    ; TAC: goto L34
    rjmp L34

L35:
; Linha 135
    ; TAC: t660 = MEM[SOMA]
    lds r23, SOMA  ; Carregar de 0x011A

; Linha 136
    ; TAC: t661 = MEM[SOMA]
    lds r16, SOMA  ; Carregar de 0x011A

    ; TAC: t664 = MEM[FAT]
    lds r17, FAT  ; Carregar de 0x0128


fim:
    ; Loop infinito no final
    rjmp fim

