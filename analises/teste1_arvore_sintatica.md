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
  ├─ num : int = 0
  └─ id = CONT
```

## Expressão 4

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = TEMP
```

## Expressão 5

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = CONT
    └─ num : int = 12
  └─ plus : int = +
    ├─ store : int
      ├─ plus : int = +
        ├─ id : int = A
        └─ id : int = B
      └─ id = TEMP
    └─ plus : int = +
      ├─ store : int
        ├─ id : int = B
        └─ id = A
      └─ plus : int = +
        ├─ store : int
          ├─ id : int = TEMP
          └─ id = B
        └─ plus : int = +
          ├─ store : int
            ├─ plus : int = +
              ├─ id : int = CONT
              └─ num : int = 1
            └─ id = CONT
          └─ id : int = A
```

## Expressão 6

**Tipo inferido:** `int`

```
id : int = A
```

