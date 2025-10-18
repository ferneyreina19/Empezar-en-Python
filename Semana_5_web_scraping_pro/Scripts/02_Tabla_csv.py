import pandas as pd 

url = "https://es.wikipedia.org/wiki/Departamentos_de_Colombia"

tabla = pd.read_html(url)[15]

print(tabla.head())



tabla_columns = ['Departamento', 'Capital', 'Superficie (km²)', 'Población (hab)[3]\u200b', 'Densidad (hab/km²)', 'Fecha de creación[nota 1]\u200b']

tabla = tabla.dropna(subset=['Departamento'])

tabla['Superficie (km²)'] = (
    tabla['Superficie (km²)']
    .astype(str)
    .str.replace("\xa0" , "", regex=False)
    .str.replace(" ","", regex=False)
    .str.replace(".","", regex=False)
    .str.replace(",",".", regex=False)
    .astype(float)
    )
tabla['Población (hab)[3]\u200b'] = (
    tabla['Población (hab)[3]\u200b']
    .astype(str)
    .str.replace("\xa0" , "", regex=False)
    .str.replace(" ","", regex=False)
    .str.replace("." , "", regex=False)
    .astype(int)
    )
tabla['Densidad (hab/km²)'] =(
    tabla['Densidad (hab/km²)']
    .astype(str)
    .str.replace("\xa0", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.replace(",", ".", regex=False) 
    .astype(float)
    )

tabla.to_csv(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Departamentos_limpio.csv", index=False)
print("Archivo limpio actualizado: Departamentos limpios")


