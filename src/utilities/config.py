import os
import time
import yaml
from typing import List
from src.utilities.files import FileUtils as file


class Util_Config:
    """

    La clase se utiliza para manejar las configuraciones de la aplicación.
    Contiene rutas de archivos y configuraciones para la simulación y la generación de reportes.

    Attributes:
        CONF_FILE_PATH (str): La ruta del archivo de configuración.
        DESTINATION_FILE (str): Ruta donde se almacenan los datos simulados.
        FOLDER_BACKUP (str): La carpeta de respaldo.
        FOLDER_REPORT (str): La carpeta de reportes para la generación de reportes.
        NAME_CONSOLIDATED (str): El nombre del archivo consolidado de reportes.
        NAME_REPORT (str): El nombre del archivo de reporte.
        NAME_COLUMNS (List[str]): Lista de nombres de columnas para el reporte.

    """
    _instance = None

    # ruta del archivo de configuracion
    CONF_FILE_PATH: str = os.path.join("settings", "configuration_file.yaml")

    # configuracion para la simulacion
    DESTINATION_FILE: str = os.path.join("files", "devices")

    # Configuracion para la generacion de reportes
    DATE_REPORT = str(time.strftime('%Y%m%d%H%M%S'))
    FOLDER_BACKUP: str = os.path.join("files", "backups", DATE_REPORT)
    FOLDER_REPORT: str = os.path.join("files", "reports", DATE_REPORT)
    NAME_CONSOLIDATED = f"APLSTATS-Consolidated-{DATE_REPORT}.log"
    NAME_REPORT = f"APLSTATS-****-{DATE_REPORT}.log"
    NAME_COLUMNS: List[str] = ['date', 'mission', 'device_type', 'device_status', 'hash']

    def __new__(cls):
        """Método para crear una única instancia de la clase.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__load_config()
        return cls._instance

    def __load_config(self):
        """Método privado para cargar la configuración desde el archivo."""

        self.__configuration_file: dict = yaml.load(file.read_file(Util_Config.CONF_FILE_PATH).object,
                                                    Loader=yaml.FullLoader)

        # asignamos dinamicamente cada clave valor a un atributo de la instancia
        for key, value in self.__configuration_file.items():
            setattr(self, key, value)

    @classmethod
    def replace_name_report(cls, value):
        """Método de clase para reemplazar parte del nombre del reporte

        Args:
            value (str): El valor a reemplazar en el nombre del reporte
        """
        current_value = getattr(cls, "NAME_REPORT")
        setattr(cls, "NAME_REPORT", current_value.replace("****", value))
