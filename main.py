import time
import threading
import argparse
import logging
from src.utilities.config import Util_Config
from src.Simulator.simulator import Simulator_Apolo11 as apl11
from src.dashboard.process import Report as apl11_report

# función definida por el usuario para validar si el valor es un número positivo
def es_numero_positivo(valor):
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            raise argparse.ArgumentTypeError(f"{valor} no es un número positivo")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{valor} no es un número")     


def main():
    parser = argparse.ArgumentParser(
        prog='Apolo11',
        description='Control manual de simulaciones de la Nasa.')

    parser.add_argument('-start', default = "simulation", choices=["simulation", "report"], help = 'lista de procesos que puedo ejecutar')
    parser.add_argument('-sc', type = es_numero_positivo, default = 20, help = 'ciclo de simulación, default = 20')
    parser.add_argument('-nr', type = str, help ='nombre del reporte a generar')
    parser.add_argument('-lg', type = int, default = 20, choices=[0,10,20,30,40,50],
                               help = """Nivel de logging a mostrar. Default(20):
                                         CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0""")

    args = parser.parse_args()
    # Nivel de logging
    logging.basicConfig(level=args.lg)
    config = Util_Config()

    if args.start == 'simulation':
        logging.info(f"Proceso de simulación iniciado con un ciclo de {args.sc} segundos, para detener presiona Ctrl + c")
        try:
            i: int = 1
            while True:
                thread = threading.Thread(target = call_simulator, args=(i,args.lg))
                thread.start()
                time.sleep(args.sc)
                i += 1
        except KeyboardInterrupt:
            logging.info("Stop: Finalizando ejecución, espere por favor....")
    elif args.start == 'report':
        if args.nr is None:
            raise argparse.ArgumentTypeError("Se requiere especificar el nombre del reporte; argumento: -nr")
        else:
            config.replace_name_report(args.nr)
            logging.info("Generación de reporte iniciado...")
            if call_report(args.lg):
                logging.info("Reporte generado exitosamente")
            else:
                logging.error("Ocurrió un error durante la ejecución de generación del reporte ")

def call_simulator(count: int = 1 , level_logging: int = 20):
    simulator = apl11(count, level_logging)
    simulator.start_simulator()

def call_report(level_logging: int = 20) -> bool:
    report = apl11_report(level_logging)
    result = report.start_process().message["state"]
    return result  

if __name__ == '__main__':
    main()
