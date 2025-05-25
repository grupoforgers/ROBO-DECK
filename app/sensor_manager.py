# Integra sensores conectados ao Raspberry Pi (ex: GPS, acelerômetro)

import random
import time

# Dados simulados
sensor_data = {
    "temperatura": 25.0,
    "umidade": 60.0,
    "distancia_cm": 50,
    "velocidade_kmh": 0.0,
    "gps": {"lat": -23.5505, "lon": -46.6333}
}

def atualizar_dados():
    """Atualiza os dados simulados com pequenas variações"""
    sensor_data["temperatura"] = round(24 + random.uniform(-1, 1), 2)
    sensor_data["umidade"] = round(60 + random.uniform(-5, 5), 2)
    sensor_data["distancia_cm"] = random.randint(10, 100)
    sensor_data["velocidade_kmh"] = round(random.uniform(0, 20), 1)
    sensor_data["gps"]["lat"] += random.uniform(-0.0001, 0.0001)
    sensor_data["gps"]["lon"] += random.uniform(-0.0001, 0.0001)

def obter_dados():
    atualizar_dados()
    return sensor_data
