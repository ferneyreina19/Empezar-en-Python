import pyautogui
import subprocess
import time

mensaje = input("¿Qué operación quieres realizar? (Ejemplo: 2 + 2): ")
time.sleep(5)
subprocess.Popen('calc.exe') 
time.sleep(3)

pyautogui.write(mensaje, interval=0.1)
pyautogui.press('enter')