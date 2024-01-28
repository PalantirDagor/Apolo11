import yaml
import os
import time
from typing import List
from src.utilities.files import FileUtils as file



class Util_Config:
    _instance = None

    # ruta del archivo de configuracion
    CONF_FILE_PATH : str = os.path.join("settings", "configuration_file.yaml")

    #configuracion para la simulacion
    DESTINATION_FILE: str = os.path.join("files", "devices")
    
    # Configuracion para la generacion de reportes
    DATE_REPORT = str(time.strftime('%Y%m%d%H%M%S'))
    FOLDER_BACKUP: str = os.path.join("files", "backups", DATE_REPORT)
    FOLDER_REPORT: str = os.path.join("files", "reports", DATE_REPORT)
    NAME_CONSOLIDATED = f"APLSTATS-Consolidated-{DATE_REPORT}.log"
    NAME_REPORT= f"APLSTATS-****-{DATE_REPORT}.log"
    NAME_COLUMNS: List[str] = ['date', 'mission', 'device_type', 'device_status', 'hash']


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        self.__configuration_file: dict = yaml.load(file.read_file(Util_Config.CONF_FILE_PATH).object,
                                                    Loader=yaml.FullLoader)

        # asignamos dinamicamente cada clave valor a un atributo de la instancia
        for key , value in self.__configuration_file.items():
            setattr(self,key,value)

    @classmethod
    def replace_name_report(cls, value,):
        current_value = getattr(cls, "NAME_REPORT")
        setattr(cls, "NAME_REPORT", current_value.replace("****",value))
