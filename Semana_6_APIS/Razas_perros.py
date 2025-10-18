import requests
import csv

# API Key y URL
api_key = "live_0zKjesqoBbzVdq7R06gEXOtX2QhvGewoxiSNll1GCykh08nwtDIG3KqvClCY1rTn"
url = "https://api.thedogapi.com/v1/breeds"

# Cabecera con autenticación
headers = {
    "x-api-key": api_key
}

# Petición a la API
respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    datos = respuesta.json()

    # Guardar en CSV
    with open("razas_perros.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["name", "bred_for", "breed_group", "life_span", "temperament", "origin"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()

        for raza in datos:
            writer.writerow({
                "name": raza.get("name", ""),
                "bred_for": raza.get("bred_for", ""),
                "breed_group": raza.get("breed_group", ""),
                "life_span": raza.get("life_span", ""),
                "temperament": raza.get("temperament", ""),
                "origin": raza.get("origin", "")
            })

    print("✅ Archivo CSV creado con éxito: razas_perros.csv")

else:
    print("❌ Error al consultar la API:", respuesta.status_code)
