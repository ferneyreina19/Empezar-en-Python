import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 4.61,      # Bogotá
    "longitude": -74.08,
    "hourly": "temperature_2m",
    "timezone": "America/Bogota"
}

respuesta = requests.get(url, params=params)
datos = respuesta.json()

import json

tiempos = datos['hourly']['time']
temperaturas = datos['hourly']['temperature_2m']

for i in range(3):
    print(f"{tiempos[i]} → {temperaturas[i]}°C")
    
datos_horas = []

for tiempo, temp in zip(tiempos, temperaturas):
    datos_horas.append({
        "hora": tiempo,
        "temperatura": temp
    })

print(datos_horas[:3])

