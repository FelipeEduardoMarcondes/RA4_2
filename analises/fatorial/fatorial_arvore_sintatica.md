# Árvore Sintática Atribuída - testes/fatorial.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
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
  ├─ gt : booleano = >
    ├─ id : int = N
    └─ num : int = 1
  ├─ store : int
    ├─ mult : int = *
      ├─ id : int = FAT
      └─ id : int = N
    └─ id = FAT
  └─ store
    ├─ minus = -
      ├─ id = N
      └─ num = 1
    └─ id = N
```

## Expressão 4

**Tipo inferido:** `int`

```
id : int = FAT
```

