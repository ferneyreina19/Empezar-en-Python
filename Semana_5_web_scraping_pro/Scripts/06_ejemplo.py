import pandas as pd
import requests
from datetime import datetime

def descargarpreciodolar():
    url = 'https://www.capitalcolombia.com/sec-trm_precio_dolar_en_colombia?srsltid=AfmBOootDrd6za5YY9zSSkRKkjVPAHg9Fw08YrAX1y7kCB-u9FqNPCzy'
    tablas = pd.read_html(url)
    df = tablas[0]  # o ajusta el índice según tu tabla
    df.to_csv(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Dolar_hoy.csv", index=False)
    print("✅ Datos descargados y guardados correctamente.")
descargarpreciodolar

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Dolarhoy.txt", "a") as f:
    f.write(f"Datos descargados el {fecha}\n")
    
if __name__ == "__main__":
    descargarpreciodolar()
 

