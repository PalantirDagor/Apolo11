import shutil
import os
from src.utilities.control_messages import Message as message
from src.utilities.generic import Util_Return


class FileUtils():

    @classmethod
    def Save(cls, name: str, path: str, data: list[str]) -> Util_Return:
        """
        Save, Guarda en un archivo la información  entregada

        Args:
            name (str): Nombre asignado para el archivo, con extensión incluida "NameFile.log"

            path (str): Ruta donde se creará  el archivo

            data (str): Contiene los datos que se crearan en el archivo

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = None,
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario
        Note:
            - Si el archivo ya existe en la ruta de destino este adicionara el nuevo dato en una línea nueva
        """
        try:

            if not os.path.exists(path):
                os.makedirs(path)

            with open(os.path.join(path, name), 'a') as file:
                for row in data:
                    file.write(str(row) + '\n')

            return Util_Return(object=None, message=message.build_message(id_mesage=0, type="S"))
        except Exception as e:
            return Util_Return(object=None, message=message.build_message(0,
                                                                          "E",
                                                                          str(e.args[1]),
                                                                          str(e.filename),
                                                                          str(e.filename2)))

    @classmethod
    def read_file(cls, path_file: str) -> Util_Return:
        """
        read_file, lee la información  contenida en el archivo especificado y lo retorna como un string

        Args:
            path_file (str): Ruta del archivo a leer

        Returns:
            Util_Return: Retorna un objeto con dos atributos, 1 Object = string con la informacion leida,
            2 Dict con mensaje del resultado de la operación, y un estado True si la operación
            finalizo con éxito o False en caso contrario
        """
        try:
            with open(path_file) as file:
                read = file.read()
                return Util_Return(object=read, message=message.build_message(id_mesage=0, type="S"))
        except Exception as e:
            return Util_Return(object=None, message=message.build_message(0, "E", str(e.args[1])))

    @classmethod
    def move_file(cls,
                  origin_path: str,
                  destination_path: str,
                  filename: str = None) -> Util_Return:
        """
            move_file, mueve los archivos de la ruta origen a una ruta destino, si el archivo ya existe
            en la ruta de destino este se remplazará

            Args:
                origin_path (str): Ruta de origen de del archivo

                origin_path (str): Ruta de destino de los archivos

                filename (str): Nombre del archivo a copiar, si no se envía valor se copian todos los archivos
                de la ruta origen a destino

            Returns:
                Util_Return: Retorna un objeto con dos atributos, 1 Object = None,
                2 Dict con mensaje del resultado de la operación, y un estado True si la operación
                finalizo con éxito o False en caso contrario

            Note:
                -Si el archivo ya existe en la ruta de destino este se remplazará
        """
        try:

            if not os.path.exists(origin_path):
                return Util_Return(object=None,
                                   message=message.build_message(id_mesage=1, type="W", part1_mesage=origin_path))
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            if filename is None:
                files = os.listdir(origin_path)

                for file in files:
                    shutil.move(os.path.join(origin_path, file),
                                os.path.join(destination_path, file))
            else:
                shutil.move(os.path.join(origin_path, filename),
                            os.path.join(destination_path, filename))

            return Util_Return(object=None,
                               message=message.build_message(id_mesage=0, type="S"))
        except Exception as e:
            return Util_Return(object=None,
                               message=message.build_message(0,
                                                             "E",
                                                             str(e.args[1]),
                                                             str(e.filename),
                                                             str(e.filename2)))
