import time
import logging
import sys
import json

from src.utilities.config import Util_Config as config
from src.utilities.files import FileUtils as file
from src.utilities.generic import Utils as util


class Simulator_Apolo11:
    """
    Simulator_Apolo11: Clase encargada de generar la simulación
    """

    def __init__(self, execution_number: int = 1, logging_level: int = 20):
        """
        Constructor de la clase.
        Cargan los atributos de instancia.

        configuration_file: Archivo de configuracion
        consecutive_file: Consecutivo del archivo

        Args:
            execution_number (int): Numero de ejecucion de la clase
            logging_level (int): Nivel de logging, default 40 - Error
        """

        logging.basicConfig(level=logging_level)

        self.__execution_number: int = execution_number
        self.__consecutive_file: dict[str, int] = {}

    @property
    def execution_number(self) -> int:
        return self.__execution_number

    @property
    def consecutive_file(self) -> dict[str, int]:
        return self.__consecutive_file

    @consecutive_file.setter
    def consecutive_file(self, mission: str) -> None:
        if self.__consecutive_file.get(mission) is None:
            self.__consecutive_file[mission] = 1
        else:
            self.__consecutive_file[mission] = self.__consecutive_file.get(mission) + 1

    def __generate_data(self, mission: str) -> dict:
        """
        Método privado que genera los datos simulados de cada la misión

        Args:
            mission (str): Mision a la que se debe generar los datos

        Returns:
            dict[str,str]: Diccionario con el registro de la mision
        """

        LC_UNKNOWN: str = 'unknown'

        row: dict = {"date": time.strftime(config._instance.date_format),
                     "mission": mission}

        if mission != "UNKN":
            row["device_type"] = util.generate_random(config._instance.device_type)
            row["device_status"] = util.generate_random(config._instance.device_status)
            row["hash"] = util.generate_hash(row.get("date"),
                                             row.get("mission"),
                                             row.get("device_type"),
                                             row.get("device_status"))
        else:
            row["device_type"] = LC_UNKNOWN
            row["device_status"] = LC_UNKNOWN
            row["hash"] = ""

        logging.debug("Se han generado los datos del archivo")
        return row

    def __create_file(self, rows: int = 1) -> None:
        """
        Método privado que crea el archivo de la mision

        Args:
            rows (int, optional): Numero de registros ha generar por archivo. Default 1
        """
        l_rows_file: list = []
        lv_mission: str = util.generate_random(config._instance.mission)

        # print(f"Star create files, mision: {lv_mission}")
        for i in range(0, rows):
            l_rows_file.append(self.__generate_data(lv_mission))

        # Save file
        file.Save(self.__filename(lv_mission), config.DESTINATION_FILE, l_rows_file)
        logging.debug(f"Se creo archivo de la mision {lv_mission} en la ruta {config.DESTINATION_FILE}")

    def __filename(self, mission: str) -> str:
        """
        Método privado que genera el nombre del archivo

        Args:
            mission (str): Mision a la que se va a generar el nombre

        Returns:
            str: Nombre del archivo
        """
        # Consetutivo de la mision
        self.consecutive_file = mission

        return (f"APL{mission}-{self.execution_number:0>{config._instance.number_digits}}-"
                f"{self.consecutive_file.get(mission):0>{config._instance.number_digits}}.log")

    def _start_simulator(self) -> bool:
        """Inicia el proceso de simulación

        Returns:
            bool: True si la simulación fue exitosa, False si genera algun error
        """
        try:
            ln_files: int = util.generate_random_number(config._instance.file_quantity[0],
                                                        config._instance.file_quantity[1])

            logging.debug(f"Inicia la creacion de {ln_files} archivos para le ejecución nro {self.execution_number}")

            for i in range(0, ln_files):
                self.__create_file(config._instance.rows_file)

            logging.info(f"Se han generado {ln_files} archivos en la ejecución nro {self.execution_number}")
            return True

        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'nombre_archivo': exc_traceback.tb_frame.f_code.co_filename,
                'linea_nro': exc_traceback.tb_lineno,
                'modulo': exc_traceback.tb_frame.f_code.co_name,
                'tipo_error': exc_type.__name__,
                'excepcion': str(ex)
            }
            print(json.dumps(traceback_details, indent=4))
            return False
