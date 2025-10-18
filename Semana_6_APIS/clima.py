import requests

ciudad = "Fundacion"
url = f"https://wttr.in/{ciudad}?m&lang=es" 

respuesta = requests.get(url)

if respuesta.status_code == 200:
    print(respuesta.text)
else:
    print("Error al obtener los datos del clima:", respuesta.status_code)
