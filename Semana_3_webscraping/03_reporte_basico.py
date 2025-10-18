import requests
from bs4 import BeautifulSoup

url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    print("📰 Titulares encontrados:\n")

    # Cambia la etiqueta/clase según el sitio
    for titular in soup.find_all("h2"):
        texto = titular.get_text(strip=True)
        if texto:
            print("•", texto)
else:
    print("❌ No se pudo acceder a la página:", response.status_code)
    
    
import csv

with open("reporte_titulares.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Titular"])  # Encabezado

    for titular in soup.find_all("h2"):
        texto = titular.get_text(strip=True)
        if texto:
            writer.writerow([texto])
