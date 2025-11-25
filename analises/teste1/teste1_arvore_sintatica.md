# Árvore Sintática Atribuída - testes/teste1.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
num : int = -5
```

## Expressão 2

**Tipo inferido:** `int`

```
num : int = -10
```

## Expressão 3

**Tipo inferido:** `int`

```
plus : int = +
  ├─ num : int = -5
  └─ num : int = -3
```

## Expressão 4

**Tipo inferido:** `real`

```
mult : real = *
  ├─ num : int = 10
  └─ num : real = -2.5
```

## Expressão 5

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 100
  └─ num : real = -2.52
```

## Expressão 6

**Tipo inferido:** `real`

```
res : real = RES
  └─ num : int = 1
```

## Expressão 7

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 4
```

