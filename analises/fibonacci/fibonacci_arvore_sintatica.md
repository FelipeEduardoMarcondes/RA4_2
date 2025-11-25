# Árvore Sintática Atribuída - testes/fibonacci.txt

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
  ├─ num : int = 0
  └─ id = I
```

## Expressão 4

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 23
  └─ id = N
```

## Expressão 5

**Tipo inferido:** `int`

```
id : int = A
```

## Expressão 6

**Tipo inferido:** `int`

```
id : int = B
```

## Expressão 7

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ id : int = N
  └─ if : int = if
    ├─ gt : booleano = >
      ├─ plus : int = +
        ├─ plus : int = +
          ├─ store : int
            ├─ plus : int = +
              ├─ id : int = A
              └─ id : int = B
            └─ id = TEMP
          └─ store : int
            ├─ id : int = B
            └─ id = A
        └─ plus : int = +
          ├─ store : int
            ├─ id : int = TEMP
            └─ id = B
          └─ store : int
            ├─ plus : int = +
              ├─ id : int = I
              └─ num : int = 1
            └─ id = I
      └─ num : int = 0
    ├─ id : int = B
    └─ id : int = B
```

