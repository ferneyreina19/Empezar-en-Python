# organizador_de_tareas.py

# Lista global para almacenar las tareas
tareas = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Función para agregar una tarea
def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ").strip()
    if tarea:
        tareas.append(tarea)
        print("✅ Tarea agregada.")
    else:
        print("⚠️ No puedes agregar una tarea vacía.")

# Función para ver las tareas
def ver_tareas():
    if not tareas:
        print("📭 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
            
# Función para marcar una tarea como completada
def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Número de la tarea completada: "))
        if 1 <= indice <= len(tareas):
            tarea_completada = tareas.pop(indice - 1)
            print(f"✅ Tarea '{tarea_completada}' marcada como completada.")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")

# Función para eliminar una tarea
def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")

# Función principal para ejecutar el programa
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("👋 Hasta luego, Ferney. ¡Buen trabajo!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa si se llama directamente
if __name__ == "__main__":
    ejecutar()
