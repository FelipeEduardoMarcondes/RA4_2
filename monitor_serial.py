# monitor_serial.py
# FELIPE EDUARDO MARCONDES - GRUPO 2

import serial
import serial.tools.list_ports
import time
import sys

# ==========================================
# CONFIGURAÇÕES
# ==========================================
BAUD_RATE = 9600
PORTA_PADRAO = 'COM4'
TIMEOUT = 1
# ==========================================

def listar_portas():
    # Lista todas as portas seriais disponíveis.
    print("\n=== PORTAS SERIAIS DISPONÍVEIS ===")
    ports = list(serial.tools.list_ports.comports())
    
    if not ports:
        print("Nenhuma porta serial encontrada!")
        return None
    
    for i, p in enumerate(ports, 1):
        print(f"{i}. {p.device}")
        print(f"   Descrição: {p.description}")
        print(f"   Hardware ID: {p.hwid}")
        print()
    
    return ports

def encontrar_porta_arduino():
    # Tenta encontrar automaticamente uma porta Arduino.
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        desc = p.description.lower()
        if any(x in desc for x in ["arduino", "ch340", "usb-serial", "atmega"]):
            return p.device
    return None

def selecionar_porta():
    # Permite ao usuário selecionar uma porta.
    ports = listar_portas()
    
    if not ports:
        return None
    
    while True:
        try:
            escolha = input(f"\nEscolha uma porta (1-{len(ports)}) ou Enter para usar padrão ({PORTA_PADRAO}): ").strip()
            
            if not escolha:
                return PORTA_PADRAO
            
            idx = int(escolha) - 1
            if 0 <= idx < len(ports):
                return ports[idx].device
            else:
                print("Escolha inválida!")
        except ValueError:
            print("Digite um número válido!")

def monitorar_serial():
    print("=" * 60)
    print("MONITOR SERIAL - COMPILADOR RPN")
    print("=" * 60)
    
    # Tentativas de encontrar porta
    porta = PORTA_PADRAO
    
    # 1. Tenta usar porta padrão
    try:
        test_serial = serial.Serial(porta, BAUD_RATE, timeout=TIMEOUT)
        test_serial.close()
        print(f"✓ Porta padrão encontrada: {porta}")
    except serial.SerialException:
        print(f"✗ Porta padrão ({porta}) não disponível")
        
        # 2. Tenta encontrar automaticamente
        porta_auto = encontrar_porta_arduino()

        if porta_auto:
            porta = porta_auto
            print(f"✓ Arduino detectado em: {porta}")

        else:
            # 3. Pede ao usuário para escolher
            print("\nNão foi possível detectar o Arduino automaticamente.")
            porta = selecionar_porta()
            
            if not porta:
                print("\n✗ Nenhuma porta disponível. Saindo...")
                sys.exit(1)
    
    print(f"\n{'=' * 60}")
    print(f"Conectando em: {porta} ({BAUD_RATE} baud)")
    print(f"Pressione Ctrl+C para sair")
    print(f"{'=' * 60}\n")

    try:
        # Abre conexão serial
        ser = serial.Serial(porta, BAUD_RATE, timeout=TIMEOUT)
        
        # Aguarda reset do Arduino
        print("[INFO] Aguardando reset do Arduino...")
        time.sleep(2)
        
        # Limpa buffer
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        print("[INFO] Conectado! Aguardando dados...\n")
        
        linha_count = 0
        tempo_inicio = time.time()
        
        # Loop de leitura
        while True:

            if ser.in_waiting > 0:
                try:
                    # Lê linha
                    linha = ser.readline().decode('utf-8', errors='replace').strip()
                    
                    if linha:
                        linha_count += 1
                        timestamp = time.time() - tempo_inicio
                        
                        # Formatação da saída
                        print(f"[{timestamp:7.2f}s] {linha}")
                        sys.stdout.flush()
                        
                except UnicodeDecodeError as e:
                    print(f"[ERRO] Decodificação: {e}")

                except Exception as e:
                    print(f"[ERRO] Leitura: {e}")
            
            time.sleep(0.01)

    except serial.SerialException as e:
        print(f"\n✗ ERRO ao conectar em {porta}:")
        print(f"   {e}")
        print("\nVerifique:")
        print("  1. Cabo USB conectado corretamente")
        print("  2. Driver CH340/FTDI instalado")
        print("  3. Arduino IDE ou outras ferramentas não estão usando a porta")
        print("  4. Porta correta selecionada")
        
    except KeyboardInterrupt:
        print(f"\n\n{'=' * 60}")
        print(f"Monitor encerrado pelo usuário")
        print(f"Total de linhas recebidas: {linha_count}")
        print(f"{'=' * 60}")
        
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Conexão fechada.")

if __name__ == "__main__":
    monitorar_serial()