import requests
from bs4 import BeautifulSoup

url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/demografia-y-poblacion/movilidad-y-migracion'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("archivos encontrados:\n")

for link in soup.find_all("a", href=True):
    href = link['href']
    if href.endswith('.pdf') or href.endswith('.xlsx') or href.endswith('.xls') or href.endswith('.csv'):
        print("->", href)