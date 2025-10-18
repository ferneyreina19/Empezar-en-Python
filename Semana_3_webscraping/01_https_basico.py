import requests
# Este script realiza una solicitud HTTP a una página web y muestra el contenido de la página si la conexión es exitosa.
# Si la conexión falla, muestra un mensaje de error con el código de estado.


url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo'

response = requests.get(url)

if response.status_code == 200:
    print("Pagina conectada")
    print("Contenido de la pagina:")
    print(response.text[:1000])
else:
    print("Error para conectar la pagina:", response.status_code)
    
