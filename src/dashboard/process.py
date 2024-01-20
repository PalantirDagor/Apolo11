import os
import json
import pandas as pd
import time
from typing import List
from src.utilities.files import FileUtils as file
from src.utilities.control_messages import Mensage as message


class Report:

    def __init__(self, name_report):
        self.__folder_path: str = os.path.join("Files", "Devices")
        self.__date_report = str(time.strftime('%Y%m%d%H%M%S'))
        self.__folder_backup: str = os.path.join("Files", "Backup", self.__date_report)
        self.__folder_report: str = os.path.join("Files", "Report", self.__date_report)
        self.__name_report = f"APLSTATS-{name_report}-{self.__date_report}.log"
        self.__name_consolidated = f"APLSTATS-Consolidated_Files-{self.__date_report}.log"

    def start_process(self) -> dict:
        """Orquestador de la generacion de reportes

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado
            (successful,warning) un state (True o False) si la operacion finalizo con exito o algo fallo respectivamente
            y un atributo object con el listado de datos leidos
        """
        try:
            # 1. Consolido los datos
            consolidate_events = self.consolidate_files().get("object")

            # 2. Creo un archivo con los datos consolidados
            file.Save(self.__name_consolidated, self.__folder_report, consolidate_events)

            # 3. Creo un DataFrame con los datos concolidados
            df = pd.DataFrame(consolidate_events, columns=['date', 'mission', 'device_type', 'device_status', 'hash'])

            # 4. Genero los diferentes tipos de reportes
            self.generate_dashboard(df)

            return message.build_message(id_mesage=0)
        except Exception as e:
            return message.build_message(0, str(e.args[1]))

    def consolidate_files(self) -> dict:

        """Consolidad en una única lista los datos de los archivos reportados por las misiones

        Returns:
            list[str]: Retorna los eventos como una lista de string

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado
            (successful,warning) un state (True o False) si la operacion finalizo con exito o algo fallo respectivamente
            y un atributo object con el listado de datos leidos
        """

        try:
            records: List[str] = []

            for file_name in os.listdir(self.__folder_path):
                file_path = os.path.join(self.__folder_path, file_name)
                lines = file.read_file(file_path).get("object")

                if lines is not None:
                    lines = lines.splitlines()
                    for line in lines:
                        data = json.loads(line.replace("'", "\""))
                        record = list(data.values())
                        records.append(record)

            return message.build_message(id_mesage=0, obj=list(records))
        except Exception as e:
            return message.build_message(0, str(e.args[1]))

    def add_header():
        def decorador(func):
            """Recibe una función y le aplica un estilo al titulo

            Args:
                func (function): funcion que recibe
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

        """procesa un DataFrame convirtiendolo en una lista de string para ser grabada en un archivo

        Args:
            data (pd.core.frame.DataFrame): DataFrame
            title (_type_): titulo de la cabecera

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado
            (successful,warning) un state (True o False) si la operacion finalizo con exito o algo fallo respectivamente
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

            return message.build_message(id_mesage=0)
        except Exception as e:
            return message.build_message(0, str(e.args[1]))

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

    def generate_dashboard(self, df: pd.core.frame.DataFrame) -> dict:
        """Se encarga de controlar el flujo de la generación de reportes y manejo de archivos

        Args:
            df (pd.core.frame.DataFrame): DataFrame con el universo de datos consolidado

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado
            (successful,warning) un state (True o False) si la operacion finalizo con exito o algo fallo respectivamente
        """

        try:

            # Análisis de eventos
            e_a = self.event_analysis(df)
            title = "Candidad de eventos por estado para cada mision y dispositivo"
            # self.save_graphic(e_a, 1, title)
            self.save_in_dashboard(e_a, title)

            # Gestión de desconexiones
            d_m = self.disconnection_management(df)
            title = "Dispositivos con número de desconexiones (unknown) por misión"
            self.save_in_dashboard(d_m, title)

            # Consolidación de misiones
            k_d = self.killed_devices(df)
            self.save_in_dashboard(k_d, "Cantidad de dispositivos inoperables")

            # Cálculo de porcentajes
            c_p = self.calculate_percentage(df)
            self.save_in_dashboard(c_p, "Porcentaje de datos generados por dispositivos y mision")

            return message.build_message(id_mesage=0)
        except Exception as e:
            return message.build_message(0, str(e.args[1]))
