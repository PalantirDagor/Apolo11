import os
import json
import pandas as pd
import time
import logging
from typing import List
from src.utilities.files import FileUtils as file
from src.utilities.control_messages import Message as message
from src.utilities.generic import Util_Return


class Report:

    def __init__(self, name_report, logging_level: int):

        logging.basicConfig(level=logging_level)

        self.__name_columns: List[str] = ['date', 'mission', 'device_type', 'device_status', 'hash']
        self.__folder_path: str = os.path.join("files", "devices")
        self.__date_report = str(time.strftime('%Y%m%d%H%M%S'))
        self.__folder_backup: str = os.path.join("files", "backups", self.__date_report)
        self.__folder_report: str = os.path.join("files", "reports", self.__date_report)
        self.__name_report = f"APLSTATS-{name_report}-{self.__date_report}.log"
        self.__name_consolidated = f"APLSTATS-Consolidated_Files-{self.__date_report}.log"

    def start_process(self) -> Util_Return:
        """Orquestador de la generación de reportes

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = listado de datos leídos o None
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario

        """
        try:
            # 1. Consolido los datos
            consolidate_events = self.consolidate_files().object

            # 2. Creo un archivo con los datos consolidados
            self.save_consolidated(consolidate_events)

            # 3. Creo un DataFrame con los datos concolidados
            df = self.dataframe_creation(consolidate_events)

            # 4. Genero los diferentes tipos de reportes
            self.generate_dashboard(df)

            return Util_Return(object=None,
                               message=message.build_message(0, "S"))
        except Exception as e:
            return Util_Return(object=None,
                               message=message.build_message(0, "E", str(e.args[1])))

    def consolidate_files(self) -> Util_Return:

        """Consolidad en una única lista los datos de los archivos reportados por las misiones

        Returns:
            list[str]: Retorna los eventos como una lista de string

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = listado de datos leídos o None
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario
        """

        try:

            if len(os.listdir(self.__folder_path)) == 0:
                logging.info("No existen archivos simulados para procesar...")
                raise SystemExit()

            records: List[str] = []

            for file_name in os.listdir(self.__folder_path):
                file_path = os.path.join(self.__folder_path, file_name)
                lines = file.read_file(file_path).object

                if lines is not None:
                    lines = lines.splitlines()
                    for line in lines:
                        data = json.loads(line.replace("'", "\""))
                        record = list(data.values())
                        records.append(record)

                file.move_file(self.__folder_path, self.__folder_backup, file_name)

            logging.debug((f"""Se genero la consolidación de {len(list(records))} registros de un total de
                           {len(os.listdir(self.__folder_path))} archivos"""))

            return Util_Return(object=list(records),
                               message=message.build_message(0, "S"))
        except Exception as e:
            return Util_Return(object=None,
                               message=message.build_message(0, "E", str(e.args[1])))

    def save_consolidated(self, list: List[str]):
        """Crea un archivo con los datos consolidados

        Args:
            list (List[str]): Lista con los eventos consolidados
        """
        file.Save(self.__name_consolidated, self.__folder_report, [self.__name_columns] + list)
        logging.debug(f"Generación de consolidados {os.path.join(self.__folder_report, self.__name_consolidated)}")

    def dataframe_creation(self, list: List[str]) -> pd.core.frame.DataFrame:
        """Creo un DataFrame con los datos consolidados

        Args:
            list (List[str]): Lista con los eventos consolidados

        Returns:
            pd.core.frame.DataFrame: DataFrame de pandas
        """

        logging.debug("Se genera un Dataframe de los datos consolidados")
        return pd.DataFrame(list, columns=self.__name_columns)

    def generate_dashboard(self, df: pd.core.frame.DataFrame) -> dict:

        """Se encarga de controlar el flujo de la generación de reportes y manejo de archivos

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = None
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario
        """

        try:

            # Análisis de eventos
            logging.debug("Generando análisis de eventos...")
            e_a = self.event_analysis(df)
            title = "Cantidad  de eventos por estado para cada misión y dispositivo"
            # self.save_graphic(e_a, 1, title)
            self.save_in_dashboard(e_a, title)

            # Gestión de desconexiones
            logging.debug("Validando gestión de desconexiones...")
            d_m = self.disconnection_management(df)
            title = "Dispositivos con número de desconexiones (unknown) por misión"
            self.save_in_dashboard(d_m, title)

            # Consolidación de misiones
            logging.debug("Validando dispositivos inoperables...")
            k_d = self.killed_devices(df)
            self.save_in_dashboard(k_d, "Cantidad de dispositivos inoperables")

            # Cálculo de porcentajes
            logging.debug("Validando porcentaje de datos generados por dispositivos y misión")
            c_p = self.calculate_percentage(df)
            self.save_in_dashboard(c_p, "Porcentaje de datos generados por dispositivos y misión")

            logging.debug(f"Informe generado en la carpera {self.__date_report}")
            return Util_Return(object=None,
                               message=message.build_message(0, "S"))
        except Exception as e:
            return Util_Return(object=None,
                               message=message.build_message(0, "E", str(e.args[1])))

    def add_header():
        def decorador(func):
            """Recibe una función y le aplica un estilo al titulo

            Args:
                func (function): Función que recibe
            """
            def wrapper(self,
                        data: pd.core.frame.DataFrame,
                        title: str):

                head = f"""
                {'*' * len(title)}
                {title}
                {'*' * len(title)}
                """
                func(self, data, head)

            return wrapper
        return decorador

    @add_header()
    def save_in_dashboard(self,
                          data: pd.core.frame.DataFrame,
                          title: str) -> dict:

        """Procesa un DataFrame convirtiéndolo  en una lista de string para ser grabada en un archivo

        Args:
            data (pd.core.frame.DataFrame): DataFrame
            title (_type_): título  de la cabecera

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = None
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario

        """
        try:

            info: List[str] = []

            if isinstance(data, pd.core.frame.DataFrame):
                info = [str(row) for row in data.to_string(index=False).split('\n')]
            else:
                info.append(str(data))

            # Agrego un titulo al conjunto de datos
            file.Save(self.__name_report, self.__folder_report, [title])

            # Agrego el conjunto de datos
            file.Save(self.__name_report, self.__folder_report, info)

            return Util_Return(object=None,
                               message=message.build_message(0, "S"))
        except Exception as e:
            return Util_Return(object=None,
                               message=message.build_message(0, "E", str(e.args[1])))

    def event_analysis(self, df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:

        """
        Realizar un análisis de la cantidad de eventos por estado para cada misión y dispositivo

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            filter (pd.core.frame.DataFrame): DataFrame con el resultado de la consulta
        """

        filter = (df.groupby(['mission', 'device_type', 'device_status'])
                  .size()
                  .rename('number_events')
                  .reset_index()
                  .sort_values(by=['mission', 'device_type', 'device_status', 'number_events'],
                               ascending=[True, True, True, False]))
        return filter

    def disconnection_management(self, df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
        """
         Identificar los dispositivos que presentan un mayor número
         de desconexiones, específicamente en el estado "unknown", para cada misión.

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            number_disconnections (pd.core.frame.DataFrame): DataFrame con el resultado de la consulta
        """

        unknown_devices = df[df['device_status'] == 'unknown']

        number_disconnections = (unknown_devices.groupby(['mission', 'device_type'])
                                 .size()
                                 .rename('number_disconnections')
                                 .reset_index()
                                 .sort_values(by='number_disconnections',
                                              ascending=False))

        return number_disconnections

    def killed_devices(self, df: pd.core.frame.DataFrame) -> int:
        """Realiza la consulta para determinar cuántos dispositivos son inoperables

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            int: cantidad de dispositivos inoperables
        """
        return len(df[df['device_status'] == 'killed'])

    def calculate_percentage(self, df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
        """
        Calcular los porcentajes de datos generados para cada
        dispositivo y misión con respecto a la cantidad total de datos

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            filter (pd.core.frame.DataFrame): DataFrame con el resultado de la consulta
        """

        filter = (df.groupby(['mission', 'device_type'])
                  .size()
                  .rename('count_data')
                  .reset_index()
                  .sort_values(by=['mission', 'count_data'],
                               ascending=[True, False]))

        filter['percentage_data'] = ((filter.count_data / len(df) * 100).round(2).astype(str) + ' %')

        return filter
