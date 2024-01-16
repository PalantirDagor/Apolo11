import os
import json
import pandas as pd
import shutil
import time
import matplotlib.pyplot as plt
import seaborn as sns
#from src.utilities.files import FileUtils as file

class file:
    
    @classmethod 
    def read_file(cls,path_file: str) -> str: 
        with open(path_file) as file:
            return file.read()
        
    @classmethod
    def move_file(cls, 
                origin_path: str, 
                destination_path: str,
                filename:str = None) -> dict:
        
            
            
        if not os.path.exists(origin_path):
            return False

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

            if filename is None:
                files = os.listdir(origin_path)

                for file in files:
                    shutil.move(os.path.join(origin_path, file),
                                os.path.join(destination_path, file))
            else:
                shutil.move(os.path.join(origin_path, filename),
                            os.path.join(destination_path, filename)
                            )

        return True

    @classmethod
    def Save(cls, name: str, path: str, data: list[str]):
        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, name), 'a') as file:
            for row in data:
                file.write(str(row) + '\n')


class Report:

    def __init__(self):
        self.__folder_path: str = os.path.join("Files", "Devices")
        self.__date_report = str(time.strftime('%Y%m%d%H%M%S'))
        self.__folder_backup: str = os.path.join("Files", "Backup", self.__date_report)
        self.__folder_report: str = os.path.join("Files", "Report", self.__date_report)
        self.__name_report = f"APLSTATS-Control_Panel-{self.__date_report}.log"
        self.__name_consolidated = f"APLSTATS-Consolidated_Files-{self.__date_report}.log"

    def consolidate_files(self):
        records = []

        for file_name in os.listdir(self.__folder_path):
            file_path = os.path.join(self.__folder_path, file_name)
            lines = file.read_file(file_path).splitlines()
            for line in lines:
                data = json.loads(line.replace("'", "\""))
                record = list(data.values())
                records.append(record)

        return list(records)

    def save_in_dashboard(self, data, title):

        info: list[str] = []

        head = f'''
        {'-' * len(title)}
        {title}
        {'-' * len(title)}
        '''

        file.Save(self.__name_report, self.__folder_report, [head])

        if isinstance(data, pd.core.frame.DataFrame):
            info = [str(row) for row in data.to_string(index=False).split('\n')]
        else:
            info.append(str(data))

        file.Save(self.__name_report, self.__folder_report, info)
    
    def add_header():
        def decorador(func):
            def wrapper(self, data, title):
                
                head = f"""
                {'*' * len(title)}
                {title}
                {'*' * len(title)}
                """
                func(self, data, head)

            return wrapper
        return decorador
    
    @add_header()
    def save_in_dashboard(self, data, title):

        info: list[str] = []
        
        if isinstance(data, pd.core.frame.DataFrame):
            info = [str(row) for row in data.to_string(index=False).split('\n')]
        else:
            info.append(str(data))
        
        # Agrego un titulo al conjunto de datos
        file.Save(self.__name_report, self.__folder_report, [title])
        
        # Agrego el conjunto de datos
        file.Save(self.__name_report, self.__folder_report, info)


    def event_analysis(self, df):
        filter = (df.groupby(['mission', 'device_type', 'device_status'])
                  .size()
                  .rename('number_events')
                  .reset_index()
                  .sort_values(by=['mission', 'device_type', 'device_status', 'number_events'],
                               ascending=[True, True, True, False]))
        return filter

    def disconnection_management(self, df):

        unknown_devices = df[df['device_status'] == 'unknown']

        # Encontrar los dispositivos con el mayor número de desconexiones para cada misión
        number_disconnections = (unknown_devices.groupby(['mission', 'device_type'])
                                 .size()
                                 .rename('number_disconnections')
                                 .reset_index()
                                 .sort_values(by='number_disconnections',
                                              ascending=False))

        return number_disconnections

    def killed_devices(self, df):
        return len(df[df['device_status'] == 'killed'])

    def calculate_percentage(self, df):

        filter = (df.groupby(['mission', 'device_type'])
                  .size()
                  .rename('count_data')
                  .reset_index()
                  .sort_values(by=['mission', 'count_data'],
                               ascending=[True, False]))

        filter['percentage_data'] = ((filter.count_data / len(df) * 100).round(2).astype(str) + ' %')

        return filter

    def save_graphic(self, df, chart_type, title):

        match chart_type:
            case 1:

                graphic = sns.catplot(x='device_status', y='number_events', hue='device_type',
                                      col='mission', data=df, kind='bar', height=2, aspect=1.5,
                                      palette='viridis', col_wrap=2)
                graphic.set_axis_labels('Estados', 'Número de Eventos')
                graphic.set_titles('Misión: {col_name}')
                graphic.add_legend(title='Dispositivo', bbox_to_anchor=(1, 0.5), loc='right')
                graphic.fig.suptitle(title, y=1)

                graphic.fig.savefig(os.path.join(self.__folder_report, "graphic1.png"))
                plt.close()

            case 2:
                pass

    def generate_dashboard(self, df):
        # Análisis de eventos
        e_a = self.event_analysis(df)
        title = "Candidad de eventos por estado para cada mision y dispositivo"
        self.save_graphic(e_a, 1, title)
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

    def start_process(self):
        consolidate_events = process.consolidate_files()

        # Creo un archivo con los datos consolidados
        file.Save(self.__name_consolidated, self.__folder_report, consolidate_events)

        # Creo un DataFrame con los datos concolidados
        df = pd.DataFrame(consolidate_events, columns=['date', 'mission', 'device_type', 'device_status', 'hash'])

        # Genero los diferentes tipos de reportes
        process.generate_dashboard(df)


process = Report()
process.start_process()
