import os
import shutil


class FileUtils:

    @classmethod
    def Save(cls, name: str, path: str ,data: str) -> bool:
        """
         Save, Guarda en un archivo la informacion entregada        
        
        Args:
            name (str): Nombre asignado para el archivo, con extencion incluida "NameFile.txt"
            
            path (str): Ruta donde se creara el archivo
            
            data (str): Contiene los datos que se crearan en el archivo

        Returns:
            Bool: Retorna True si se logra crear el archivo, en caso contrario retorna False
            
        Note:
            -Si el archivo ya existe en la ruta de destino este adicionara el nuevo dato en una linea nueva
        """
        try:
            
            if not os.path.exists(path):
                os.makedirs(path)
                
            with open(os.path.join(path,name), 'a') as file:
                file.write(str(data) + '\n')
                
            return True        
        except Exception as e:
            return False
    
    @classmethod
    def read_file(cls,path_file: str) -> str: 
        """
         read_file, lee la informacion contenida en el archivo especificado y lo retorna como un string        
        
        Args:
            path_file (str): Ruta del archivo a leer

        Returns:
            str: Retorna string con el contenido del archivo leeido
        """
        with open(path_file) as file:
            return file.read()
    
          
    @classmethod
    def move_file(cls,origin_path: str,destination_path: str) -> bool:
        
        """
        move_file, mueve los archivos de la ruta origen a una ruta destino, si el archivo ya existe en la ruta de destino este se remplazara

        Args:
            origin_path (str): Ruta de origen de los archivos
            
            origin_path (str): Ruta de destino de los archivos

        Returns:
            bool: Retorna True si los archivos de movieron con exito, en caso contrario se retorna False
        
        Note:
            -Si el archivo ya existe en la ruta de destino este se remplazara
        """
        try:
            
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
        
            files = os.listdir(origin_path) 
        
            for file in files:
                shutil.move(os.path.join(origin_path, file),
                            os.path.join(destination_path, file)
                            )

            return True        
        except Exception as e:
            return False
         
    
    @classmethod
    def copy_file(cls,origin_path: str,destination_path: str) -> bool:
        """
        copy_file, copia los archivos de la ruta origen a una ruta destino, si el archivo ya existe en la ruta de destino este se remplazara
        
        Args:
            origin_path (str): Ruta de origen de los archivos
            
            origin_path (str): Ruta de destino de los archivos

        Returns:
            bool: Retorna True si los archivos de movieron con exito, en caso contrario se retorna False
        
        """
        try:
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            
            files = os.listdir(origin_path) 
            
            for file in files:
                shutil.copy(os.path.join(origin_path, file),
                            os.path.join(destination_path, file)
                            ) 
                
            return True        
        except Exception as e:
            return False
        
    @classmethod
    def delete_file(cls,path_file: str) -> bool:
        """
        delete_file, elimina el archivo especificado
        
        Args:
            path_file (str): Ruta del archivo a eliminar

        Returns:
            bool: Retorna True si el archivo se elimino exitosamente, en caso contrario se retorna False
        
        """
        try:
            os.remove(path_file)
            return True        
        except Exception as e:
            return False
    
    @classmethod
    def clear_folder(cls,path_folder: str) -> bool:
        """
        clear_folder, elimina los archivos contenidos dentro de la carpeta especificada
        
        Args:
            path_folder (str): Ruta de la carpeta a limpiar

        Returns:
            bool: Retorna True si la carpeta se limpio exitosamente, en caso contrario se retorna False
        """

        try:
            files = os.listdir(path_folder)
            for file in files:
                path_file = os.path.join(path_folder, file)
                os.remove(path_file)
            return True        
        except Exception as e:
            return False
    

    

