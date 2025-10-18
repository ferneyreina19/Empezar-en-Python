import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Listas para almacenar los datos
tiempos = []
precios = []

# Criptomoneda y moneda local
cripto = "bitcoin"
vs_moneda = "usd"

# Función que consulta y actualiza el gráfico
def actualizar(i):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies={vs_moneda}"
    response = requests.get(url)

    if response.status_code == 200:
        precio = response.json()[cripto][vs_moneda]
        tiempo = datetime.now().strftime('%H:%M:%S')

        tiempos.append(tiempo)
        precios.append(precio)

        # Limitar a los últimos 20 datos
        if len(tiempos) > 20:
            tiempos.pop(0)
            precios.pop(0)

        # Limpiar y graficar
        plt.cla()
        plt.plot(tiempos, precios, marker='o')
        plt.xticks(rotation=45)
        plt.title(f"Precio de {cripto.capitalize()} en {vs_moneda.upper()} (Tiempo Real)")
        plt.ylabel(f"Precio ({vs_moneda.upper()})")
        plt.tight_layout()
    else:
        print("❌ Error en la solicitud:", response.status_code)

# Crear animación que actualiza cada 5 segundos
fig = plt.figure()
ani = animation.FuncAnimation(fig, actualizar, interval=50000)
plt.show()
