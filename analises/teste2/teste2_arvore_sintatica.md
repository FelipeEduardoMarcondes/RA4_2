# Árvore Sintática Atribuída - .\teste2.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = X
```

## Expressão 2

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 50
  └─ id = Y
```

## Expressão 3

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 25
  └─ id = Z
```

## Expressão 4

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 3.14
  └─ id = PI
```

## Expressão 5

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 2.71
  └─ id = E
```

## Expressão 6

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 4
```

## Expressão 7

**Tipo inferido:** `int`

```
minus : int = -
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 8

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 9

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = A
```

## Expressão 10

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = B
```

## Expressão 11

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = C
```

## Expressão 12

**Tipo inferido:** `int`

```
minus : int = -
  ├─ plus : int = +
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 13

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 14

**Tipo inferido:** `int`

```
plus : int = +
  ├─ pow : int = ^
    ├─ id : int = A
    └─ num : int = 2
  └─ pow : int = ^
    ├─ id : int = B
    └─ num : int = 2
```

## Expressão 15

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = E
  └─ div_real : real = |
    ├─ id : int = A
    └─ id : int = B
```

## Expressão 16

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 1
  └─ num : int = 3
```

## Expressão 17

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 22
  └─ num : int = 7
```

## Expressão 18

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ id : int = B
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 19

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = A
    └─ id : int = B
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 20

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 21

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ num : int = 5
  ├─ minus : int = -
    ├─ id : int = A
    └─ num : int = 1
  └─ plus : int = +
    ├─ id : int = A
    └─ num : int = 1
```

## Expressão 22

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = B
    └─ id : int = C
  ├─ num : int = 1
  └─ num : int = -1
```

## Expressão 23

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = I
```

## Expressão 24

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ num : int = 5
  └─ plus : int = +
    ├─ store : int
      ├─ plus : int = +
        ├─ id : int = I
        └─ num : int = 1
      └─ id = I
    └─ id : int = I
```

## Expressão 25

**Tipo inferido:** `int`

```
id : int = I
```

