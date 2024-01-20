import time
import threading
import argparse
from src.Simulator.simulator import Simulator_Apolo11 as apl11
from src.dashboard.process import Report as apl11_report


def main():
    parser = argparse.ArgumentParser(
        prog='Apolo11',
        description='Control manual de simulaciones de la Nasa.')

    parser.add_argument('-start', choices=["simulation", "report"], help='lista de procesos que puedo ejecutar')
    parser.add_argument('-sc', type=int, default = 20, help='ciclo de simulación, default 20')
    parser.add_argument('-nr', type=str, help='nombre del reporte a generar')
    
    args = parser.parse_args()

    if args.start == 'simulation':
        print(f"Proceso de simulacion iniciado con un ciclo de {args.sc} segundos, para detener presiona Ctrl + c")
        try:
            i: int = 0
            while True:
                thread = threading.Thread(target = call_simulator, args=(i,))
                thread.start()
                time.sleep(args.sc)
                i += 1
        except KeyboardInterrupt:
            print("Stop: Finalizando ejecución, espere por favor....")
    elif args.start == 'report':
        if args.nr is None:
            print("Se requiere especificar el nombre del reporte; argumento: -nr")
        else:
            print("Generación  de reporte iniciado...")
            call_report(args.nr)
            print("Reporte generado exitosamente")


def call_simulator(count: int = 0):
    simulator = apl11(count)
    simulator.start_simulator()


def call_report(name_report: str):
    report = apl11_report(name_report)
    report.start_process()


if __name__ == '__main__':
    main()
