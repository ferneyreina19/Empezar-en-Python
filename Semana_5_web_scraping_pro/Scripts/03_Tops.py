import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Departamentos_limpio.csv")



top_10 = df.sort_values(by="Población (hab)[3]\u200b", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10['Departamento'], top_10['Población (hab)[3]\u200b'], color = 'darkblue')
plt.title("Top 10 Departamentos mas poblados")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("Top poblacion.png")
plt.show

import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Colombian_departments_by_population"
tablas = pd.read_html(url)

print(f"Cantidad de tablas detectadas: {len(tablas)}")

for i, df in enumerate(tablas):
    print(f"Tabla {i} — columnas:", df.columns.tolist())

# Supongamos que tabla 0 es la relevante
df = tablas[0]
print(df.head())

df.to_csv(r"C:\Users\Ferney Reina\Documents\Python\Aprender\Semana_5_web_scraping_pro\Datos\Departamentos_limpio.csv", index=False)
print("✅ Guardado en deptos_poblacion_wiki.csv")

