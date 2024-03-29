import logging
from src.utilities.logging.logger_apolo11 import get_logger
from random import (randrange, choice)
from typing import List, Tuple
from pydantic import BaseModel
from typing import Dict, Union

logger = get_logger('Utils', logger_level=logging.ERROR)


class Utils():

    # genera el aleatorio de las listas de misiones, estados etc..
    @staticmethod
    def generate_random(list_elements: List[str]) -> str:
        """generate_random, Entrega de manera aleatoria un elemento del tipo cadena de texto

        Args:
            list_elements (List[str]): lista con los elementos que será enviado 1 de ellos de manera aleatoria

        Returns:
            str: Retorna un elemento en cadena de texto
        """

        try:
            return choice(list_elements)
        except Exception as e:
            logger.error('generate_random2', e)
            return

    @staticmethod
    def generate_random_number(initial_value: int, final_value: int) -> int:
        """generate_random, Entrega de manera aleatoria un elemento del tipo numérico entero entre dos valores

        Args:
            initial_value (int): número inicial que indica el comienzo de la búsqueda del número aleatorio
            final_value (int): número final hasta donde se dará la búsqueda del número aleatorio

        Returns:
            int: Retorna un número entero
        """

        try:
            number_random: int = randrange(initial_value, final_value, 1)
            return number_random
        except Exception as e:
            logger.error("generate_random", e)
            return

    @staticmethod
    def generate_hash(*datos: Tuple) -> str:
        """generate_random, Entrega de manera aleatoria un elemento del tipo numérico entero entre dos valores

        Returns:
            str: Retorna un hash encriptado del tipo cadena de texto
        """
        return str(hash(datos))


class Util_Return(BaseModel):
    """La clase se utiliza para representar valores de retorno

    Args:
        BaseModel (_type_): hereda BaseModel  debido a que esta utilizando Pydantic para definir modelos de datos.
    """

    object: object
    message: Dict[str, Union[bool, str, str, str]]
