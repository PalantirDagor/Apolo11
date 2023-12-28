
import os
import shutil
from src.utilities.control_messages import Mensage as message

class FileUtils:

    @classmethod
    def Save(cls, name: str, path: str, data: list[str]) -> dict:
        """
         Save, Guarda en un archivo la informacion entregada        
        
        Args:
            name (str): Nombre asignado para el archivo, con extencion incluida "NameFile.txt"
            
            path (str): Ruta donde se creara el archivo
            
            data (str): Contiene los datos que se crearan en el archivo

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado (successful,warning) y un estado True si la operacion finalizo con exito o False en caso contrario 
            
        Note:
            - Si el archivo ya existe en la ruta de destino este adicionara el nuevo dato en una linea nueva
        """
        try:
            
            if not os.path.exists(path):
                os.makedirs(path)
                
            with open(os.path.join(path,name), 'a') as file:
                for row in data:
                    file.write(str(row) + '\n')
                
            return  message.build_message(id_mesage = 0)    
            #return None    
        except Exception as e:
            return message.build_message(0,str(e.args[1]),e.filename,e.filename2)
            #return None
    
    
    @classmethod
    def read_file(cls,path_file: str) -> str: 
        """
        read_file, lee la informacion contenida en el archivo especificado y lo retorna como un string        
        
        Args:
            path_file (str): Ruta del archivo a leer

        Returns:
            str: Retorna string con el contenido del archivo leeido, en caso de un error retorna un valor None
        """
        try:
            
            with open(path_file) as file:
                return file.read()
        except Exception as e:
            return None
    
    '''
    @classmethod
    def move_file(cls,origin_path: str,destination_path: str) -> dict:
        
        """
        move_file, mueve los archivos de la ruta origen a una ruta destino, si el archivo ya existe en la ruta de destino este se remplazara

        Args:
            origin_path (str): Ruta de origen de los archivos
            
            origin_path (str): Ruta de destino de los archivos

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado (successful,warning) y un estado True si la operacion finalizo con exito o False en caso contrario 
        
        Note:
            -Si el archivo ya existe en la ruta de destino este se remplazara
        """
        try:
            
            if not os.path.exists(origin_path):
                return  message.build_message(id_mesage = 1,part1_mesage = origin_path)
            
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
        
            files = os.listdir(origin_path) 
        
            for file in files:
                shutil.move(os.path.join(origin_path, file),
                            os.path.join(destination_path, file)
                            )

            return  message.build_message(id_mesage = 0)          
        except Exception as e:
            return message.build_message(0,str(e.args[1]),e.filename,e.filename2)
    
    @classmethod
    def delete_file(cls,path_file: str) -> dict:
        """
        delete_file, elimina el archivo especificado
        
        Args:
            path_file (str): Ruta del archivo a eliminar

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado (successful,warning) y un estado True si la operacion finalizo con exito o False en caso contrario 
        
        """
        try:
            if not os.path.exists(path_file):
                return  message.build_message(id_mesage = 3,part1_mesage = path_file)
            
            os.remove(path_file)
            
            return  message.build_message(id_mesage = 0)        
        except Exception as e:
            return message.build_message(0,str(e.args[1]),e.filename,e.filename2)
    
    @classmethod
    def clear_folder(cls,path_folder: str) -> dict:
        """
        clear_folder, elimina los archivos contenidos dentro de la carpeta especificada
        
        Args:
            path_folder (str): Ruta de la carpeta a limpiar

        Returns:
            Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado (successful,warning) y un estado True si la operacion finalizo con exito o False en caso contrario 
        """

        try:
            
            if not os.path.exists(path_folder):
                return  message.build_message(id_mesage = 2,part1_mesage = path_folder)
            
            files = os.listdir(path_folder)
            for file in files:
                path_file = os.path.join(path_folder, file)
                os.remove(path_file)
                
            return message.build_message(id_mesage = 0) 
              
        except Exception as e:
            return message.build_message(0,str(e.args[1]),e.filename,e.filename2)

    @classmethod
    def copy_file(cls,origin_path: str,destination_path: str) -> dict :
            """
            copy_file, copia los archivos de la ruta origen a una ruta destino, si el archivo ya existe en la ruta de destino este se remplazara

            Args:
                origin_path (str): Ruta de origen de los archivos
                
                origin_path (str): Ruta de destino de los archivos

            Returns:
                Dict: Retorna diccionario con mensaje del resultado de la operacion, tipo de resultado (successful,warning) y un estado True si la operacion finalizo con exito o False en caso contrario 
            
            Note:
                -Si el archivo ya existe en la ruta de destino este se remplazara
            """
            try:
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                if not os.path.exists(origin_path):
                    return  message.build_message(id_mesage = 1,part1_mesage = origin_path)

                files = os.listdir(origin_path) 
                
                for file in files:
                    shutil.copy(os.path.join(origin_path, file),
                                os.path.join(destination_path, file)
                                ) 
                    
                return  message.build_message(id_mesage = 0)      
            except Exception as e:
                return message.build_message(0,str(e.args[1]),e.filename,e.filename2)

mlist: list = [123, 345,566,777]

FileUtils.Save("hola.txt","R:\Cursos\Python\ProyectoNASA\Apolo11\Files",mlist)

'''
