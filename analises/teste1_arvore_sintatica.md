# Árvore Sintática Atribuída - .\teste1.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A
```

## Expressão 2

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = B
```

## Expressão 3

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = N
```

## Expressão 4

**Tipo inferido:** `None`

```
res = RES
  └─ id : int = A
```

## Expressão 5

**Tipo inferido:** `None`

```
res = RES
  └─ id : int = B
```

## Expressão 6

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 24
  └─ id = MAX
```

## Expressão 7

**Tipo inferido:** `None`

```
while = while
  ├─ lt : booleano = <
    ├─ id : int = N
    └─ id : int = MAX
  └─ plus = +
    ├─ plus = +
      ├─ plus = +
        ├─ store : int
          ├─ plus : int = +
            ├─ id : int = A
            └─ id : int = B
          └─ id = C
        └─ res = RES
          └─ id : int = C
      └─ plus : int = +
        ├─ store : int
          ├─ id : int = B
          └─ id = A
        └─ store : int
          ├─ id : int = C
          └─ id = B
    └─ store : int
      ├─ plus : int = +
        ├─ id : int = N
        └─ num : int = 1
      └─ id = N
```

