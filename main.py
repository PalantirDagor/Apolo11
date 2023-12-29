
import time
import threading
from src.Simulator.simulator import Simulator_Apolo11 as apl11

def __main__():
    pass 

def call_simulator(count: int = 0):
     simulador = apl11(count)
     simulador.start_simulator()
     i = count + 1
     print(f"Instancia nro: {i}")
     threading.Timer(1,call_simulator(i)).start()

try:
    call_simulator()  
    time.sleep(1)
except KeyboardInterrupt: 
    print("Stop: Ejecución interrumpida por el usuario")       

"""
#for i in range(1,4):
try:
    i: int = 0
    while True:    
        simulador = apl11(i)
        #simulador.start_simulator()
        #time.sleep(1)
        threading.Timer(1,simulador.start_simulator()).start()
        i += 1 
        print(f"Ejecución nro: {i}")
except KeyboardInterrupt:
    print("Pare...")    
#print(simulador.filename("ORBONE"))
#print(simulador.filename("ORBONE"))
# Cargar archivos de configuración
# Hacer control de excepciones global
# llamar método start_simulator de la clase Simulator_Apolo11     
"""