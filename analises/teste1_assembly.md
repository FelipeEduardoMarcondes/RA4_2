# Relatório Assembly
Gerado com suporte a RES (Histórico de Resultados).

## Implementação de RES

O comando `(N RES)` recupera o resultado da expressão N linhas anteriores.

**Implementação:**
1. Durante análise do TAC, rastreia variável final de cada linha
2. Armazena em array `res_history[]`
3. `RES(N)` carrega valor de `res_history[-N]`
4. Imprime valor com `print_int16`

