def introducirNumeros ():
    global numero1, numero2
    numero1 = int(input("Ingreso un primer número : "))
    numero2 = int(input("Ingreso un segundo número : "))
    
def sumar(numero1, numero2):
    print(f"La suma de", numero1, "+", numero2, " = ", numero1 + numero2)
    
def restar(numero1, numero2):
    print(f"La resta de", numero1, "-", numero2, " = ", numero1 - numero2)
    
def multiplicar(numero1, numero2):
    print(f"La multiplicación de", numero1, "*", numero2, " = ", numero1 * numero2)
    
def dividir(numero1, numero2):
    if numero2 == 0:
        print("Error: División por cero no permitida.")
    else:
        print(f"La división de", numero1, "/", numero2, " = ", numero1 / numero2)


while True :
    print("""
    Indique la operacion que desea realizar:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    """)
    eleccion = int(input("Ingrese su opción: "))
    
    if eleccion == 1:
        introducirNumeros()
        sumar(numero1, numero2)
    elif eleccion == 2:
        introducirNumeros()
        restar(numero1, numero2)
    elif eleccion == 3:
        introducirNumeros()
        multiplicar(numero1, numero2)
    elif eleccion == 4:
        introducirNumeros()
        dividir(numero1, numero2)
    elif eleccion == 5:
        print("Saliendo de la calculadora.")
        break