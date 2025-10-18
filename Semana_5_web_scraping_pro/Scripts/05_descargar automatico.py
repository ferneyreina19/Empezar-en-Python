import pandas as pd
import requests
from datetime import datetime

def descargar_y_guardar():
    url = 'https://tradingeconomics.com/country-list/interest-rate'
    
    # Agregamos headers con User-Agent para evitar error 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    # Usamos requests para obtener el HTML
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lanza error si falla la descarga
    
    # Le pasamos el contenido HTML directamente a pandas
    tablas = pd.read_html(response.text)
    df = tablas[0]
    
    # Guardamos en CSV
    ruta_csv = r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Taxes_paises.csv"
    df.to_csv(ruta_csv, index=False)
    print("Datos descargados y guardados correctamente.")

    # Guardamos log de descarga
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\log.txt", "a") as f:
        f.write(f"Datos descargados el {fecha}\n")
        
descargar_y_guardar()
    
if __name__ == "__main__":
    descargar_y_guardar()
