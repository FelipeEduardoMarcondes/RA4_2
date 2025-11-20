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

**Tipo inferido:** `None`

```
mult = *
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  └─ gt : booleano = >
    ├─ id : int = Z
    └─ num : int = 0
```

## Expressão 13

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 14

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

## Expressão 15

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : real = PI
    └─ id : real = E
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 16

**Tipo inferido:** `None`

```
mult = *
  ├─ lt : booleano = <
    ├─ id : int = X
    └─ id : int = Y
  └─ lt : booleano = <
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 17

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 18

**Tipo inferido:** `None`

```
eq = ==
  ├─ mod = %
    ├─ id : int = X
    └─ num : real = 1001.445452112
  └─ num : int = 0
```

## Expressão 19

**Tipo inferido:** `booleano`

```
eq : booleano = ==
  ├─ mod : int = %
    ├─ id : int = Z
    └─ num : int = 5
  └─ num : int = 2
```

## Expressão 20

**Tipo inferido:** `int`

```
plus : int = +
  ├─ pow : int = ^
    ├─ num : int = 2
    └─ id : int = X
  └─ pow : int = ^
    ├─ num : int = 3
    └─ id : int = Y
```

## Expressão 21

**Tipo inferido:** `int`

```
mod : int = %
  ├─ pow : int = ^
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 22

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ id : int = X
    └─ num : real = 3.7557
  └─ div_real : real = |
    ├─ id : int = Y
    └─ num : real = 2.3345
```

## Expressão 23

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

## Expressão 24

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

## Expressão 25

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ num : real = 100.54
    └─ num : int = 7
  └─ div_real : real = |
    ├─ num : int = 3
    └─ num : int = 2
```

## Expressão 26

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

## Expressão 27

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

## Expressão 28

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = Y
    └─ id : int = Z
  ├─ num : int = 1
  └─ num : int = -1
```

## Expressão 29

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  ├─ id : int = X
  └─ id : int = Y
```

## Expressão 30

**Tipo inferido:** `int`

```
if : int = if
  ├─ neq : booleano = !=
    ├─ id : int = Z
    └─ num : int = 0
  ├─ div_int : int = /
    ├─ id : int = X
    └─ id : int = Z
  └─ num : int = 0
```

## Expressão 31

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ plus : int = +
      ├─ id : int = X
      └─ id : int = Y
    └─ num : int = 100
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 32

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = I
```

## Expressão 33

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

## Expressão 34

**Tipo inferido:** `int`

```
id : int = I
```

## Expressão 35

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = CONTADOR
```

## Expressão 36

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

## Expressão 37

**Tipo inferido:** `int`

```
id : int = CONTADOR
```

## Expressão 38

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

## Expressão 39

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ num : int = 2
```

## Expressão 40

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ id : real = PI
    └─ num : int = 2
  └─ id : int = X
```

## Expressão 41

**Tipo inferido:** `real`

```
plus : real = +
  ├─ pow : real = ^
    ├─ id : real = E
    └─ id : int = X
  └─ num : int = 1
```

## Expressão 42

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = X
    └─ id : int = Y
  └─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
```

## Expressão 43

**Tipo inferido:** `None`

```
pow = ^
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ id : int = X
      └─ num : int = 2
    └─ pow : int = ^
      ├─ id : int = Y
      └─ num : int = 2
  └─ num : real = 0.5
```

## Expressão 44

**Tipo inferido:** `None`

```
mult = *
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  └─ gt : booleano = >
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 45

**Tipo inferido:** `None`

```
mult = *
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ num : int = 0
    └─ gt : booleano = >
      ├─ id : int = Y
      └─ num : int = 0
  └─ gt : booleano = >
    ├─ id : int = Z
    └─ num : int = 0
```

## Expressão 46

**Tipo inferido:** `None`

```
mult = *
  ├─ gte : booleano = >=
    ├─ id : int = X
    └─ id : int = Y
  └─ lte : booleano = <=
    ├─ id : int = X
    └─ id : int = Z
```

## Expressão 47

**Tipo inferido:** `None`

```
mult = *
  ├─ neq : booleano = !=
    ├─ id : int = X
    └─ id : int = Y
  └─ neq : booleano = !=
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 48

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ minus : int = -
    ├─ id : int = Z
    └─ num : int = 10
```

## Expressão 49

**Tipo inferido:** `int`

```
minus : int = -
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ id : int = X
      └─ num : int = 2
    └─ pow : int = ^
      ├─ id : int = Y
      └─ num : int = 2
  └─ pow : int = ^
    ├─ id : int = Z
    └─ num : int = 2
```

## Expressão 50

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ mult : real = *
      ├─ id : real = PI
      └─ id : int = X
    └─ num : int = 2
  └─ div_int = /
    ├─ mult : real = *
      ├─ id : real = E
      └─ id : int = Y
    └─ num : int = 3
```

## Expressão 51

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

## Expressão 52

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ num : int = 100
  └─ mod : int = %
    ├─ id : int = Y
    └─ num : int = 100
```

## Expressão 53

**Tipo inferido:** `None`

```
plus = +
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ id : int = Y
    └─ num : int = 1
  └─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = Z
      └─ id : int = Y
    └─ num : int = 1
```

## Expressão 54

**Tipo inferido:** `None`

```
eq = ==
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ num : int = 0
    └─ gt : booleano = >
      ├─ id : int = Y
      └─ num : int = 0
  └─ num : int = 1
```

## Expressão 55

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = A
```

## Expressão 56

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = B
```

## Expressão 57

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 3
  └─ id = C
```

## Expressão 58

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 4
  └─ id = D
```

## Expressão 59

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = F
```

## Expressão 60

**Tipo inferido:** `int`

```
plus : int = +
  ├─ plus : int = +
    ├─ plus : int = +
      ├─ plus : int = +
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 61

**Tipo inferido:** `int`

```
mult : int = *
  ├─ mult : int = *
    ├─ mult : int = *
      ├─ mult : int = *
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 62

**Tipo inferido:** `int`

```
minus : int = -
  ├─ minus : int = -
    ├─ minus : int = -
      ├─ minus : int = -
        ├─ id : int = F
        └─ id : int = D
      └─ id : int = C
    └─ id : int = B
  └─ id : int = A
```

## Expressão 63

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ div_int : int = /
    ├─ div_int : int = /
      ├─ div_int : int = /
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 64

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = A
    └─ id : int = B
  ├─ if : int = if
    ├─ lt : booleano = <
      ├─ id : int = C
      └─ id : int = D
    ├─ num : int = 1
    └─ num : int = 2
  └─ num : int = 3
```

## Expressão 65

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ num : int = 0
  ├─ if : int = if
    ├─ gt : booleano = >
      ├─ id : int = B
      └─ num : int = 0
    ├─ plus : int = +
      ├─ id : int = A
      └─ id : int = B
    └─ minus : int = -
      ├─ id : int = A
      └─ id : int = B
  └─ num : int = 0
```

## Expressão 66

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 1
  └─ num : int = 3
```

## Expressão 67

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 2
  └─ num : int = 3
```

## Expressão 68

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 5
  └─ num : int = 6
```

## Expressão 69

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 22
  └─ num : int = 7
```

## Expressão 70

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 355
  └─ num : int = 113
```

## Expressão 71

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ id : int = X
```

## Expressão 72

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ plus : int = +
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 73

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ minus : int = -
    ├─ id : int = A
    └─ id : int = B
  └─ num : int = 0
```

## Expressão 74

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 75

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 76

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

## Expressão 77

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

## Expressão 78

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = N
```

## Expressão 79

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

## Expressão 80

**Tipo inferido:** `int`

```
id : int = N
```

## Expressão 81

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = SOMA
```

## Expressão 82

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = I
```

## Expressão 83

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

## Expressão 84

**Tipo inferido:** `int`

```
id : int = SOMA
```

## Expressão 85

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

## Expressão 86

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Y
    └─ num : int = 2
```

## Expressão 87

**Tipo inferido:** `int`

```
plus : int = +
  ├─ div_int : int = /
    ├─ num : int = 100
    └─ num : int = 7
  └─ mod : int = %
    ├─ num : int = 100
    └─ num : int = 7
```

## Expressão 88

**Tipo inferido:** `real`

```
mult : real = *
  ├─ id : real = PI
  └─ pow : int = ^
    ├─ num : int = 5
    └─ num : int = 2
```

## Expressão 89

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ num : int = 2
    └─ id : real = PI
  └─ num : int = 5
```

## Expressão 90

**Tipo inferido:** `int`

```
mult : int = *
  ├─ mult : int = *
    ├─ num : int = 10
    └─ num : int = 20
  └─ num : int = 2
```

## Expressão 91

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ num : int = 10
    └─ num : int = 20
  └─ num : int = 2
```

## Expressão 92

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ id : int = X
  └─ plus : int = +
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 93

**Tipo inferido:** `None`

```
pow = ^
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ plus : int = +
        ├─ id : int = A
        └─ id : int = B
      └─ num : int = 2
    └─ pow : int = ^
      ├─ plus : int = +
        ├─ id : int = C
        └─ id : int = D
      └─ num : int = 2
  └─ num : real = 0.5
```

## Expressão 94

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ div_int : int = /
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ div_int : int = /
      ├─ id : int = Y
      └─ id : int = Z
  └─ div_int : int = /
    ├─ id : int = Z
    └─ id : int = X
```

## Expressão 95

**Tipo inferido:** `None`

```
minus = -
  ├─ pow = ^
    ├─ id : real = PI
    └─ id : real = E
  └─ pow = ^
    ├─ id : real = E
    └─ id : real = PI
```

## Expressão 96

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = D
      └─ id : int = F
    └─ id : int = A
```

## Expressão 97

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 1.0
  └─ id = A
```

## Expressão 98

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 5.0
  └─ id = B
```

## Expressão 99

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 2.0
  └─ id = C
```

## Expressão 100

**Tipo inferido:** `real`

```
minus : real = -
  ├─ mult : real = *
    ├─ id : real = B
    └─ id : real = B
  └─ mult : real = *
    ├─ num : int = 4
    └─ id : real = A
```

## Expressão 101

**Tipo inferido:** `None`

```
res = RES
  └─ id = DELTA
```

## Expressão 102

**Tipo inferido:** `int`

```
num : int = 0
```

## Expressão 103

**Tipo inferido:** `int`

```
num : int = 0
```

## Expressão 104

**Tipo inferido:** `int`

```
num : int = 0
```

## Expressão 105

**Tipo inferido:** `int`

```
num : int = 0
```

## Expressão 106

**Tipo inferido:** `int`

```
num : int = 0
```

## Expressão 107

**Tipo inferido:** `None`

```
if = if
  ├─ lt = <
    ├─ id = DELTA
    └─ num : int = 0
  ├─ num : int = 0
  └─ num : int = 1
```

## Expressão 108

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = R
```

## Expressão 109

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 3.14159
  └─ id = PI
```

## Expressão 110

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ id : real = PI
    └─ id : int = R
  └─ id : int = R
```

## Expressão 111

**Tipo inferido:** `None`

```
res = RES
  └─ id = AREA
```

## Expressão 112

**Tipo inferido:** `real`

```
mult : real = *
  ├─ div_int : int = /
    ├─ num : int = 4
    └─ num : int = 3
  └─ id : real = PI
```

## Expressão 113

**Tipo inferido:** `None`

```
res = RES
  └─ id = TEMP
```

## Expressão 114

**Tipo inferido:** `None`

```
mult = *
  ├─ mult = *
    ├─ id = TEMP
    └─ id : int = R
  └─ id : int = R
```

## Expressão 115

**Tipo inferido:** `None`

```
res = RES
  └─ id = QUASE_VOL
```

## Expressão 116

**Tipo inferido:** `None`

```
mult = *
  ├─ id = QUASE_VOL
  └─ id : int = R
```

## Expressão 117

**Tipo inferido:** `None`

```
res = RES
  └─ id = VOLUME
```

## Expressão 118

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = X
```

## Expressão 119

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 20
  └─ id = Y
```

## Expressão 120

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 30
  └─ id = Z
```

## Expressão 121

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = X
  └─ id : int = Y
```

## Expressão 122

**Tipo inferido:** `int`

```
mult : int = *
  ├─ id : int = X
  └─ id : int = Y
```

## Expressão 123

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ id : int = Z
  └─ res : int = RES
    └─ num : int = 1
```

## Expressão 124

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ id : int = Z
  └─ res : int = RES
    └─ num : int = 2
```

## Expressão 125

**Tipo inferido:** `None`

```
minus = -
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ id : int = X
      └─ id : int = Y
    └─ plus : int = +
      ├─ id : int = Z
      └─ num : int = 10
  └─ div_int = /
    ├─ plus : real = +
      ├─ id : real = A
      └─ id : real = B
    └─ mult : real = *
      ├─ id : real = C
      └─ num : int = 1
```

## Expressão 126

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = I
```

## Expressão 127

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = FAT
```

## Expressão 128

**Tipo inferido:** `int`

```
while : int = while
  ├─ gt : booleano = >
    ├─ id : int = I
    └─ num : int = 0
  └─ mult : int = *
    ├─ store : int
      ├─ mult : int = *
        ├─ id : int = FAT
        └─ id : int = I
      └─ id = FAT
    └─ store : int
      ├─ minus : int = -
        ├─ id : int = I
        └─ num : int = 1
      └─ id = I
```

## Expressão 129

**Tipo inferido:** `int`

```
id : int = FAT
```

## Expressão 130

**Tipo inferido:** `None`

```
if = if
  ├─ gt : booleano = >
    ├─ id : int = FAT
    └─ num : int = 100
  ├─ id = AREA
  └─ id = VOLUME
```

## Expressão 131

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = LIMITE
```

## Expressão 132

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = CONTADOR
```

## Expressão 133

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = SOMA
```

## Expressão 134

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = CONTADOR
    └─ id : int = LIMITE
  └─ store : int
    ├─ plus : int = +
      ├─ id : int = SOMA
      └─ id : int = CONTADOR
    └─ id = SOMA
```

## Expressão 135

**Tipo inferido:** `int`

```
id : int = SOMA
```

## Expressão 136

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ plus : int = +
    ├─ div_int : int = /
      ├─ id : int = SOMA
      └─ num : int = 2
    └─ div_int : int = /
      ├─ id : int = FAT
      └─ num : int = 2
  └─ num : real = 500.5
```

