# config.py
# Configurações do Compilador RPN
# FELIPE EDUARDO MARCONDES - GRUPO 2

# ============================================
# CONFIGURAÇÕES DE HARDWARE
# ============================================

# Porta Serial do Arduino
# Windows: "COM3", "COM4", "COM5", etc.
# Linux: "/dev/ttyUSB0", "/dev/ttyACM0", etc.
# macOS: "/dev/cu.usbserial-XXXX"
PORTA_SERIAL = "COM4"

# Taxa de comunicação (baud rate)
# Padrão: 115200 para upload, 9600 para serial monitor
BAUD_RATE_UPLOAD = 115200
BAUD_RATE_MONITOR = 9600

# ============================================
# CONFIGURAÇÕES DO COMPILADOR
# ============================================

# Fator de escala para ponto fixo (Fixed Point)
# 100 significa: 1.00 → 100, 0.5 → 50
SCALE_FACTOR = 100

# Habilitar otimizações
ENABLE_OPTIMIZATIONS = True

# Habilitar upload automático após compilação
AUTO_UPLOAD = True  # Mude para True se quiser upload automático

# ============================================
# CONFIGURAÇÕES DE SAÍDA
# ============================================

# Diretório de saída para arquivos gerados
OUTPUT_DIR = "analises"

# Gerar relatórios em Markdown
GENERATE_REPORTS = True

# Verbosidade (0=mínimo, 1=normal, 2=detalhado)
VERBOSE_LEVEL = 1

# ============================================
# CONFIGURAÇÕES AVANÇADAS
# ============================================

# Tamanho do histórico (para comando RES)
HISTORY_SIZE = 16

# Timeout para operações seriais (segundos)
SERIAL_TIMEOUT = 2

# Caminho da biblioteca matemática AVR
MATH_LIB_PATH = "avr_math_lib.s"

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def get_config():
    """Retorna todas as configurações como dicionário."""
    return {
        'porta_serial': PORTA_SERIAL,
        'baud_upload': BAUD_RATE_UPLOAD,
        'baud_monitor': BAUD_RATE_MONITOR,
        'scale': SCALE_FACTOR,
        'optimizations': ENABLE_OPTIMIZATIONS,
        'auto_upload': AUTO_UPLOAD,
        'output_dir': OUTPUT_DIR,
        'reports': GENERATE_REPORTS,
        'verbose': VERBOSE_LEVEL,
        'history_size': HISTORY_SIZE,
        'serial_timeout': SERIAL_TIMEOUT,
        'math_lib': MATH_LIB_PATH
    }


def print_config():
    """Imprime configurações atuais."""
    print("=" * 60)
    print("CONFIGURAÇÕES DO COMPILADOR")
    print("=" * 60)
    config = get_config()
    for key, value in config.items():
        print(f"{key:20s}: {value}")
    print("=" * 60)


if __name__ == "__main__":
    print_config()