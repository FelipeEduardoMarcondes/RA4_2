# Relatório de Geração de Assembly AVR

**Compilador RPN - Arduino Uno (ATmega328P)**

## Estatísticas

- **Instruções TAC:** 16
- **Linhas Assembly:** 147
- **Arquitetura:** ATmega328P (8-bit, 16MHz)
- **Precisão numérica:** 16-bit signed integer

## Implementação

### Operação PRINT[X]
```
1. Carrega X em R25:R24
2. Chama print_int16 (converte para decimal)
3. Chama uart_newline (envia CR+LF)
4. Armazena resultado (mesmo valor impresso)
```

### Operação RES(N)
```
1. Valida N (1 <= N <= número de linhas)
2. Recupera resultado de N linhas atrás
3. Carrega valor em R25:R24
4. Armazena em variável destino
```

### Convenção de Registradores

| Registrador | Uso |
|-------------|-----|
| R0-R1 | Multiplicação (mul) e zero |
| R16-R23 | Temporários |
| R24-R25 | Operando 1 / Retorno |
| R22-R23 | Operando 2 |
| R26-R27 (X) | Ponteiro |
| R30-R31 (Z) | Ponteiro de programa |

## Funções da Biblioteca

- `uart_init`: Inicializa UART 9600 baud
- `uart_tx`: Transmite um byte
- `uart_newline`: Envia CR+LF
- `print_int16`: Imprime inteiro 16-bit com sinal
- `mul16u`: Multiplicação 16x16=16 bit
- `div16u`: Divisão 16-bit unsigned
- `mod16u`: Módulo 16-bit
- `pow16u`: Potência 16-bit

