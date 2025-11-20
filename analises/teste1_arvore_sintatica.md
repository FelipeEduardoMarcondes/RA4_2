# Árvore Sintática Atribuída - .\teste1.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
plus : int = +
  ├─ num : int = 2
  └─ num : int = 3
```

## Expressão 2

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 10
  └─ num : int = 5
```

## Expressão 3

**Tipo inferido:** `int`

```
mult : int = *
  ├─ num : int = 4
  └─ num : int = 5
```

## Expressão 4

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ num : int = 100
  └─ num : int = 10
```

## Expressão 5

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = X
```

## Expressão 6

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = X
  └─ num : int = 3
```

## Expressão 7

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = A
```

## Expressão 8

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 20
  └─ id = B
```

## Expressão 9

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 99
  └─ id = UNUSED
```

## Expressão 10

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = A
  └─ id : int = B
```

## Expressão 11

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = A
```

## Expressão 12

**Tipo inferido:** `int`

```
store : int
  ├─ id : int = A
  └─ id = B
```

## Expressão 13

**Tipo inferido:** `int`

```
store : int
  ├─ id : int = B
  └─ id = C
```

## Expressão 14

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = C
  └─ num : int = 5
```

## Expressão 15

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ num : int = 2
    └─ num : int = 3
  └─ mult : int = *
    ├─ num : int = 4
    └─ num : int = 5
```

## Expressão 16

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ num : int = 100
  └─ minus : int = -
    ├─ num : int = 10
    └─ num : int = 5
```

## Expressão 17

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ num : int = 10
  └─ num : int = 5
```

## Expressão 18

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ num : int = 3
  └─ num : int = 7
```

## Expressão 19

**Tipo inferido:** `booleano`

```
eq : booleano = ==
  ├─ num : int = 5
  └─ num : int = 5
```

## Expressão 20

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ num : int = 10
    └─ num : int = 5
  ├─ num : int = 100
  └─ num : int = 200
```

## Expressão 21

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = N
```

## Expressão 22

**Tipo inferido:** `int`

```
store : int
  ├─ id : int = N
  └─ id = M
```

## Expressão 23

**Tipo inferido:** `int`

```
store : int
  ├─ id : int = M
  └─ id = K
```

## Expressão 24

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = K
  └─ num : int = 10
```

## Expressão 25

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 3.14
  └─ id = PI
```

## Expressão 26

**Tipo inferido:** `real`

```
mult : real = *
  ├─ id : real = PI
  └─ num : real = 2.0
```

## Expressão 27

**Tipo inferido:** `real`

```
res : real = RES
  └─ num : int = 1
```

## Expressão 28

**Tipo inferido:** `int`

```
pow : int = ^
  ├─ num : int = 2
  └─ num : int = 8
```

## Expressão 29

**Tipo inferido:** `int`

```
pow : int = ^
  ├─ num : int = 10
  └─ num : int = 3
```

