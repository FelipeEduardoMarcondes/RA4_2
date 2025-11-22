import serial
import serial.tools.list_ports
import time
import sys

# ==========================================
# CONFIGURAÇÕES
# ==========================================
BAUD_RATE = 9600       # Deve ser o mesmo configurado no código do Arduino
PORTA_PADRAO = 'COM3'  # Altere se souber sua porta (ex: 'COM3' no Windows, '/dev/ttyUSB0' no Linux)
TIMEOUT = 2            # Tempo de espera para leitura
# ==========================================

def encontrar_porta_arduino():
    """Tenta encontrar automaticamente uma porta que pareça ser um Arduino."""
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        # Filtro simples: geralmente Arduinos têm "Arduino", "USB Serial" ou "USB-SERIAL" na descrição
        if "Arduino" in p.description or "CH340" in p.description or "USB" in p.description:
            return p.device
    return None

def monitorar_serial():
    # Tenta usar a porta configurada ou encontrar uma automaticamente
    porta = PORTA_PADRAO
    
    # Se a porta padrão não existir, tenta achar
    try:
        s = serial.Serial(porta)
        s.close()
    except serial.SerialException:
        print(f"Porta {porta} não encontrada ou ocupada. Procurando automaticamente...")
        detectada = encontrar_porta_arduino()
        if detectada:
            porta = detectada
            print(f"Dispositivo encontrado em: {porta}")
        else:
            print("Nenhum dispositivo serial óbvio encontrado.")
            print("Liste as portas disponíveis com: python -m serial.tools.list_ports")
            porta = input("Digite o nome da porta manualmente (ex: COM3): ").strip()

    print(f"\n--- Iniciando Monitor Serial na {porta} ({BAUD_RATE} baud) ---")
    print("Pressione Ctrl+C para sair.\n")

    try:
        # Abre a conexão serial
        ser = serial.Serial(porta, BAUD_RATE, timeout=TIMEOUT)
        time.sleep(2)  # Espera o Arduino reiniciar após abrir a serial (comportamento padrão do Uno)

        # Loop de leitura
        while True:
            # Lê uma linha da serial (bytes)
            if ser.in_waiting > 0:
                try:
                    # decodifica bytes para string (utf-8 ou ascii) e remove espaços/quebras de linha extras
                    linha = ser.readline().decode('utf-8', errors='ignore').strip()
                    if linha:
                        print(f"[Arduino]: {linha}")
                except Exception as e:
                    print(f"[Erro de Leitura]: {e}")
            
            time.sleep(0.01) # Pequena pausa para não fritar a CPU do PC

    except serial.SerialException as e:
        print(f"\nErro ao conectar na porta {porta}: {e}")
        print("Verifique se o cabo está conectado e se nenhuma outra janela (como o VS Code ou Arduino IDE) está usando a porta.")
    except KeyboardInterrupt:
        print("\n--- Monitor encerrado pelo usuário ---")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Conexão fechada.")

if __name__ == "__main__":
    monitorar_serial()