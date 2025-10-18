import pyautogui
import time

mensaje = input("¿Qué mensaje quieres enviar? ")
veces = int(input("¿Cuántas veces quieres enviarlo? "))

print("Tienes 5 segundos para cambiarte de ventana...")
time.sleep(5)

for i in range(veces):
    pyautogui.write(mensaje, interval=0.1)
    pyautogui.press('enter')