import pyautogui
import time

# Espera 5 segundos para que te dé tiempo de abrir otra ventana
time.sleep(5)

# Mueve el mouse a la posición (x, y)
pyautogui.moveTo(294, 724, duration=1)  # duración en segundos

# Hace clic izquierdo
pyautogui.click()
pyautogui.click()

# Escribe el mensaje automáticamente
pyautogui.write("Esto fue hecho sin tocar el mouse ni el teclado 😱", interval=0.05)

# Presiona Enter al final (opcional)
pyautogui.press('enter')