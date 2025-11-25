# Relatório de Otimizações de Código

**Gerado automaticamente pelo otimizador TAC**

## Estatísticas

- **Instruções originais:** 1113
- **Instruções otimizadas:** 789
- **Redução:** 324 instruções (29.1%)

## Otimizações Aplicadas

### Constant Folding

**Aplicações:** 69

**Descrição:** Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

### Constant Propagation

**Aplicações:** 326

**Descrição:** Propaga valores constantes através do código.

**Exemplo:**
```
Antes: t1 = 5
       t2 = t1 + 3
Depois: t1 = 5
        t2 = 5 + 3
        (que será reduzido para t2 = 8)
```

### Dead Code Elimination

**Aplicações:** 324

**Descrição:** Remove código que não afeta o resultado do programa.

**IMPORTANTE:** Preserva instruções com efeitos colaterais (PRINT, MEM, RES).

**Exemplo:**
```
Antes: t1 = 5
       t2 = 3  # t2 nunca é usado
       t3 = t1 + 2
Depois: t1 = 5
        t3 = t1 + 2
```

### Redundant Jumps

**Aplicações:** 0

**Descrição:** Remove saltos para a próxima instrução.

**Exemplo:**
```
Antes: goto L1
       L1:
Depois: L1:
```

## Comparação de Código

### TAC Original

```
# Linha 1
t0 = 100
MEM[X] = t0
HIST[t0]
# Linha 2
t1 = 50
MEM[Y] = t1
HIST[t1]
# Linha 3
t2 = 25
MEM[Z] = t2
HIST[t2]
# Linha 4
t3 = 3.14159
MEM[PI] = t3
HIST[t3]
# Linha 5
t4 = 2.71828
MEM[E] = t4
HIST[t4]
# Linha 6
t5 = 4
t6 = RES[t5]
HIST[t6]
t7 = PRINT[t6]
# Linha 7
t8 = MEM[X]
t9 = MEM[Y]
t10 = t8 + t9
t11 = MEM[Z]
t12 = t10 - t11
HIST[t12]
t13 = PRINT[t12]
# Linha 8
t14 = MEM[X]
t15 = MEM[Y]
t16 = t14 * t15
t17 = MEM[Z]
t18 = t16 / t17
HIST[t18]
t19 = PRINT[t18]
# Linha 9
t20 = MEM[X]
t21 = 2
t22 = t20 ^ t21
t23 = MEM[Y]
t24 = 2
t25 = t23 ^ t24
t26 = t22 + t25
HIST[t26]
t27 = PRINT[t26]
# Linha 10
t28 = MEM[PI]
t29 = 2
t30 = t28 * t29
t31 = 10
t32 = t30 ^ t31
HIST[t32]
t33 = PRINT[t32]
# Linha 11
t34 = MEM[E]
t35 = MEM[X]
t36 = MEM[Y]
t37 = t35 | t36
t38 = t34 + t37
HIST[t38]
t39 = PRINT[t38]
# Linha 12
t40 = MEM[X]
t41 = MEM[Y]
t42 = t40 + t41
t43 = MEM[Z]
t44 = t42 > t43
HIST[t44]
t45 = PRINT[t44]
# Linha 13
t46 = MEM[X]
t47 = MEM[Y]
t48 = MEM[Z]
t49 = t47 + t48
t50 = t46 + t49
t51 = 100
t52 = t50 >= t51
HIST[t52]
t53 = PRINT[t52]
# Linha 14
t54 = MEM[PI]
t55 = MEM[E]
t56 = t54 > t55
ifFalse t56 goto L0
t58 = 1
t57 = t58
goto L1
L0:
t59 = 0
t57 = t59
L1:
HIST[t57]
# Linha 15
t60 = MEM[X]
t61 = MEM[Y]
t62 = t60 ^ t61
t63 = MEM[Z]
t64 = t62 % t63
HIST[t64]
t65 = PRINT[t64]
# Linha 16
t66 = MEM[Z]
t67 = 4
t68 = t66 / t67
t69 = MEM[X]
t70 = 5
t71 = t69 | t70
t72 = t68 - t71
HIST[t72]
t73 = PRINT[t72]
# Linha 17
t74 = MEM[X]
t75 = MEM[Y]
t76 = t74 / t75
t77 = MEM[Z]
t78 = t76 | t77
t79 = 2
t80 = t78 * t79
HIST[t80]
t81 = PRINT[t80]
# Linha 18
t82 = MEM[X]
t83 = MEM[Y]
t84 = t82 | t83
t85 = MEM[Z]
t86 = 2
t87 = t85 / t86
t88 = t84 - t87
HIST[t88]
t89 = PRINT[t88]
# Linha 19
t90 = MEM[X]
t91 = 50
t92 = t90 > t91
ifFalse t92 goto L2
t94 = MEM[X]
t95 = 10
t96 = t94 - t95
t93 = t96
goto L3
L2:
t97 = MEM[X]
t98 = 10
t99 = t97 + t98
t93 = t99
L3:
HIST[t93]
# Linha 20
t100 = MEM[Y]
t101 = MEM[Z]
t102 = t100 == t101
ifFalse t102 goto L4
t104 = 1
t103 = t104
goto L5
L4:
t105 = -1
t103 = t105
L5:
HIST[t103]
# Linha 21
t106 = 0
MEM[I] = t106
HIST[t106]
# Linha 22
L6:
t108 = MEM[I]
t109 = 10
t110 = t108 < t109
ifFalse t110 goto L7
t111 = MEM[I]
t112 = 1
t113 = t111 + t112
MEM[I] = t113
t107 = t113
goto L6
L7:
HIST[t107]
# Linha 23
t114 = MEM[I]
HIST[t114]
t115 = PRINT[t114]
# Linha 24
t116 = 1
MEM[CONTADOR] = t116
HIST[t116]
# Linha 25
L8:
t118 = MEM[CONTADOR]
t119 = 5
t120 = t118 <= t119
ifFalse t120 goto L9
t121 = MEM[CONTADOR]
t122 = 2
t123 = t121 * t122
MEM[CONTADOR] = t123
t117 = t123
goto L8
L9:
HIST[t117]
# Linha 26
t124 = MEM[CONTADOR]
HIST[t124]
t125 = PRINT[t124]
# Linha 27
t126 = 10
t127 = 20
t128 = t126 + t127
t129 = 5
t130 = t128 * t129
t131 = 2
t132 = t130 - t131
HIST[t132]
t133 = PRINT[t132]
# Linha 28
t134 = MEM[X]
t135 = MEM[Y]
t136 = t134 + t135
t137 = 2
t138 = t136 / t137
HIST[t138]
t139 = PRINT[t138]
# Linha 29
t140 = MEM[PI]
t141 = 2
t142 = t140 * t141
t143 = MEM[X]
t144 = t142 * t143
HIST[t144]
t145 = PRINT[t144]
# Linha 30
t146 = MEM[X]
t147 = MEM[Y]
t148 = t146 / t147
t149 = MEM[Y]
t150 = MEM[Z]
t151 = t149 / t150
t152 = t148 * t151
HIST[t152]
t153 = PRINT[t152]
# Linha 31
t154 = 1
MEM[A] = t154
HIST[t154]
# Linha 32
t155 = 3
MEM[C] = t155
HIST[t155]
# Linha 33
t156 = 4
MEM[D] = t156
HIST[t156]
# Linha 34
t157 = 5
MEM[F] = t157
HIST[t157]
# Linha 35
t158 = 5
MEM[B] = t158
HIST[t158]
# Linha 36
t159 = 2
MEM[AREA] = t159
HIST[t159]
# Linha 37
t160 = 2
MEM[VOLUME] = t160
HIST[t160]
# Linha 38
t161 = 1
t162 = 3
t163 = t161 | t162
HIST[t163]
t164 = PRINT[t163]
# Linha 39
t165 = 2
t166 = 3
t167 = t165 | t166
HIST[t167]
t168 = PRINT[t167]
# Linha 40
t169 = 5
t170 = 6
t171 = t169 | t170
HIST[t171]
t172 = PRINT[t171]
# Linha 41
t173 = 22
t174 = 7
t175 = t173 | t174
HIST[t175]
t176 = PRINT[t175]
# Linha 42
t177 = 355
t178 = 113
t179 = t177 | t178
HIST[t179]
t180 = PRINT[t179]
# Linha 43
t181 = 0
t182 = MEM[X]
t183 = t181 - t182
HIST[t183]
t184 = PRINT[t183]
# Linha 44
t185 = 0
t186 = MEM[Y]
t187 = MEM[Z]
t188 = t186 + t187
t189 = t185 - t188
HIST[t189]
t190 = PRINT[t189]
# Linha 45
t191 = 1
t192 = RES[t191]
HIST[t192]
t193 = PRINT[t192]
# Linha 46
t194 = MEM[A]
t195 = MEM[B]
t196 = t194 - t195
t197 = 0
t198 = t196 < t197
HIST[t198]
t199 = PRINT[t198]
# Linha 47
t200 = MEM[A]
t201 = MEM[B]
t202 = t200 + t201
t203 = MEM[C]
t204 = t202 * t203
HIST[t204]
t205 = PRINT[t204]
# Linha 48
t206 = 1
t207 = RES[t206]
HIST[t207]
t208 = PRINT[t207]
# Linha 49
t209 = MEM[A]
t210 = MEM[B]
t211 = t209 * t210
t212 = MEM[C]
t213 = t211 + t212
HIST[t213]
t214 = PRINT[t213]
# Linha 50
t215 = 1
t216 = RES[t215]
HIST[t216]
t217 = PRINT[t216]
# Linha 51
t218 = MEM[A]
t219 = MEM[B]
t220 = t218 + t219
t221 = MEM[C]
t222 = t220 * t221
t223 = MEM[D]
t224 = t222 + t223
HIST[t224]
t225 = PRINT[t224]
# Linha 52
t226 = MEM[A]
t227 = MEM[B]
t228 = t226 * t227
t229 = MEM[C]
t230 = t228 + t229
t231 = MEM[D]
t232 = t230 * t231
HIST[t232]
t233 = PRINT[t232]
# Linha 53
t234 = 1
t235 = RES[t234]
HIST[t235]
t236 = PRINT[t235]
# Linha 54
t237 = 10
MEM[N] = t237
HIST[t237]
# Linha 55
L10:
t239 = MEM[N]
t240 = 0
t241 = t239 > t240
ifFalse t241 goto L11
t242 = MEM[N]
t243 = 1
t244 = t242 - t243
MEM[N] = t244
t238 = t244
goto L10
L11:
HIST[t238]
# Linha 56
t245 = MEM[N]
HIST[t245]
t246 = PRINT[t245]
# Linha 57
t247 = 0
MEM[SOMA] = t247
HIST[t247]
# Linha 58
t248 = 1
t249 = RES[t248]
HIST[t249]
t250 = PRINT[t249]
# Linha 59
t251 = 1
MEM[I] = t251
HIST[t251]
# Linha 60
L12:
t253 = MEM[I]
t254 = 10
t255 = t253 <= t254
ifFalse t255 goto L13
t256 = MEM[SOMA]
t257 = MEM[I]
t258 = t256 + t257
MEM[SOMA] = t258
t259 = MEM[I]
t260 = 1
t261 = t259 + t260
MEM[I] = t261
t262 = t258 * t261
t252 = t262
goto L12
L13:
HIST[t252]
# Linha 61
t263 = MEM[SOMA]
HIST[t263]
t264 = PRINT[t263]
# Linha 62
t265 = MEM[X]
t266 = MEM[Y]
t267 = t265 / t266
t268 = MEM[Y]
t269 = t267 * t268
t270 = MEM[X]
t271 = t269 - t270
HIST[t271]
t272 = PRINT[t271]
# Linha 63
t273 = MEM[X]
t274 = MEM[Y]
t275 = t273 + t274
t276 = MEM[Z]
t277 = 10
t278 = t276 + t277
t279 = t275 * t278
t280 = MEM[A]
t281 = MEM[B]
t282 = t280 + t281
t283 = MEM[C]
t284 = 1
t285 = t283 * t284
t286 = t282 / t285
t287 = t279 - t286
HIST[t287]
t288 = PRINT[t287]
# Linha 64
t289 = 5
MEM[I] = t289
HIST[t289]
# Linha 65
t290 = 1
MEM[FAT] = t290
HIST[t290]
# Linha 66
L14:
t292 = MEM[I]
t293 = 0
t294 = t292 > t293
ifFalse t294 goto L15
t295 = MEM[FAT]
t296 = MEM[I]
t297 = t295 * t296
MEM[FAT] = t297
t298 = MEM[I]
t299 = 1
t300 = t298 - t299
MEM[I] = t300
t301 = t297 * t300
t291 = t301
goto L14
L15:
HIST[t291]
# Linha 67
t302 = MEM[FAT]
HIST[t302]
t303 = PRINT[t302]
# Linha 68
t304 = 100
MEM[LIMITE] = t304
HIST[t304]
# Linha 69
t305 = 0
MEM[CONTADOR] = t305
HIST[t305]
# Linha 70
t306 = 0
MEM[SOMA] = t306
HIST[t306]
# Linha 71
L16:
t308 = MEM[CONTADOR]
t309 = MEM[LIMITE]
t310 = t308 < t309
ifFalse t310 goto L17
t311 = MEM[SOMA]
t312 = MEM[CONTADOR]
t313 = t311 + t312
MEM[SOMA] = t313
t307 = t313
goto L16
L17:
HIST[t307]
# Linha 72
t314 = MEM[SOMA]
HIST[t314]
t315 = PRINT[t314]
# Linha 73
t316 = MEM[SOMA]
t317 = 2
t318 = t316 / t317
t319 = MEM[FAT]
t320 = 2
t321 = t319 / t320
t322 = t318 + t321
t323 = 500.5
t324 = t322 | t323
HIST[t324]
t325 = PRINT[t324]
# Linha 74
t326 = 10
t327 = 20
t328 = t326 + t327
HIST[t328]
t329 = PRINT[t328]
# Linha 75
t330 = 1
t331 = RES[t330]
HIST[t331]
t332 = PRINT[t331]
# Linha 76
t333 = 100
t334 = 25
t335 = t333 - t334
HIST[t335]
t336 = PRINT[t335]
# Linha 77
t337 = 1
t338 = RES[t337]
HIST[t338]
t339 = PRINT[t338]
# Linha 78
t340 = 12
t341 = 10
t342 = t340 * t341
HIST[t342]
t343 = PRINT[t342]
# Linha 79
t344 = 1
t345 = RES[t344]
HIST[t345]
t346 = PRINT[t345]
# Linha 80
t347 = 100
t348 = 2
t349 = t347 / t348
HIST[t349]
t350 = PRINT[t349]
# Linha 81
t351 = 1
t352 = RES[t351]
HIST[t352]
t353 = PRINT[t352]
# Linha 82
t354 = 125
t355 = 5
t356 = t354 | t355
HIST[t356]
t357 = PRINT[t356]
# Linha 83
t358 = 1
t359 = RES[t358]
HIST[t359]
t360 = PRINT[t359]
# Linha 84
t361 = 10
t362 = 3
t363 = t361 % t362
HIST[t363]
t364 = PRINT[t363]
# Linha 85
t365 = 1
t366 = RES[t365]
HIST[t366]
t367 = PRINT[t366]
# Linha 86
t368 = 2
t369 = 6
t370 = t368 ^ t369
HIST[t370]
t371 = PRINT[t370]
# Linha 87
t372 = 1
t373 = RES[t372]
HIST[t373]
t374 = PRINT[t373]
# Linha 88
t375 = 5
t376 = 3
t377 = t375 ^ t376
HIST[t377]
t378 = PRINT[t377]
# Linha 89
t379 = 1
t380 = RES[t379]
HIST[t380]
t381 = PRINT[t380]
# Linha 90
t382 = 10
t383 = 10
t384 = t382 == t383
HIST[t384]
t385 = PRINT[t384]
# Linha 91
t386 = 1
t387 = RES[t386]
HIST[t387]
t388 = PRINT[t387]
# Linha 92
t389 = 20
t390 = 10
t391 = t389 > t390
HIST[t391]
t392 = PRINT[t391]
# Linha 93
t393 = 1
t394 = RES[t393]
HIST[t394]
t395 = PRINT[t394]
# Linha 94
t396 = 5
t397 = 50
t398 = t396 < t397
HIST[t398]
t399 = PRINT[t398]
# Linha 95
t400 = 1
t401 = RES[t400]
HIST[t401]
t402 = PRINT[t401]
# Linha 96
t403 = 15
t404 = 15
t405 = t403 >= t404
HIST[t405]
t406 = PRINT[t405]
# Linha 97
t407 = 1
t408 = RES[t407]
HIST[t408]
t409 = PRINT[t408]
# Linha 98
t410 = 10
t411 = 20
t412 = t410 <= t411
HIST[t412]
t413 = PRINT[t412]
# Linha 99
t414 = 1
t415 = RES[t414]
HIST[t415]
t416 = PRINT[t415]
# Linha 100
t417 = 100
t418 = 100
t419 = t417 != t418
HIST[t419]
t420 = PRINT[t419]
# Linha 101
t421 = 1
t422 = RES[t421]
HIST[t422]
t423 = PRINT[t422]
# Linha 102
t424 = 1.5
t425 = 2.5
t426 = t424 + t425
HIST[t426]
t427 = PRINT[t426]
# Linha 103
t428 = 1
t429 = RES[t428]
HIST[t429]
t430 = PRINT[t429]
# Linha 104
t431 = 10.5
t432 = 0.5
t433 = t431 - t432
HIST[t433]
t434 = PRINT[t433]
# Linha 105
t435 = 1
t436 = RES[t435]
HIST[t436]
t437 = PRINT[t436]
# Linha 106
t438 = 10
t439 = 0.5
t440 = t438 * t439
HIST[t440]
t441 = PRINT[t440]
# Linha 107
t442 = 1
t443 = RES[t442]
HIST[t443]
t444 = PRINT[t443]
# Linha 108
t445 = 5
t446 = 0.25
t447 = t445 * t446
HIST[t447]
t448 = PRINT[t447]
# Linha 109
t449 = 1
t450 = RES[t449]
HIST[t450]
t451 = PRINT[t450]
# Linha 110
t452 = 10
t453 = 2
t454 = t452 | t453
HIST[t454]
t455 = PRINT[t454]
# Linha 111
t456 = 1
t457 = RES[t456]
HIST[t457]
t458 = PRINT[t457]
# Linha 112
t459 = 1
t460 = 3
t461 = t459 | t460
HIST[t461]
t462 = PRINT[t461]
# Linha 113
t463 = 1
t464 = RES[t463]
HIST[t464]
t465 = PRINT[t464]
# Linha 114
t466 = 22
t467 = 7
t468 = t466 | t467
HIST[t468]
t469 = PRINT[t468]
# Linha 115
t470 = 1
t471 = RES[t470]
HIST[t471]
t472 = PRINT[t471]
# Linha 116
t473 = 10
t474 = 2
t475 = t473 + t474
t476 = 5
t477 = t475 - t476
HIST[t477]
t478 = PRINT[t477]
# Linha 117
t479 = 1
t480 = RES[t479]
HIST[t480]
t481 = PRINT[t480]
# Linha 118
t482 = 5
t483 = 5
t484 = t482 * t483
t485 = 2
t486 = t484 / t485
HIST[t486]
t487 = PRINT[t486]
# Linha 119
t488 = 1
t489 = RES[t488]
HIST[t489]
t490 = PRINT[t489]
# Linha 120
t491 = 100
t492 = 2
t493 = t491 | t492
t494 = 10
t495 = t493 + t494
HIST[t495]
t496 = PRINT[t495]
# Linha 121
t497 = 1
t498 = RES[t497]
HIST[t498]
t499 = PRINT[t498]
# Linha 122
t500 = 2
t501 = 3
t502 = t500 ^ t501
t503 = 4
t504 = t502 + t503
HIST[t504]
t505 = PRINT[t504]
# Linha 123
t506 = 1
t507 = RES[t506]
HIST[t507]
t508 = PRINT[t507]
# Linha 124
t509 = 10
t510 = 2
t511 = t509 % t510
t512 = 1
t513 = t511 + t512
HIST[t513]
t514 = PRINT[t513]
# Linha 125
t515 = 1
t516 = RES[t515]
HIST[t516]
t517 = PRINT[t516]
# Linha 126
t518 = 50
t519 = 2
t520 = t518 * t519
t521 = 100
t522 = t520 == t521
HIST[t522]
t523 = PRINT[t522]
# Linha 127
t524 = 1
t525 = RES[t524]
HIST[t525]
t526 = PRINT[t525]
# Linha 128
t527 = 10
t528 = 10
t529 = t527 + t528
t530 = 20
t531 = t529 >= t530
HIST[t531]
t532 = PRINT[t531]
# Linha 129
t533 = 1
t534 = RES[t533]
HIST[t534]
t535 = PRINT[t534]
# Linha 130
t536 = 126
t537 = 127
t538 = t536 < t537
HIST[t538]
t539 = PRINT[t538]
# Linha 131
t540 = 1
t541 = RES[t540]
HIST[t541]
t542 = PRINT[t541]
# Linha 132
t543 = 127
t544 = 127
t545 = t543 == t544
HIST[t545]
t546 = PRINT[t545]
# Linha 133
t547 = 1
t548 = RES[t547]
HIST[t548]
t549 = PRINT[t548]
# Linha 134
t550 = -10
t551 = -20
t552 = t550 + t551
HIST[t552]
t553 = PRINT[t552]
# Linha 135
t554 = 1
t555 = RES[t554]
HIST[t555]
t556 = PRINT[t555]
# Linha 136
t557 = -50
t558 = 2
t559 = t557 * t558
HIST[t559]
t560 = PRINT[t559]
# Linha 137
t561 = 1
t562 = RES[t561]
HIST[t562]
t563 = PRINT[t562]
# Linha 138
t564 = -100
t565 = 2
t566 = t564 / t565
HIST[t566]
t567 = PRINT[t566]
# Linha 139
t568 = 1
t569 = RES[t568]
HIST[t569]
t570 = PRINT[t569]
# Linha 140
t571 = -5
t572 = 5
t573 = t571 * t572
HIST[t573]
t574 = PRINT[t573]
# Linha 141
t575 = 1
t576 = RES[t575]
HIST[t576]
t577 = PRINT[t576]
# Linha 142
t578 = 0
t579 = 0
t580 = t578 == t579
HIST[t580]
t581 = PRINT[t580]
# Linha 143
t582 = 1
t583 = RES[t582]
HIST[t583]
t584 = PRINT[t583]
# Linha 144
t585 = 0
t586 = 1
t587 = t585 < t586
HIST[t587]
t588 = PRINT[t587]
# Linha 145
t589 = 1
t590 = RES[t589]
HIST[t590]
t591 = PRINT[t590]
# Linha 146
t592 = 1
t593 = 0
t594 = t592 > t593
HIST[t594]
t595 = PRINT[t594]
# Linha 147
t596 = 1
t597 = RES[t596]
HIST[t597]
t598 = PRINT[t597]
# Linha 148
t599 = 0.1
t600 = 0.1
t601 = t599 + t600
HIST[t601]
t602 = PRINT[t601]
# Linha 149
t603 = 1
t604 = RES[t603]
HIST[t604]
t605 = PRINT[t604]
# Linha 150
t606 = 0.1
t607 = 100
t608 = t606 * t607
HIST[t608]
t609 = PRINT[t608]
# Linha 151
t610 = 1
t611 = RES[t610]
HIST[t611]
t612 = PRINT[t611]
# Linha 152
t613 = 12.5
t614 = 10
t615 = t613 * t614
HIST[t615]
t616 = PRINT[t615]
# Linha 153
t617 = 1
t618 = RES[t617]
HIST[t618]
t619 = PRINT[t618]
# Linha 154
t620 = 60
t621 = 2.1
t622 = t620 * t621
HIST[t622]
t623 = PRINT[t622]
# Linha 155
t624 = 1
t625 = RES[t624]
HIST[t625]
t626 = PRINT[t625]
# Linha 156
t627 = 100
t628 = 1.2
t629 = t627 | t628
HIST[t629]
t630 = PRINT[t629]
# Linha 157
t631 = 1
t632 = RES[t631]
HIST[t632]
t633 = PRINT[t632]
# Linha 158
t634 = 3
t635 = 3
t636 = t634 ^ t635
HIST[t636]
t637 = PRINT[t636]
# Linha 159
t638 = 1
t639 = RES[t638]
HIST[t639]
t640 = PRINT[t639]
# Linha 160
t641 = 11
t642 = 2
t643 = t641 ^ t642
HIST[t643]
t644 = PRINT[t643]
# Linha 161
t645 = 1
t646 = RES[t645]
HIST[t646]
t647 = PRINT[t646]
# Linha 162
t648 = 5
t649 = 3
t650 = t648 % t649
HIST[t650]
t651 = PRINT[t650]
# Linha 163
t652 = 1
t653 = RES[t652]
HIST[t653]
t654 = PRINT[t653]
# Linha 164
t655 = 1
t656 = 2
t657 = t655 + t656
t658 = 3
t659 = 4
t660 = t658 + t659
t661 = t657 + t660
HIST[t661]
t662 = PRINT[t661]
# Linha 165
t663 = 1
t664 = RES[t663]
HIST[t664]
t665 = PRINT[t664]
# Linha 166
t666 = 10
t667 = 2
t668 = t666 * t667
t669 = 5
t670 = 4
t671 = t669 * t670
t672 = t668 - t671
HIST[t672]
t673 = PRINT[t672]
# Linha 167
t674 = 1
t675 = RES[t674]
HIST[t675]
t676 = PRINT[t675]
# Linha 168
t677 = 120
t678 = 5
t679 = t677 + t678
HIST[t679]
t680 = PRINT[t679]
# Linha 169
t681 = 1
t682 = RES[t681]
HIST[t682]
t683 = PRINT[t682]
# Linha 170
t684 = 127.5
t685 = 0.5
t686 = t684 - t685
HIST[t686]
t687 = PRINT[t686]
# Linha 171
t688 = 1
t689 = RES[t688]
HIST[t689]
t690 = PRINT[t689]
# Linha 172
t691 = 0.5
t692 = 250
t693 = t691 * t692
HIST[t693]
t694 = PRINT[t693]
# Linha 173
t695 = 1
t696 = RES[t695]
HIST[t696]
t697 = PRINT[t696]
```

### TAC Otimizado

```
# Linha 1
MEM[X] = 100
HIST[100]
# Linha 2
MEM[Y] = 50
HIST[50]
# Linha 3
MEM[Z] = 25
HIST[25]
# Linha 4
MEM[PI] = 3.14159
HIST[3.14159]
# Linha 5
MEM[E] = 2.71828
HIST[2.71828]
# Linha 6
t6 = RES[4]
HIST[t6]
t7 = PRINT[t6]
# Linha 7
t8 = MEM[X]
t9 = MEM[Y]
t10 = t8 + t9
t11 = MEM[Z]
t12 = t10 - t11
HIST[t12]
t13 = PRINT[t12]
# Linha 8
t14 = MEM[X]
t15 = MEM[Y]
t16 = t14 * t15
t17 = MEM[Z]
t18 = t16 / t17
HIST[t18]
t19 = PRINT[t18]
# Linha 9
t20 = MEM[X]
t22 = t20 ^ 2
t23 = MEM[Y]
t25 = t23 ^ 2
t26 = t22 + t25
HIST[t26]
t27 = PRINT[t26]
# Linha 10
t28 = MEM[PI]
t30 = t28 * 2
t32 = t30 ^ 10
HIST[t32]
t33 = PRINT[t32]
# Linha 11
t34 = MEM[E]
t35 = MEM[X]
t36 = MEM[Y]
t37 = t35 | t36
t38 = t34 + t37
HIST[t38]
t39 = PRINT[t38]
# Linha 12
t40 = MEM[X]
t41 = MEM[Y]
t42 = t40 + t41
t43 = MEM[Z]
t44 = t42 > t43
HIST[t44]
t45 = PRINT[t44]
# Linha 13
t46 = MEM[X]
t47 = MEM[Y]
t48 = MEM[Z]
t49 = t47 + t48
t50 = t46 + t49
t52 = t50 >= 100
HIST[t52]
t53 = PRINT[t52]
# Linha 14
t54 = MEM[PI]
t55 = MEM[E]
t56 = t54 > t55
ifFalse t56 goto L0
goto L1
L0:
L1:
HIST[t57]
# Linha 15
t60 = MEM[X]
t61 = MEM[Y]
t62 = t60 ^ t61
t63 = MEM[Z]
t64 = t62 % t63
HIST[t64]
t65 = PRINT[t64]
# Linha 16
t66 = MEM[Z]
t68 = t66 / 4
t69 = MEM[X]
t71 = t69 | 5
t72 = t68 - t71
HIST[t72]
t73 = PRINT[t72]
# Linha 17
t74 = MEM[X]
t75 = MEM[Y]
t76 = t74 / t75
t77 = MEM[Z]
t78 = t76 | t77
t80 = t78 * 2
HIST[t80]
t81 = PRINT[t80]
# Linha 18
t82 = MEM[X]
t83 = MEM[Y]
t84 = t82 | t83
t85 = MEM[Z]
t87 = t85 / 2
t88 = t84 - t87
HIST[t88]
t89 = PRINT[t88]
# Linha 19
t90 = MEM[X]
t92 = t90 > 50
ifFalse t92 goto L2
t94 = MEM[X]
goto L3
L2:
t97 = MEM[X]
L3:
HIST[t93]
# Linha 20
t100 = MEM[Y]
t101 = MEM[Z]
t102 = t100 == t101
ifFalse t102 goto L4
goto L5
L4:
L5:
HIST[t103]
# Linha 21
MEM[I] = 0
HIST[0]
# Linha 22
L6:
t108 = MEM[I]
t110 = t108 < 10
ifFalse t110 goto L7
t111 = MEM[I]
t113 = t111 + 1
MEM[I] = t113
goto L6
L7:
HIST[t107]
# Linha 23
t114 = MEM[I]
HIST[t114]
t115 = PRINT[t114]
# Linha 24
MEM[CONTADOR] = 1
HIST[1]
# Linha 25
L8:
t118 = MEM[CONTADOR]
t120 = t118 <= 5
ifFalse t120 goto L9
t121 = MEM[CONTADOR]
t123 = t121 * 2
MEM[CONTADOR] = t123
goto L8
L9:
HIST[t117]
# Linha 26
t124 = MEM[CONTADOR]
HIST[t124]
t125 = PRINT[t124]
# Linha 27
HIST[148]
t133 = PRINT[148]
# Linha 28
t134 = MEM[X]
t135 = MEM[Y]
t136 = t134 + t135
t138 = t136 / 2
HIST[t138]
t139 = PRINT[t138]
# Linha 29
t140 = MEM[PI]
t142 = t140 * 2
t143 = MEM[X]
t144 = t142 * t143
HIST[t144]
t145 = PRINT[t144]
# Linha 30
t146 = MEM[X]
t147 = MEM[Y]
t148 = t146 / t147
t149 = MEM[Y]
t150 = MEM[Z]
t151 = t149 / t150
t152 = t148 * t151
HIST[t152]
t153 = PRINT[t152]
# Linha 31
MEM[A] = 1
HIST[1]
# Linha 32
MEM[C] = 3
HIST[3]
# Linha 33
MEM[D] = 4
HIST[4]
# Linha 34
MEM[F] = 5
HIST[5]
# Linha 35
MEM[B] = 5
HIST[5]
# Linha 36
MEM[AREA] = 2
HIST[2]
# Linha 37
MEM[VOLUME] = 2
HIST[2]
# Linha 38
HIST[0.3333333333333333]
t164 = PRINT[0.3333333333333333]
# Linha 39
HIST[0.6666666666666666]
t168 = PRINT[0.6666666666666666]
# Linha 40
HIST[0.8333333333333334]
t172 = PRINT[0.8333333333333334]
# Linha 41
HIST[3.142857142857143]
t176 = PRINT[3.142857142857143]
# Linha 42
HIST[3.1415929203539825]
t180 = PRINT[3.1415929203539825]
# Linha 43
t182 = MEM[X]
t183 = 0 - t182
HIST[t183]
t184 = PRINT[t183]
# Linha 44
t186 = MEM[Y]
t187 = MEM[Z]
t188 = t186 + t187
t189 = 0 - t188
HIST[t189]
t190 = PRINT[t189]
# Linha 45
t192 = RES[1]
HIST[t192]
t193 = PRINT[t192]
# Linha 46
t194 = MEM[A]
t195 = MEM[B]
t196 = t194 - t195
t198 = t196 < 0
HIST[t198]
t199 = PRINT[t198]
# Linha 47
t200 = MEM[A]
t201 = MEM[B]
t202 = t200 + t201
t203 = MEM[C]
t204 = t202 * t203
HIST[t204]
t205 = PRINT[t204]
# Linha 48
t207 = RES[1]
HIST[t207]
t208 = PRINT[t207]
# Linha 49
t209 = MEM[A]
t210 = MEM[B]
t211 = t209 * t210
t212 = MEM[C]
t213 = t211 + t212
HIST[t213]
t214 = PRINT[t213]
# Linha 50
t216 = RES[1]
HIST[t216]
t217 = PRINT[t216]
# Linha 51
t218 = MEM[A]
t219 = MEM[B]
t220 = t218 + t219
t221 = MEM[C]
t222 = t220 * t221
t223 = MEM[D]
t224 = t222 + t223
HIST[t224]
t225 = PRINT[t224]
# Linha 52
t226 = MEM[A]
t227 = MEM[B]
t228 = t226 * t227
t229 = MEM[C]
t230 = t228 + t229
t231 = MEM[D]
t232 = t230 * t231
HIST[t232]
t233 = PRINT[t232]
# Linha 53
t235 = RES[1]
HIST[t235]
t236 = PRINT[t235]
# Linha 54
MEM[N] = 10
HIST[10]
# Linha 55
L10:
t239 = MEM[N]
t241 = t239 > 0
ifFalse t241 goto L11
t242 = MEM[N]
t244 = t242 - 1
MEM[N] = t244
goto L10
L11:
HIST[t238]
# Linha 56
t245 = MEM[N]
HIST[t245]
t246 = PRINT[t245]
# Linha 57
MEM[SOMA] = 0
HIST[0]
# Linha 58
t249 = RES[1]
HIST[t249]
t250 = PRINT[t249]
# Linha 59
MEM[I] = 1
HIST[1]
# Linha 60
L12:
t253 = MEM[I]
t255 = t253 <= 10
ifFalse t255 goto L13
t256 = MEM[SOMA]
t257 = MEM[I]
t258 = t256 + t257
MEM[SOMA] = t258
t259 = MEM[I]
t261 = t259 + 1
MEM[I] = t261
goto L12
L13:
HIST[t252]
# Linha 61
t263 = MEM[SOMA]
HIST[t263]
t264 = PRINT[t263]
# Linha 62
t265 = MEM[X]
t266 = MEM[Y]
t267 = t265 / t266
t268 = MEM[Y]
t269 = t267 * t268
t270 = MEM[X]
t271 = t269 - t270
HIST[t271]
t272 = PRINT[t271]
# Linha 63
t273 = MEM[X]
t274 = MEM[Y]
t275 = t273 + t274
t276 = MEM[Z]
t278 = t276 + 10
t279 = t275 * t278
t280 = MEM[A]
t281 = MEM[B]
t282 = t280 + t281
t283 = MEM[C]
t285 = t283 * 1
t286 = t282 / t285
t287 = t279 - t286
HIST[t287]
t288 = PRINT[t287]
# Linha 64
MEM[I] = 5
HIST[5]
# Linha 65
MEM[FAT] = 1
HIST[1]
# Linha 66
L14:
t292 = MEM[I]
t294 = t292 > 0
ifFalse t294 goto L15
t295 = MEM[FAT]
t296 = MEM[I]
t297 = t295 * t296
MEM[FAT] = t297
t298 = MEM[I]
t300 = t298 - 1
MEM[I] = t300
goto L14
L15:
HIST[t291]
# Linha 67
t302 = MEM[FAT]
HIST[t302]
t303 = PRINT[t302]
# Linha 68
MEM[LIMITE] = 100
HIST[100]
# Linha 69
MEM[CONTADOR] = 0
HIST[0]
# Linha 70
MEM[SOMA] = 0
HIST[0]
# Linha 71
L16:
t308 = MEM[CONTADOR]
t309 = MEM[LIMITE]
t310 = t308 < t309
ifFalse t310 goto L17
t311 = MEM[SOMA]
t312 = MEM[CONTADOR]
t313 = t311 + t312
MEM[SOMA] = t313
goto L16
L17:
HIST[t307]
# Linha 72
t314 = MEM[SOMA]
HIST[t314]
t315 = PRINT[t314]
# Linha 73
t316 = MEM[SOMA]
t318 = t316 / 2
t319 = MEM[FAT]
t321 = t319 / 2
t322 = t318 + t321
t324 = t322 | 500.5
HIST[t324]
t325 = PRINT[t324]
# Linha 74
HIST[30]
t329 = PRINT[30]
# Linha 75
t331 = RES[1]
HIST[t331]
t332 = PRINT[t331]
# Linha 76
HIST[75]
t336 = PRINT[75]
# Linha 77
t338 = RES[1]
HIST[t338]
t339 = PRINT[t338]
# Linha 78
HIST[120]
t343 = PRINT[120]
# Linha 79
t345 = RES[1]
HIST[t345]
t346 = PRINT[t345]
# Linha 80
HIST[50]
t350 = PRINT[50]
# Linha 81
t352 = RES[1]
HIST[t352]
t353 = PRINT[t352]
# Linha 82
HIST[25.0]
t357 = PRINT[25.0]
# Linha 83
t359 = RES[1]
HIST[t359]
t360 = PRINT[t359]
# Linha 84
HIST[1]
t364 = PRINT[1]
# Linha 85
t366 = RES[1]
HIST[t366]
t367 = PRINT[t366]
# Linha 86
HIST[64]
t371 = PRINT[64]
# Linha 87
t373 = RES[1]
HIST[t373]
t374 = PRINT[t373]
# Linha 88
HIST[125]
t378 = PRINT[125]
# Linha 89
t380 = RES[1]
HIST[t380]
t381 = PRINT[t380]
# Linha 90
HIST[1]
t385 = PRINT[1]
# Linha 91
t387 = RES[1]
HIST[t387]
t388 = PRINT[t387]
# Linha 92
HIST[1]
t392 = PRINT[1]
# Linha 93
t394 = RES[1]
HIST[t394]
t395 = PRINT[t394]
# Linha 94
HIST[1]
t399 = PRINT[1]
# Linha 95
t401 = RES[1]
HIST[t401]
t402 = PRINT[t401]
# Linha 96
HIST[1]
t406 = PRINT[1]
# Linha 97
t408 = RES[1]
HIST[t408]
t409 = PRINT[t408]
# Linha 98
HIST[1]
t413 = PRINT[1]
# Linha 99
t415 = RES[1]
HIST[t415]
t416 = PRINT[t415]
# Linha 100
HIST[0]
t420 = PRINT[0]
# Linha 101
t422 = RES[1]
HIST[t422]
t423 = PRINT[t422]
# Linha 102
HIST[4]
t427 = PRINT[4]
# Linha 103
t429 = RES[1]
HIST[t429]
t430 = PRINT[t429]
# Linha 104
HIST[10]
t434 = PRINT[10]
# Linha 105
t436 = RES[1]
HIST[t436]
t437 = PRINT[t436]
# Linha 106
HIST[5]
t441 = PRINT[5]
# Linha 107
t443 = RES[1]
HIST[t443]
t444 = PRINT[t443]
# Linha 108
HIST[1.25]
t448 = PRINT[1.25]
# Linha 109
t450 = RES[1]
HIST[t450]
t451 = PRINT[t450]
# Linha 110
HIST[5.0]
t455 = PRINT[5.0]
# Linha 111
t457 = RES[1]
HIST[t457]
t458 = PRINT[t457]
# Linha 112
HIST[0.3333333333333333]
t462 = PRINT[0.3333333333333333]
# Linha 113
t464 = RES[1]
HIST[t464]
t465 = PRINT[t464]
# Linha 114
HIST[3.142857142857143]
t469 = PRINT[3.142857142857143]
# Linha 115
t471 = RES[1]
HIST[t471]
t472 = PRINT[t471]
# Linha 116
HIST[7]
t478 = PRINT[7]
# Linha 117
t480 = RES[1]
HIST[t480]
t481 = PRINT[t480]
# Linha 118
HIST[12]
t487 = PRINT[12]
# Linha 119
t489 = RES[1]
HIST[t489]
t490 = PRINT[t489]
# Linha 120
HIST[60]
t496 = PRINT[60]
# Linha 121
t498 = RES[1]
HIST[t498]
t499 = PRINT[t498]
# Linha 122
HIST[12]
t505 = PRINT[12]
# Linha 123
t507 = RES[1]
HIST[t507]
t508 = PRINT[t507]
# Linha 124
HIST[1]
t514 = PRINT[1]
# Linha 125
t516 = RES[1]
HIST[t516]
t517 = PRINT[t516]
# Linha 126
HIST[1]
t523 = PRINT[1]
# Linha 127
t525 = RES[1]
HIST[t525]
t526 = PRINT[t525]
# Linha 128
HIST[1]
t532 = PRINT[1]
# Linha 129
t534 = RES[1]
HIST[t534]
t535 = PRINT[t534]
# Linha 130
HIST[1]
t539 = PRINT[1]
# Linha 131
t541 = RES[1]
HIST[t541]
t542 = PRINT[t541]
# Linha 132
HIST[1]
t546 = PRINT[1]
# Linha 133
t548 = RES[1]
HIST[t548]
t549 = PRINT[t548]
# Linha 134
HIST[-30]
t553 = PRINT[-30]
# Linha 135
t555 = RES[1]
HIST[t555]
t556 = PRINT[t555]
# Linha 136
HIST[-100]
t560 = PRINT[-100]
# Linha 137
t562 = RES[1]
HIST[t562]
t563 = PRINT[t562]
# Linha 138
HIST[-50]
t567 = PRINT[-50]
# Linha 139
t569 = RES[1]
HIST[t569]
t570 = PRINT[t569]
# Linha 140
HIST[-25]
t574 = PRINT[-25]
# Linha 141
t576 = RES[1]
HIST[t576]
t577 = PRINT[t576]
# Linha 142
HIST[1]
t581 = PRINT[1]
# Linha 143
t583 = RES[1]
HIST[t583]
t584 = PRINT[t583]
# Linha 144
HIST[1]
t588 = PRINT[1]
# Linha 145
t590 = RES[1]
HIST[t590]
t591 = PRINT[t590]
# Linha 146
HIST[1]
t595 = PRINT[1]
# Linha 147
t597 = RES[1]
HIST[t597]
t598 = PRINT[t597]
# Linha 148
HIST[0.2]
t602 = PRINT[0.2]
# Linha 149
t604 = RES[1]
HIST[t604]
t605 = PRINT[t604]
# Linha 150
HIST[10]
t609 = PRINT[10]
# Linha 151
t611 = RES[1]
HIST[t611]
t612 = PRINT[t611]
# Linha 152
HIST[125]
t616 = PRINT[125]
# Linha 153
t618 = RES[1]
HIST[t618]
t619 = PRINT[t618]
# Linha 154
HIST[126]
t623 = PRINT[126]
# Linha 155
t625 = RES[1]
HIST[t625]
t626 = PRINT[t625]
# Linha 156
HIST[83.33333333333334]
t630 = PRINT[83.33333333333334]
# Linha 157
t632 = RES[1]
HIST[t632]
t633 = PRINT[t632]
# Linha 158
HIST[27]
t637 = PRINT[27]
# Linha 159
t639 = RES[1]
HIST[t639]
t640 = PRINT[t639]
# Linha 160
HIST[121]
t644 = PRINT[121]
# Linha 161
t646 = RES[1]
HIST[t646]
t647 = PRINT[t646]
# Linha 162
HIST[2]
t651 = PRINT[2]
# Linha 163
t653 = RES[1]
HIST[t653]
t654 = PRINT[t653]
# Linha 164
HIST[10]
t662 = PRINT[10]
# Linha 165
t664 = RES[1]
HIST[t664]
t665 = PRINT[t664]
# Linha 166
HIST[0]
t673 = PRINT[0]
# Linha 167
t675 = RES[1]
HIST[t675]
t676 = PRINT[t675]
# Linha 168
HIST[125]
t680 = PRINT[125]
# Linha 169
t682 = RES[1]
HIST[t682]
t683 = PRINT[t682]
# Linha 170
HIST[127]
t687 = PRINT[127]
# Linha 171
t689 = RES[1]
HIST[t689]
t690 = PRINT[t689]
# Linha 172
HIST[125]
t694 = PRINT[125]
# Linha 173
t696 = RES[1]
HIST[t696]
t697 = PRINT[t696]
```

