import requests
from bs4 import BeautifulSoup

url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo' 
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titulo = soup.title.string
print("Titulo de la pagina:", titulo)

print("\n Enlaces encontrados:")
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        print("->", href)