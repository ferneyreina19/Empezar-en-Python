from plyer import notification
import time

while True:
    notification.notify(
        title='⏰ Pausa activa',
        message='Han pasado 2 horas. Estírate, toma agua y descansa los ojos.',
        timeout=10
    )
    time.sleep(2 * 60 * 60)  # 2 horas en segundos



