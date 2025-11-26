# Árvore Sintática Atribuída - .\testes\teste_estresse.txt

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
  ├─ num : real = 3.14159
  └─ id = PI
```

## Expressão 5

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 2.71828
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
plus : int = +
  ├─ pow : int = ^
    ├─ id : int = X
    └─ num : int = 2
  └─ pow : int = ^
    ├─ id : int = Y
    └─ num : int = 2
```

## Expressão 10

**Tipo inferido:** `real`

```
pow : real = ^
  ├─ mult : real = *
    ├─ id : real = PI
    └─ num : int = 2
  └─ num : int = 10
```

## Expressão 11

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = E
  └─ div_real : real = |
    ├─ id : int = X
    └─ id : int = Y
```

## Expressão 12

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 13

**Tipo inferido:** `booleano`

```
gte : booleano = >=
  ├─ plus : int = +
    ├─ id : int = X
    └─ plus : int = +
      ├─ id : int = Y
      └─ id : int = Z
  └─ num : int = 100
```

## Expressão 14

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : real = PI
    └─ id : real = E
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 15

**Tipo inferido:** `int`

```
mod : int = %
  ├─ pow : int = ^
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 16

**Tipo inferido:** `real`

```
minus : real = -
  ├─ div_int : int = /
    ├─ id : int = Z
    └─ num : int = 4
  └─ div_real : real = |
    ├─ id : int = X
    └─ num : int = 5
```

## Expressão 17

**Tipo inferido:** `real`

```
mult : real = *
  ├─ div_real : real = |
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ id : int = Z
  └─ num : int = 2
```

## Expressão 18

**Tipo inferido:** `real`

```
minus : real = -
  ├─ div_real : real = |
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Z
    └─ num : int = 2
```

## Expressão 19

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ num : int = 50
  ├─ minus : int = -
    ├─ id : int = X
    └─ num : int = 10
  └─ plus : int = +
    ├─ id : int = X
    └─ num : int = 10
```

## Expressão 20

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = Y
    └─ id : int = Z
  ├─ num : int = 1
  └─ num : int = -1
```

## Expressão 21

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = I
```

## Expressão 22

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ num : int = 10
  └─ store : int
    ├─ plus : int = +
      ├─ id : int = I
      └─ num : int = 1
    └─ id = I
```

## Expressão 23

**Tipo inferido:** `int`

```
id : int = I
```

## Expressão 24

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = CONTADOR
```

## Expressão 25

**Tipo inferido:** `int`

```
while : int = while
  ├─ lte : booleano = <=
    ├─ id : int = CONTADOR
    └─ num : int = 5
  └─ store : int
    ├─ mult : int = *
      ├─ id : int = CONTADOR
      └─ num : int = 2
    └─ id = CONTADOR
```

## Expressão 26

**Tipo inferido:** `int`

```
id : int = CONTADOR
```

## Expressão 27

**Tipo inferido:** `int`

```
minus : int = -
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ num : int = 10
      └─ num : int = 20
    └─ num : int = 5
  └─ num : int = 2
```

## Expressão 28

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ num : int = 2
```

## Expressão 29

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ id : real = PI
    └─ num : int = 2
  └─ id : int = X
```

## Expressão 30

**Tipo inferido:** `int`

```
mult : int = *
  ├─ div_int : int = /
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 31

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = A
```

## Expressão 32

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 3
  └─ id = C
```

## Expressão 33

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 4
  └─ id = D
```

## Expressão 34

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = F
```

## Expressão 35

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = B
```

## Expressão 36

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = AREA
```

## Expressão 37

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = VOLUME
```

## Expressão 38

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 1
  └─ num : int = 3
```

## Expressão 39

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 2
  └─ num : int = 3
```

## Expressão 40

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 5
  └─ num : int = 6
```

## Expressão 41

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 22
  └─ num : int = 7
```

## Expressão 42

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 355
  └─ num : int = 113
```

## Expressão 43

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ id : int = X
```

## Expressão 44

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ plus : int = +
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 45

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 1
```

## Expressão 46

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ minus : int = -
    ├─ id : int = A
    └─ id : int = B
  └─ num : int = 0
```

## Expressão 47

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 48

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 1
```

## Expressão 49

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 50

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 1
```

## Expressão 51

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ id : int = D
```

## Expressão 52

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ id : int = D
```

## Expressão 53

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 1
```

## Expressão 54

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = N
```

## Expressão 55

**Tipo inferido:** `int`

```
while : int = while
  ├─ gt : booleano = >
    ├─ id : int = N
    └─ num : int = 0
  └─ store : int
    ├─ minus : int = -
      ├─ id : int = N
      └─ num : int = 1
    └─ id = N
```

## Expressão 56

**Tipo inferido:** `int`

```
id : int = N
```

## Expressão 57

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = SOMA
```

## Expressão 58

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 1
```

## Expressão 59

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = I
```

## Expressão 60

**Tipo inferido:** `int`

```
while : int = while
  ├─ lte : booleano = <=
    ├─ id : int = I
    └─ num : int = 10
  └─ mult : int = *
    ├─ store : int
      ├─ plus : int = +
        ├─ id : int = SOMA
        └─ id : int = I
      └─ id = SOMA
    └─ store : int
      ├─ plus : int = +
        ├─ id : int = I
        └─ num : int = 1
      └─ id = I
```

## Expressão 61

**Tipo inferido:** `int`

```
id : int = SOMA
```

## Expressão 62

**Tipo inferido:** `int`

```
minus : int = -
  ├─ mult : int = *
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ id : int = Y
  └─ id : int = X
```

## Expressão 63

**Tipo inferido:** `int`

```
minus : int = -
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ id : int = X
      └─ id : int = Y
    └─ plus : int = +
      ├─ id : int = Z
      └─ num : int = 10
  └─ div_int : int = /
    ├─ plus : int = +
      ├─ id : int = A
      └─ id : int = B
    └─ mult : int = *
      ├─ id : int = C
      └─ num : int = 1
```

