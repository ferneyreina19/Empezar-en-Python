import  subprocess

def notion():
    print("Abriendo Notion...")
    subprocess.run(r"C:\Users\Ferney Reina\AppData\Local\Programs\Notion\Notion.exe")
def discord():
    print("Abriendo Discord...")
    subprocess.run(r'"C:\Users\Ferney Reina\AppData\Local\Discord\Update.exe" --processStart Discord.exe')


while True:
    print("""
    Seleccione el programa que desea abrir:
    1. Notion
    2. Discord
    3. Salir
    """)
    eleccion = int(input("""
Seleccione el programa que desea abrir:"""))  
    if eleccion == 1:
        notion()
    elif eleccion == 2:
        discord()
    elif eleccion == 3:
        print("Saliendo...")
    break

