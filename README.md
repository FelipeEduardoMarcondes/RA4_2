# Gramática LL(1) para Linguagem RPN

**Autor:** FELIPE EDUARDO MARCONDES  
**Grupo:** 2  
**Universidade:** Pontifícia Universidade Católica do Paraná (PUCPR)  
**Disciplina:** Linguagens Formais e Compiladores  
**Professor:** Frank Coelho de Alcantara  
**Ano:** 2025

---

## 1. Visão Geral

Este projeto implementa um compilador completo para uma linguagem de programação simplificada em **Notação Polonesa Reversa (RPN)**, incluindo todas as fases de compilação desde a análise léxica até a geração de código executável para microcontroladores AVR (Arduino).

**Características principais:**
- Expressões em notação pós-fixada: `(A B op)`
- Operações aritméticas e relacionais
- Estruturas de controle (`IF`, `WHILE`)
- Comandos de memória (identificadores em maiúsculas, `RES`)
- Aninhamento ilimitado de expressões
- Verificação de tipos e análise semântica completa
- Geração de código intermediário (TAC - Three Address Code)
- Otimizações de código
- Compilação para Assembly AVR (ATmega328P)
- Suporte para ponto fixo Q8.8 (256 = 1.0)
- Upload automático para Arduino
- Saída via Serial (9600 baud)
- Geração automática de relatórios em Markdown e JSON

---

## 2. Arquitetura do Compilador

### 2.1 Fases de Compilação

```
┌───────────────┐
│ Código Fonte  │
│   (RPN .txt)  │
└───────┬───────┘
        │
        v
┌───────────────┐
│  FASE 1       │
│  Análise      │
│  Léxica       │
│  (leitor.py)  │
└───────┬───────┘
        │ Tokens
        v
┌───────────────┐
│  FASE 2       │
│  Análise      │
│  Sintática    │
│  (parser.py)  │
└───────┬───────┘
        │ AST
        v
┌───────────────┐
│  FASE 3       │
│  Análise      │
│  Semântica    │
│(semantico.py) │
└───────┬───────┘
        │ AST Atribuída
        v
┌───────────────┐
│  FASE 4       │
│  Geração TAC  │
│(tac_gen.py)   │
└───────┬───────┘
        │ TAC
        v
┌───────────────┐
│  FASE 4.1     │
│  Otimização   │
│(otimizador.py)│
└───────┬───────┘
        │ TAC Otimizado
        v
┌───────────────┐
│  FASE 4.2     │
│  Geração ASM  │
│(assembly_gen) │
└───────┬───────┘
        │ Assembly AVR
        v
┌───────────────┐
│  FASE 4.3     │
│  Compilação   │
│  (avr-gcc)    │
└───────┬───────┘
        │ Hex
        v
┌───────────────┐
│  Upload       │
│  (avrdude)    │
└───────────────┘
```

### 2.2 Bibliotecas AVR

O compilador gera código que utiliza as seguintes bibliotecas customizadas:

- **uart.s**: Comunicação serial (9600 baud)
- **math_core.s**: Aritmética unsigned (multiplicação, divisão)
- **math_signed.s**: Aritmética signed e impressão decimal
- **math_fixed.s**: Aritmética de ponto fixo Q8.8
- **runtime.s**: Operadores relacionais e wrappers
- **storage.s**: Gerenciamento de memória (RES e MEM)

---

## 3. Requisitos

### 3.1 Software Necessário

**Python 3.8 ou superior**
```bash
python --version
# ou
python3 --version
```

**Toolchain AVR (para compilação Assembly)**
```bash
# Ubuntu/Debian
sudo apt-get install gcc-avr binutils-avr avr-libc avrdude

# macOS (via Homebrew)
brew tap osx-cross/avr
brew install avr-gcc avrdude

# Windows
# Baixar WinAVR ou Arduino IDE (que inclui as ferramentas)
```

**Arduino Uno R3 ou compatível** (opcional, para execução)

### 3.2 Estrutura de Arquivos

```
.
├── compilar.py          # Programa principal
├── config.py            # Configurações (porta, baud rate, etc)
├── leitor.py            # Analisador léxico
├── parser.py            # Analisador sintático
├── semantico.py         # Analisador semântico
├── tac_generator.py     # Gerador de TAC
├── otimizador.py        # Otimizador de TAC
├── assembly_generator.py # Gerador de Assembly AVR
├── monitor_serial.py    # Monitor serial para debug
├── readme.md            # Este arquivo
├── atributos.md         # Gramática de atributos
├── lib_avr/             # Bibliotecas AVR
│   ├── uart.s
│   ├── math_core.s
│   ├── math_signed.s
│   ├── math_fixed.s
│   ├── runtime.s
│   └── storage.s
├── teste1.txt           # Arquivo de teste 1
├── teste2.txt           # Arquivo de teste 2
├── teste3.txt           # Arquivo de teste 3
└── analises/            # Diretório de saída
```

---

## 4. Configuração

### 4.1 Arquivo config.py

Edite `config.py` para ajustar as configurações do seu sistema:

```python
# Porta Serial (Windows: "COM3", Linux: "/dev/ttyACM0")
PORTA_SERIAL = "/dev/ttyACM0"

# Baud Rates
BAUD_RATE_UPLOAD = 115200  # Para upload
BAUD_RATE_MONITOR = 9600   # Para serial monitor

# Ponto Fixo (256 = 1.0 em Q8.8)
SCALE_FACTOR = 256

# Upload Automático após compilação
AUTO_UPLOAD = True  # True para upload automático

# Otimizações
ENABLE_OPTIMIZATIONS = True

# Diretório de saída
OUTPUT_DIR = "analises"
```

---

## 5. Execução

### 5.1 Compilação Básica

```bash
python compilar.py <arquivo_de_teste.txt>
```

### 5.2 Exemplos

**Compilar teste 1:**
```bash
python compilar.py teste1.txt
```

**Compilar teste 2:**
```bash
python compilar.py teste2.txt
```

**Compilar teste 3:**
```bash
python compilar.py teste3.txt
```

### 5.3 Saída Esperada

O programa exibirá no console:

```
============================================================
COMPILANDO: teste1.txt
============================================================

[FASE 1] Análise Léxica...
[OK] 15 token(s) identificado(s)

[FASE 2] Análise Sintática...
[OK] 5 expressão(ões) válida(s)

[FASE 3] Análise Semântica...
[OK] Nenhum erro semântico detectado

[FASE 4] Geração de Código Intermediário (TAC)...
[OK] 23 instruções TAC geradas

[FASE 4.1] Otimizando código TAC...
[OK] 8 otimizações aplicadas:
  - Constant Folding: 3
  - Constant Propagation: 2
  - Dead Code Elimination: 3
[OK] Redução: 5 instruções (21.7%)

[FASE 4.2] Gerando código Assembly AVR...
[OK] 156 linhas de Assembly geradas

[FASE 4.3] Compilando Assembly para HEX...
[OK] Assembly salvo: analises/teste1/teste1.s
Compilando ELF...
Gerando HEX...
[OK] HEX gerado com sucesso: analises/teste1/teste1.hex

[UPLOAD] Fazendo upload para /dev/ttyACM0...
[OK] Upload concluído!

[INFO] Abra o monitor serial em 9600 baud para ver os resultados

[SAÍDA] Gerando relatórios...
  - analises/teste1/gramatica_atributos_gerada.md
  - analises/teste1/teste1_julgamento_tipos.md
  - analises/teste1/teste1_erros_semanticos.md
  - analises/teste1/teste1_arvore_atribuida.json
  - analises/teste1/teste1_arvore_sintatica.md
  - analises/teste1/teste1_tac.txt
  - analises/teste1/teste1_tac_otimizado.txt
  - analises/teste1/teste1_otimizacoes.md
  - analises/teste1/teste1_assembly.md

============================================================
RESUMO DA COMPILAÇÃO
============================================================
Tokens processados:          15
Expressões analisadas:       5
Variáveis declaradas:        3
Erros semânticos:            0
Instruções TAC (original):   23
Instruções TAC (otimizado):  18
Otimizações aplicadas:       8
Linhas Assembly geradas:     156

[STATUS] COMPILAÇÃO BEM-SUCEDIDA
============================================================
```

### 5.4 Arquivos Gerados

Para cada arquivo compilado, é criado um subdiretório em `analises/` contendo:

| Arquivo | Descrição |
|---------|-----------|
| `gramatica_atributos_gerada.md` | Gramática de atributos |
| `<arquivo>_julgamento_tipos.md` | Relatório de tipos |
| `<arquivo>_erros_semanticos.md` | Relatório de erros |
| `<arquivo>_arvore_atribuida.json` | AST em JSON |
| `<arquivo>_arvore_sintatica.md` | AST em Markdown |
| `<arquivo>_tac.txt` | TAC original |
| `<arquivo>_tac_otimizado.txt` | TAC otimizado |
| `<arquivo>_otimizacoes.md` | Relatório de otimizações |
| `<arquivo>.s` | Código Assembly AVR |
| `<arquivo>.hex` | Binário para upload |
| `<arquivo>_assembly.md` | Relatório Assembly |

---

## 6. Otimizações de Código

### 6.1 Tipos de Otimizações Implementadas

#### 6.1.1 Constant Folding (Dobramento de Constantes)

Avalia expressões constantes em tempo de compilação.

**Exemplo:**
```
Antes: t1 = 2 + 3
Depois: t1 = 5
```

**Benefícios:**
- Reduz instruções em tempo de execução
- Economiza ciclos de CPU
- Reduz uso de registradores

#### 6.1.2 Constant Propagation (Propagação de Constantes)

Propaga valores constantes através do código.

**Exemplo:**
```
Antes:
  t1 = 5
  t2 = t1 + 3

Depois:
  t1 = 5
  t2 = 5 + 3
  (que será reduzido para t2 = 8 por constant folding)
```

#### 6.1.3 Dead Code Elimination (Eliminação de Código Morto)

Remove código que não afeta o resultado do programa.

**Exemplo:**
```
Antes:
  t1 = 5
  t2 = 3       # t2 nunca é usado
  t3 = t1 + 2
  PRINT[t3]

Depois:
  t1 = 5
  t3 = t1 + 2
  PRINT[t3]
```

**IMPORTANTE:** Preserva instruções com efeitos colaterais:
- `PRINT[...]`
- `MEM[...]`
- `RES[...]`
- Estruturas de controle

#### 6.1.4 Redundant Jump Elimination (Eliminação de Saltos Redundantes)

Remove saltos para a próxima instrução.

**Exemplo:**
```
Antes:
  goto L1
  L1:

Depois:
  L1:
```

### 6.2 Estatísticas de Otimização

O compilador gera relatório detalhado mostrando:
- Número de otimizações de cada tipo
- Redução total de instruções
- Percentual de redução
- Comparação código original vs otimizado

---

## 7. Geração de Assembly AVR

### 7.1 Características

- **Arquitetura alvo:** ATmega328P (Arduino Uno)
- **Ponto fixo:** Q8.8 (256 = 1.0)
- **Stack:** 512 bytes (SPH:SPL = 0x08FF)
- **Serial:** 9600 baud, 8N1
- **Precisão:** 16 bits signed/unsigned

### 7.2 Mapeamento TAC → Assembly

#### Operações Aritméticas

| TAC | Assembly |
|-----|----------|
| `t1 = t2 + t3` | `add r24, r22` + `adc r25, r23` |
| `t1 = t2 - t3` | `sub r24, r22` + `sbc r25, r23` |
| `t1 = t2 * t3` | `call fx_mul` (Q8.8) |
| `t1 = t2 \| t3` | `call fx_div` (Q8.8) |
| `t1 = t2 / t3` | `call div16s` (inteiro) |
| `t1 = t2 % t3` | `call op_mod` |
| `t1 = t2 ^ t3` | `call fx_pow` |

#### Operações Relacionais

| TAC | Assembly |
|-----|----------|
| `t1 = t2 == t3` | `call op_eq` |
| `t1 = t2 != t3` | `call op_neq` |
| `t1 = t2 < t3` | `call op_lt` |
| `t1 = t2 > t3` | `call op_gt` |
| `t1 = t2 <= t3` | `call op_le` |
| `t1 = t2 >= t3` | `call op_ge` |

#### Memória

| TAC | Assembly |
|-----|----------|
| `t1 = MEM[X]` | `lds r24, X` + `lds r25, X+1` |
| `MEM[X] = t1` | `sts X, r24` + `sts X+1, r25` |
| `t1 = RES[N]` | `call res_fetch` |
| `PRINT[t1]` | `call fx_print` + `call uart_newline` |

#### Controle de Fluxo

| TAC | Assembly |
|-----|----------|
| `goto L1` | `rjmp L1` |
| `ifFalse t1 goto L1` | `or r24, r25` + `breq L1` |
| `L1:` | `L1:` |

### 7.3 Convenções de Registradores

| Registrador | Uso |
|-------------|-----|
| R24:R25 | Operando A / Retorno |
| R22:R23 | Operando B |
| R20:R21 | Temporários |
| R18:R19 | Temporários |
| R0:R1 | Resultado MUL (zerado após uso) |
| R14:R15 | Resto de divisões |

---

## 8. Monitor Serial

### 8.1 Uso Básico

```bash
python monitor_serial.py
```

### 8.2 Detecção Automática de Porta

O monitor tenta automaticamente:
1. Usar porta padrão do `config.py`
2. Detectar Arduino conectado
3. Solicitar seleção manual se necessário

### 8.3 Formato de Saída

```
[   0.00s] 8.000
[   0.05s] 13.000
[   0.10s] 5.000
[   0.15s] 2.600
```

Formato: `[timestamp] valor`

---

## 9. Símbolos Terminais

### 9.1 Delimitadores
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `lparen` | `(` | Abre parênteses |
| `rparen` | `)` | Fecha parênteses |

### 9.2 Operadores Aritméticos
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `plus`    | `+` | Adição |
| `minus`   | `-` | Subtração |
| `mult`    | `*` | Multiplicação |
| `div_real`| `|`| Divisão real (ponto flutuante) |
| `div_int` | `/` | Divisão inteira |
| `mod`     | `%` | Módulo (resto da divisão) |
| `pow`     | `^` | Potenciação |

### 9.3 Operadores Relacionais
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `eq`  | `==` | Igualdade |
| `neq` | `!=` | Diferença |
| `lt`  | `<` | Menor que |
| `gt`  | `>` | Maior que |
| `lte` | `<=` | Menor ou igual |
| `gte` | `>=` | Maior ou igual |

### 9.4 Operandos e Keywords
| Terminal | Símbolo | Descrição |
|----------|---------|-----------|
| `num`   | N/A | Literal numérico (int ou real) |
| `id`    | N/A | Identificador em MAIÚSCULAS (ex: `X`, `MEM`, `CONTADOR`) |
| `res`   | `RES` | Keyword para histórico (sempre maiúsculo) |
| `if`    | `if` | Keyword condicional |
| `while` | `while` | Keyword laço |
| `eof`   | N/A | Fim de arquivo |

---

## 10. Produções da Gramática LL(1)

```ebnf
PROGRAM -> LINE PROGRAM 
        | ε

LINE -> lparen STMT rparen

STMT -> EXPR STMT_TAIL

STMT_TAIL -> EXPR STMT_TAIL2           
          | OP_BIN                    
          | ε                         

STMT_TAIL2 -> OP_BIN                   
           | CONTROL                  
           | EXPR CONTROL             
           | ε                        
           
CONTROL -> if                          
        | while                       

EXPR -> num
     | id
     | res
     | lparen STMT rparen

OP_BIN -> plus | minus | mult | div_real | div_int | mod | pow
       | eq | neq | lt | gt | lte | gte
```

---

## 11. Semântica da Linguagem

### 11.1 Operações Binárias
Formato: `(A B op)`

**Exemplos:**
```
(3 5 +)           -> 3 + 5 = 8.000
(10 3 /)          -> 10 / 3 = 3 (divisão inteira)
(10.0 3.0 |)      -> 10.0 / 3.0 = 3.333 (divisão real)
(2 8 ^)           -> 2^8 = 256.000
```

### 11.2 Comandos de Memória

#### Armazenamento: `(valor ID)`
```
(42 X)            -> Armazena 42 em X
(3.14 PI)         -> Armazena 3.14 em PI
```

#### Recuperação: `(ID)`
```
(X)               -> Retorna valor de X
```

#### Histórico: `(N RES)`
```
Linha 1: (3 5 +)         -> resultado = 8
Linha 2: (1 RES)         -> retorna 8 (linha anterior)
Linha 3: (2 RES)         -> retorna 8 (duas linhas antes)
```

### 11.3 Estruturas de Controle

#### Condicional: `(condição then else if)`
```
((X 0 >) (X) (0 X -) if)
-> Se X > 0 retorna X, senão retorna -X (valor absoluto)
```

#### Laço: `(condição corpo while)`
```
((I 10 <) ((I 1 +) I) while)
-> Incrementa I enquanto I < 10
```

---

## 12. Tipos de Dados

### 12.1 Tipos Suportados

| Tipo | Descrição | Representação |
|------|-----------|---------------|
| `int` | Inteiros | 16 bits signed (-32768 a 32767) |
| `real` | Ponto fixo | Q8.8 (8 bits inteiros + 8 bits fracionários) |
| `booleano` | Lógico | 0 (false) ou 1 (true) |

### 12.2 Ponto Fixo Q8.8

**Formato:** 16 bits = 8 bits inteiros + 8 bits fracionários

**Escala:** 256 (2^8)

**Exemplos:**
```
1.0   = 256  (0x0100)
0.5   = 128  (0x0080)
2.5   = 640  (0x0280)
-1.0  = -256 (0xFF00 em complemento de 2)
```

**Faixa:**
- Inteiros: -128 a 127
- Fracionários: 0 a 0.996 (255/256)
- Total: -128.000 a 127.996

**Precisão:** ~0.004 (1/256)

### 12.3 Regras de Tipo

1. **Operações aritméticas com tipos mistos:** Promovem para `real`
   - `int + real -> real`
   - `int * real -> real`

2. **Divisão:**
   - `/` (divisão inteira): Requer ambos operandos `int`, retorna `int`
   - `|` (divisão real): Aceita `int` ou `real`, retorna `real`

3. **Módulo (%):** Requer ambos operandos `int`, retorna `int`

4. **Potenciação (^):** 
   - Base: `int` ou `real`
   - Expoente: **deve ser `int` positivo**
   - Retorno: mesmo tipo da base

5. **Operadores relacionais:** Aceitam `int` ou `real`, retornam `booleano`


### 12.4 Modo Inteiro (PRAGMA)

Para testes que requerem **inteiros puros sem ponto fixo** (como Fatorial e Fibonacci 
com valores grandes), o compilador suporta um **pragma de compilação**:

#### Uso:

Adicione como **primeira linha** do arquivo `.txt`:
```
# MODO: INTEIRO
```

#### Efeito:

- Desabilita ponto fixo Q8.8
- Usa aritmética **unsigned 16-bit** (0 a 65535)
- Operações mais rápidas (sem conversão)
- Evita overflow em multiplicações

#### Exemplo - fatorial.txt:
```
# MODO: INTEIRO

(1 N)
(1 FAT)
((N 8 <=) ((FAT N *) FAT) ((N 1 +) N) while)
(FAT)
```

#### Geração de Assembly:

Com o pragma, o compilador:
1. Carrega valores como **inteiros puros** (escala 1:1)
2. Usa `mul16u` (multiplicação unsigned) em vez de `fx_mul`
3. Usa `print_int16` (impressão unsigned) em vez de `fx_print`

#### Bibliotecas Usadas:

| Modo | Biblioteca | Função Multiplicação |
|------|------------|---------------------|
| **Normal (Q8.8)** | `math_fixed.s` | `fx_mul` (escala 256) |
| **Inteiro (PRAGMA)** | `math_inteiro.s` | `mul16u` (escala 1) |

#### Detecção Automática:
```python
# No compilar.py
def detectarModo(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        primeira_linha = f.readline().upper()
        if "# MODO: INTEIRO" in primeira_linha:
            return True
    return False

# Uso
usar_modo_inteiro = detectarModo(filename)
asm_generator = AVRAssemblyGenerator(int_mode=usar_modo_inteiro)
```

#### Quando Usar:

| Teste | Modo Recomendado | Razão |
|-------|------------------|-------|
| **Fatorial (1-8)** | Inteiro | Valores até 40320 |
| **Fibonacci (24 termos)** | Inteiro | Valores até 46368 |
| **Taylor (cos)** | Q8.8 | Requer frações |
| **Expressões gerais** | Q8.8 | Flexibilidade |

#### Alternativa - Argumento de Linha de Comando:
```bash
python compilar.py --int fatorial.txt
```

Força modo inteiro mesmo sem o pragma no arquivo.

---

## 13. Erros Comuns e Soluções

### 13.1 Erros de Compilação Python

**Erro: "Arquivo não encontrado"**
```bash
# Solução: Verifique se o arquivo existe
ls -la teste1.txt
```

**Erro: "Identificador 'x' deve estar em MAIÚSCULAS"**
```
# Problema: Identificadores devem ser maiúsculos
(42 x)  # Errado
(42 X)  # Correto
```

### 13.2 Erros Semânticos

**Erro: "Memória 'X' utilizada sem inicialização"**
```
(X)     # Errado - X não foi inicializado
(42 X)  # Correto - Inicializa X primeiro
(X)     # Agora pode usar X
```

**Erro: "Divisão por zero"**
```
(10 0 /)  # Errado
(10 2 /)  # Correto
```

**Erro: "Expoente de potenciação deve ser inteiro positivo"**
```
(2 -3 ^)   # Errado - negativo
(2 0 ^)    # Errado - zero
(2 3 ^)    # Correto
```

### 13.3 Erros de Compilação Assembly

**Erro: "avr-gcc: command not found"**
```bash
# Solução: Instalar toolchain AVR

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install gcc-avr binutils-avr avr-libc avrdude

# macOS
brew tap osx-cross/avr
brew install avr-gcc avrdude

# Verificar instalação
avr-gcc --version
```

**Erro: "Undefined reference to 'mul16u'"**
```
# Problema: Bibliotecas AVR não foram incluídas
# Solução: O assembly_generator.py deve incluir todas as libs automaticamente
# Verifique se os arquivos em lib_avr/ existem
ls -la lib_avr/
```

**Erro: "Permission denied" no upload**
```bash
# Linux: Adicionar usuário ao grupo dialout
sudo usermod -a -G dialout $USER
# Fazer logout e login novamente

# Ou dar permissão temporária
sudo chmod 666 /dev/ttyACM0
```

### 13.4 Erros de Hardware

**Arduino não responde**
```bash
# 1. Verificar conexão USB
lsusb  # Linux
system_profiler SPUSBDataType  # macOS

# 2. Testar porta serial
python monitor_serial.py

# 3. Resetar Arduino
# Pressionar botão RESET físico antes do upload
```

**Saída serial com caracteres estranhos**
```
# Problema: Baud rate incorreto
# Solução: Verificar config.py
BAUD_RATE_MONITOR = 9600  # Deve ser 9600
```

**Programa não executa após upload**
```
# Possíveis causas:
1. Código Assembly possui erros lógicos
2. Stack overflow (expressões muito aninhadas)
3. Divisão por zero em tempo de execução
4. Acesso a memória não inicializada

# Debug:
- Adicionar mais chamadas PRINT para rastrear execução
- Verificar TAC gerado
- Simplificar o programa de teste
```

---

## 14. Exemplos de Programas

### 14.1 Exemplo 1: Cálculo Simples

**Arquivo: exemplo1.txt**
```
(3 5 +)
(2 4 *)
(10 3 /)
```

**Saída Esperada:**
```
8.000
8.000
3
```

### 14.2 Exemplo 2: Uso de Memória

**Arquivo: exemplo2.txt**
```
(10 X)
(20 Y)
(X Y +)
```

**Saída Esperada:**
```
10.000
20.000
30.000
```

### 14.3 Exemplo 3: Uso de RES

**Arquivo: exemplo3.txt**
```
(5 3 +)
(1 RES 2 *)
(2 RES 1 RES +)
```

**Saída Esperada:**
```
8.000
16.000
24.000
```

**Explicação:**
- Linha 1: 5 + 3 = 8
- Linha 2: RES[1] * 2 = 8 * 2 = 16
- Linha 3: RES[2] + RES[1] = 8 + 16 = 24

### 14.4 Exemplo 4: Condicional (Valor Absoluto)

**Arquivo: exemplo4.txt**
```
(-5 X)
((X 0 >) (X) (0 X -) if)
```

**Saída Esperada:**
```
-5.000
5.000
```

**Explicação:**
- Linha 1: Armazena -5 em X
- Linha 2: Se X > 0 retorna X, senão retorna -X (valor absoluto)

### 14.5 Exemplo 5: Laço (Soma de 1 a 5)

**Arquivo: exemplo5.txt**
```
(1 I)
(0 SOMA)
((I 5 <=) ((SOMA I +) SOMA) ((I 1 +) I) while)
(SOMA)
```

**Saída Esperada:**
```
1.000
0.000
5.000
15.000
```

**Explicação:**
- Inicializa I = 1, SOMA = 0
- Enquanto I <= 5: SOMA = SOMA + I, I = I + 1
- Resultado: 1 + 2 + 3 + 4 + 5 = 15

### 14.6 Exemplo 6: Fatorial (Pedido no Trabalho)

**Arquivo: fatorial.txt**
```
(1 N)
(1 FAT)
((N 8 <=) ((FAT N *) FAT) ((N 1 +) N) while)
(FAT)
```

**Explicação:**
Calcula fatorial de 1 a 8, imprimindo resultado final.

### 14.7 Exemplo 7: Fibonacci (Pedido no Trabalho)

**Arquivo: fibonacci.txt**
```
(0 A)
(1 B)
(1 I)
(A)
(B)
((I 22 <=) ((A B +) TEMP) (B A) (TEMP B) (TEMP) ((I 1 +) I) while)
```

**Explicação:**
Calcula e imprime os 24 primeiros números da sequência de Fibonacci.

### 14.8 Exemplo 8: Série de Taylor para Cosseno (Pedido no Trabalho)

**Arquivo: taylor.txt**
```
(0.5 X)
(X 2 ^)
(1 RES 2.0 |)
(X 4 ^)
(1 RES 24.0 |)
(X 6 ^)
(1 RES 720.0 |)
(1.0 2 RES - 3 RES + 4 RES -)
```

**Explicação:**
Calcula cos(0.5) usando série de Taylor truncada:
cos(X) ≈ 1 - X²/2! + X⁴/4! - X⁶/6!

**Saída Esperada:** ~0.877 (com perda de precisão em Q8.8)

---

## 15. Testes e Validação

### 15.1 Testes Unitários

**Testar Analisador Léxico:**
```bash
python -c "from leitor import lerTokens; print(lerTokens('teste1.txt'))"
```

**Testar Analisador Sintático:**
```bash
python -c "
from leitor import lerTokens
from parser import parsear, construirGramatica, calcularFirst, calcularFollow, construirTabelaLL1
tokens = lerTokens('teste1.txt')
g = construirGramatica()
f = calcularFirst(g)
fl = calcularFollow(g, f)
t = construirTabelaLL1(g, f, fl)
ast, erros = parsear(tokens, t)
print(f'ASTs: {len(ast)}, Erros: {len(erros)}')
"
```

### 15.2 Validação de Tipos

Verificar se o analisador semântico detecta erros corretamente:

**Teste com erro (divisão inteira com real):**
```
(10.5 3 /)
```

**Erro esperado:**
```
ERRO SEMÂNTICO [Linha 1]: Operador '/' requer operandos inteiros,
encontrado 'real' e 'int'
```

### 15.3 Validação de Otimizações

Comparar instruções TAC antes e depois:

```bash
# Verificar redução de instruções
diff analises/teste1/teste1_tac.txt analises/teste1/teste1_tac_otimizado.txt
```

### 15.4 Validação no Hardware

**Checklist de validação:**
- [x] Assembly compila sem erros
- [x] Upload bem-sucedido
- [x] Monitor serial recebe dados
- [x] Valores corretos são impressos
- [x] Programa não trava/reseta

---

## 16. Limitações Conhecidas

### 16.1 Limitações de Hardware

| Limitação | Valor | Impacto |
|-----------|-------|---------|
| RAM | 2 KB | Limite de variáveis e aninhamento |
| Flash | 32 KB | Tamanho do programa compilado |
| Precisão | 16 bits Q8.8 | Perda de precisão em cálculos |
| Stack | 512 bytes | Profundidade de recursão limitada |

### 16.2 Limitações da Linguagem

- Sem suporte a arrays/vetores
- Sem suporte a strings
- Sem funções definidas pelo usuário
- Sem recursão explícita (apenas via while)
- Ponto fixo limitado a faixa -128 a 127
- Operações de ponto flutuante limitadas (sem sin, cos, exp nativos)

### 16.3 Limitações do Compilador

- Alocação de registradores simplificada (não otimizada)
- Sem análise de fluxo de dados avançada
- Otimizações locais apenas (sem interprocedurais)
- Sem inline de funções
- Sem loop unrolling

## 16.4 Escolha de Representação Numérica: Q8.8 vs IEEE 754

### Por que Q8.8 em vez de IEEE 754 Half Precision?

O documento da Fase 4 especifica **meia precisão IEEE 754 (16 bits)**. 
No entanto, este compilador implementa **Q8.8 (ponto fixo)** pelas seguintes razões:

#### Justificativa Técnica:

1. **Simplicidade de Implementação em AVR**
   - O ATmega328P não possui unidade FPU (Floating Point Unit)
   - IEEE 754 requer emulação via software (bibliotecas pesadas)
   - Q8.8 usa apenas operações inteiras nativas (rápido e compacto)


2. **Trade-offs Aceitáveis para o Projeto**

| Característica | IEEE 754 Half | Q8.8 (Implementado) |
|----------------|---------------|---------------------|
| Faixa | ±65504 | -128 a 127.996 |
| Precisão | ~3 dígitos decimais | ~0.004 (1/256) |
| Operações | Emuladas (lento) | Nativas (rápido) |
| Tamanho código | ~5KB libs | ~1KB libs |
| Adequação aos testes | Overkill | Suficiente |

3. **Adequação aos Testes Pedidos**
   - **Fatorial (1 a 8):** Máximo valor = 40320 Cabe em 16 bits int
   - **Fibonacci (24 termos):** Máximo valor = 46368 Cabe em 16 bits int  
   - **Taylor cos(0.5):** Resultado ~0.877 Cabe em Q8.8

4. **Modo Inteiro como Solução Completa**
   - Para Fatorial e Fibonacci, o compilador usa **modo inteiro puro**
   - Pragma `# MODO: INTEIRO` desabilita ponto fixo
   - Evita overflow e garante precisão exata

### Como o Compilador Escolhe a Representação:
```python
# Detecção automática (compilar.py)
if "# MODO: INTEIRO" in primeira_linha:
    usar_modo_inteiro = True  # Usa int16 unsigned
else:
    usar_modo_inteiro = False  # Usa Q8.8 (ponto fixo)
```


```

### Conclusão:

A escolha de Q8.8 é uma **simplificação justificada** que:
- Atende aos requisitos dos testes
- Respeita a permissão do documento (inteiros escalados)
- Otimiza para a arquitetura alvo (ATmega328P)
- Mantém o código compacto e rápido

---
