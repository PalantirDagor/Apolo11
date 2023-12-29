import schedule
import time

def mi_funcion():
    print("Ejecutando la función...")
    suma = 0
    while True:
        suma = suma +1 

# Configura el trabajo programado
schedule.every(2).seconds.do(mi_funcion())

while True:
    schedule.run_pending()
    time.sleep(1)