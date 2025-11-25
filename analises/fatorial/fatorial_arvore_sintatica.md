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
id : int = FAT
```

