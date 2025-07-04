# Importações necessárias
import time
from datetime import datetime
import random

class SensorAproximacao:
    def detectar(self):
        return random.choice([True, False, False])

class SensorChuva:
    def detectar(self):
        return random.choice([True, False, False, False])

class SensorMovimentoSuspeito:
    def detectar(self):
        return random.choice([True, False, False, False])

class SensorMotoristaMulher:
    def detectar(self):
        return random.choice([True, False])

class Semaforo:
    def __init__(self):
        self.status = "VERDE (pouco movimento)"
    def mudar_status(self, status):
        self.status = status
        print(f"🚦 Semáforo está: {self.status}")

# ========================================
# Função para verificar se é madrugada
# ========================================
def is_madrugada():
    hora_atual = datetime.now().hour
    return hora_atual >= 0 and hora_atual < 6

# ===================================================
# Aciona refletores para iluminar via
# ===================================================
def acionar_refletores():
    print("💡 Refletores ligados para melhor iluminação da via (chuva ou risco).")

# ===================================================
# Usa refletores NÃO para multar, mas para proteger
# ===================================================
def refletor_para_sinalizacao():
    print("🔦 Refletores sendo usados para sinalização ao motorista, não para multa.")

# ===================================================
# Controlador principal do semáforo inteligente
# ===================================================
def controlar_semaforo(ciclos=None):
    sensor_aproximacao = SensorAproximacao()
    sensor_chuva = SensorChuva()
    sensor_movimento_suspeito = SensorMovimentoSuspeito()
    sensor_motorista_mulher = SensorMotoristaMulher()    
    semaforo = Semaforo()
    contador = 0  # Inicializa contador de ciclos
    while True:
        print("\n🚦 Verificando condições...")
        
        if is_madrugada():
            print("⏰ É madrugada (00h–06h). Modo inteligente ativado.")

            # Coletar dados dos sensores
            carro_detectado = sensor_aproximacao.detectar()
            suspeito_detectado = sensor_movimento_suspeito.detectar()
            chovendo = sensor_chuva.detectar()

            print(f"🔍 Carro detectado? {'Sim' if carro_detectado else 'Não'}")
            print(f"🚨 Movimento suspeito? {'Sim' if suspeito_detectado else 'Não'}")
            print(f"🌧 Está chovendo? {'Sim' if chovendo else 'Não'}")

            # Ações baseadas nos dados
            if carro_detectado:
                if sensor_motorista_mulher.detectar():
                    print("👩 Motorista identificada como mulher.")
                else:
                    print("🧔 Motorista não identificado como mulher.")

            if chovendo:
                acionar_refletores()

            if carro_detectado or suspeito_detectado:
                semaforo.mudar_status("VERDE (livre)")
            else:
                semaforo.mudar_status("VERDE (pouco movimento)")

            refletor_para_sinalizacao()

        else:
            print("🕐 Fora da madrugada. Modo padrão do semáforo ativado.")
            print("🚦 Semáforo segue funcionamento normal (vermelho/verde por tempo).")

        contador += 1 
        if ciclos and contador >= ciclos:
            break
        time.sleep(5)

# ========================================
# Executa o programa principal
# ========================================
if __name__ == "__main__":
    try:
        controlar_semaforo(ciclos=5)  
    except KeyboardInterrupt:
        print("\n🚨 Programa interrompido pelo usuário. Encerrando...")