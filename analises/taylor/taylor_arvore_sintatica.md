# Árvore Sintática Atribuída - .\testes\taylor.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 0.5
  └─ id = X_VAL
```

## Expressão 2

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 1.0
  └─ id = T1
```

## Expressão 3

**Tipo inferido:** `real`

```
store : real
  ├─ div_real : real = |
    ├─ pow : real = ^
      ├─ id : real = X_VAL
      └─ num : int = 2
    └─ num : real = 2.0
  └─ id = T2
```

## Expressão 4

**Tipo inferido:** `real`

```
store : real
  ├─ div_real : real = |
    ├─ pow : real = ^
      ├─ id : real = X_VAL
      └─ num : int = 4
    └─ num : real = 24.0
  └─ id = T3
```

## Expressão 5

**Tipo inferido:** `real`

```
store : real
  ├─ div_real : real = |
    ├─ div_real : real = |
      ├─ pow : real = ^
        ├─ id : real = X_VAL
        └─ num : int = 6
      └─ num : real = 24.0
    └─ num : real = 30.0
  └─ id = T4
```

## Expressão 6

**Tipo inferido:** `real`

```
store : real
  ├─ minus : real = -
    ├─ plus : real = +
      ├─ minus : real = -
        ├─ id : real = T1
        └─ id : real = T2
      └─ id : real = T3
    └─ id : real = T4
  └─ id = FINAL_COS
```

## Expressão 7

**Tipo inferido:** `real`

```
id : real = FINAL_COS
```

