import yaml
import os
from datetime import datetime
import time

from src.utilities.files import FileUtils as file
from src.utilities.generic import Utils as util

class Simulator_Apolo11:
    
    def __init__(self, execution_number: int):
        
        self.__execution_number: int = execution_number
        
        self.__conf_file_path: str = os.path.join("setting","configuration_file.yaml")
        self.__detination_path: str = os.path.join("Files", "Devices")
        self.__configuration_file: dict = yaml.load(file.read_file(self.__conf_file_path), Loader=yaml.FullLoader)
        self.__consecutive_file: dict[str,int] = {}


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
            row["hash"] = util.generate_hash(row.get("date"), 
                                             row.get("mission"), 
                                             row.get("device_type"),
                                             row.get("device_status"))
        else:
            row["device_type"] = "unknown"
            row["device_status"] = "unknown"   
            row["hash"] = ""         
        
        #print(f"Star generate_data, row: {row}")
        return row


    def create_file(self, rows: int = 1) -> None:
        l_rows_file: list = []
        lv_mission: str = util.generate_random2(self.__configuration_file["mission"])
        #print(f"Star create files, mision: {lv_mission}")
        for i in range(0,rows):
            l_rows_file.append(self.generate_data(lv_mission))

        # Pasamos el diccionario a string
        #Head file
        l_file: list = []
        l_file.append(','.join(l_rows_file[0].keys())) 
        
        # Body file
        for row in l_rows_file:
            l_file.append(','.join(row.values()))
        
        #Save file
        file.Save(self.filename(lv_mission),self.__detination_path, l_rows_file)


    def filename(self, mission: str) -> str:
        
        if self.__consecutive_file.get(mission) == None:
            self.__consecutive_file[mission] = 1
        else:
            self.__consecutive_file[mission] = self.__consecutive_file.get(mission) + 1   
        
        # Esctructura del filename: APL[ORBONE|CLNM|TMRS|GALXONE|UNKN]-0000[1-1000].log.
        return f"APL{mission}-{self.__execution_number:0>4}-{self.__consecutive_file.get(mission):0>4}.log"    


    def start_simulator(self):
        
        ln_files: int = util.generate_random(self.__configuration_file["file_quantity"][0], 
                                             self.__configuration_file["file_quantity"][1])
        
        print(f"Start simulator: _Nro Files: {ln_files}")
        for i in range(0, ln_files):
            self.create_file()