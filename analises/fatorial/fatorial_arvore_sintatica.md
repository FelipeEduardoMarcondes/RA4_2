# Árvore Sintática Atribuída - testes/fatorial.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = N
```

## Expressão 2

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = FAT
```

## Expressão 3

**Tipo inferido:** `int`

```
while : int = while
  ├─ lte : booleano = <=
    ├─ id : int = N
    └─ num : int = 8
  └─ mult : int = *
    ├─ store : int
      ├─ mult : int = *
        ├─ id : int = FAT
        └─ id : int = N
      └─ id = FAT
    └─ store : int
      ├─ plus : int = +
        ├─ id : int = N
        └─ num : int = 1
      └─ id = N
```

## Expressão 4

**Tipo inferido:** `int`

```
store : int
  ├─ id : int = FAT
  └─ id = RESULTADO
```

## Expressão 5

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = NUM
```

## Expressão 6

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = FATORIAL1
```

## Expressão 7

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = NUM
```

## Expressão 8

**Tipo inferido:** `int`

```
mult : int = *
  ├─ num : int = 1
  └─ num : int = 2
```

## Expressão 9

**Tipo inferido:** `int`

```
store : int
  ├─ res : int = RES
    └─ num : int = 1
  └─ id = FATORIAL2
```

## Expressão 10

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 3
  └─ id = NUM
```

## Expressão 11

**Tipo inferido:** `int`

```
mult : int = *
  ├─ num : int = 2
  └─ id : int = FATORIAL2
```

## Expressão 12

**Tipo inferido:** `int`

```
store : int
  ├─ res : int = RES
    └─ num : int = 1
  └─ id = FATORIAL3
```

