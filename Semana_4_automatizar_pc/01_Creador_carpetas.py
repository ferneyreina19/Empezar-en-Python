import os 

estructura = {
    "Macroeconomia II":["Tareas", "Examenes", "Apuntes"],
    "Asginacion de recursos":["Tareas", "Examenes", "Apuntes"],
    "Econometria II":["Tareas", "Examenes", "Apuntes"],
    "Ingles IV":["Tareas", "Examenes", "Apuntes"],
    "Inteligencia Artificial":["Tareas", "Examenes", "Apuntes"],
    "Taller de habilidades profesionales":["Tareas", "Examenes", "Apuntes"],
}

base_path = "C:/Users/Ferney Reina/Documents/Universidad/6_Semestre"

for materia, subcarpetas in estructura.items():
    for sub in subcarpetas:
        ruta = os.path.join(base_path, materia, sub)
        os.makedirs(ruta, exist_ok=True)
        print(f"Carpeta creada: {ruta}")