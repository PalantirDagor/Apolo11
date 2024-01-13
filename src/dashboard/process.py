import os
import json
import pandas as pd
import shutil
import time
#from src.utilities.files import FileUtils as file

class file:
    
    @classmethod 
    def read_file(cls,path_file: str) -> str: 
        with open(path_file) as file:
            return file.read()
        
    @classmethod
    def move_file(cls, origin_path: str, destination_path: str):

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            
            files = os.listdir(origin_path)
            
            for file in files:
                shutil.move(os.path.join(origin_path, file),
                            os.path.join(destination_path, file)
                            )

    @classmethod
    def Save(cls, name: str, path: str, data: list[str]):
        if not os.path.exists(path):
            os.makedirs(path)
                
        with open(os.path.join(path,name), 'a') as file:
            for row in data:
                file.write(str(row) + '\n')

class Report:  
  
    def __init__(self, date, mission, device_type, device_status, hash):
        self.date = date
        self.mission = mission
        self.device_type = device_type
        self.device_status = device_status
        self.hash = hash

    def __iter__(self):
        return iter([self.date, 
                self.mission, 
                self.device_type,
                self.device_status,
                self.hash])

def consolidate_files(folder_path):
    records = []
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        lines = file.read_file(file_path).splitlines()
        for line in lines:
            data = json.loads(line.replace("'", "\""))
            record = Report(**data)
            records.append(list(record))

    return list(records)

def generate_dashboard(df,name_report,folder_report):
    # Análisis de eventos
    e_a = event_analysis(df)
    save_in_dashboard (e_a,name_report,"Candidad de eventos por estado para cada mision y dispositivo")

    # Gestión de desconexiones
    c_dm = disconnection_management(df)
    save_in_dashboard (e_a,name_report,"Dispositivos con número de desconexiones (unknown) por misión")
    
    # Consolidación de misiones
    d_kd = killed_devices(df)
    save_in_dashboard (e_a,name_report,"Cantidad de dispositivos inoperables")
    
    # Cálculo de porcentajes
    e_cp = calculate_percentage(df)
    save_in_dashboard (e_a,name_report,"Porcentaje de datos generados por dispositivos y mision")


def save_in_dashboard(data,name_report,folder_report,title):
    
    file.Save(name_report,folder_report,title)
    datos = [str(row) for row in data.to_records(index=False)] 
    file.Save(name_report,folder_report,datos)
    

# Se encarga de pasar los archivos de la ruta A a B y limpiar el directorio
def clean_directory(self):
    pass

def event_analysis(df):
    
    prueba = (df.groupby(['mission', 'device_type', 'device_status']).size()
                                                                               .rename('number_events')
                                                                               .reset_index()
                                                                               .sort_values(by=['mission','device_type','device_status','number_events'], ascending=[True,True,True,False])
                                                                               )
    return prueba

def disconnection_management(df):
    
    unknown_devices = df[df['device_status'] == 'unknown']

    # Encontrar los dispositivos con el mayor número de desconexiones para cada misión
    number_disconnections = (unknown_devices.groupby(['mission', 'device_type']).size()
                                                                               .rename('number_disconnections')
                                                                               .reset_index()
                                                                               .sort_values(by='number_disconnections', ascending=False)
                                                                               )

    #number_disconnections = number_disconnections.drop_duplicates(subset='mission')
    
    return number_disconnections

def killed_devices(df):
    return len(df[df['device_status'] == 'killed'])
    #return killed.mission.count()

def calculate_percentage(df):
    
    filter =  (df.groupby(['mission', 'device_type'])
                                                    .size()
                                                    .rename('count_data')
                                                    .reset_index()
                                                    .sort_values(by=['mission','count_data'], ascending=[True,False]))
    
    filter['percentage_data'] = ((filter.count_data / len(df) * 100).round(2).astype(str) + ' %')

    return filter




####
####
####
# ORQUESTADOR
####
####
####
folder_path : str = os.path.join("Files", "Devices")

date_report = str(time.strftime('%Y%m%d%H%M%S'))
folder_backup : str = os.path.join("Files", "Backup",date_report)
folder_report : str = os.path.join("Files", "Report",date_report)

consolidate_events = consolidate_files(folder_path)

#Creo un archivo con los datos consolidados
file.Save(f"APLSTATS-Consolidated_Files-{date_report}.log",folder_report,consolidate_events)

#Creo un DataFrame con los datos concolidados
df = pd.DataFrame(consolidate_events,columns=['date', 'mission', 'device_type', 'device_status', 'hash'])

# Genero los diferentes tipos de reportes
name_report = f"APLSTATS-Control_Panel-{date_report}.log"
generate_dashboard(df,name_report,folder_report)





















