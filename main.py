import time
import threading
from src.Simulator.simulator import Simulator_Apolo11 as apl11


def _main_():
    pass 

def call_simulator(count: int = 0):
    simulador = apl11(count)
    simulador.start_simulator()


try:
    i: int = 0
    while True:
        thread = threading.Thread(target= call_simulator, args=(i,) )  
        thread.start()
        time.sleep(20) 
        i +=1
except KeyboardInterrupt: 
    print("Stop: Ejecución interrumpida por el usuario")