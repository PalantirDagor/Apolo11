import yaml
import os
from datetime import datetime
import time

from src.utilities.files import FileUtils as file

from src.utilities.generic import Utils as util

class Simulator_Apolo11:
    
    def __init__(self):
        self.__conf_file_path: str = "R:\Cursos\Python\ProyectoNASA\Apolo11\setting\configuration_file.yaml"
        #ProyectoNASA\Apolo11_backup_28122023
        #self.__conf_file_path: str = os.path.join("Apolo11_backup_28122023","setting","configuration_file.yaml" )
        self.__detination_path: str = "R:\Cursos\Python\ProyectoNASA\Apolo11\Files"
        self.__configuration_file: dict = yaml.load(file.read_file(self.__conf_file_path), Loader=yaml.FullLoader)
    
    def generate_data(self, mission : str) -> dict:
        """_summary_

        :param mission: _description_
        :type mission: str
        :return: _description_
        :rtype: dict
        """
        row: dict = {"date": time.strftime('%Y%m%d%H%M%S'), "mission": mission}
        
        if mission != "UNKN":
            row["device_type"] = util.generate_random2(self.__configuration_file["device_type"])
            row["device_status"] = util.generate_random2(self.__configuration_file["device_status"])
            row["hash"] = util.generate_hash(row.get("date"), row.get("mission"), row.get("device_type"))
            # Preguntar por si es necesario enviar es device_status en el hash
        else:
            row["device_type"] = "unknown"
            row["device_status"] = "unknown"   
            row["hash"] = ""         
        
        print(f"Star generate_data, row: {row}")
        return row
    
    def create_file(self, rows: int = 100) -> None:
        l_rows_file: list = []
        lv_mission: str = util.generate_random2(list(self.__configuration_file["mission"]))
        print(f"Star create files, mision: {lv_mission}")
        for i in range(0,rows):
            l_rows_file.append(self.generate_data(lv_mission))
            
        
        file.Save("json_.txt",self.__detination_path, l_rows_file)
            
        # Pasamos el diccionario a string
        #Head file
        l_file: list = []
        l_file.append(','.join(l_rows_file[0].keys())) 
        
        # Body file
        for row in l_rows_file:
            l_file.append(','.join(row.values()))
        
        #Save file
        file.Save("separado_comas.txt",self.__detination_path, l_file)
        
    def start_simulator(self):
        ln_files: int = util.generate_random(self.__configuration_file["file_quantity"][0], self.__configuration_file["file_quantity"][1])
        print(f"Start simulator: _Nro Files: {ln_files}")
        for i in range(0, ln_files):
            self.create_file()
            
    #print(os.path.join("hola")) 