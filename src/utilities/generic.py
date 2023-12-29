import hashlib 
from random import (randrange, choice)

# Ajustar los metodos a metodos de clase
class Utils:

    # genera el aleatorio de las listas de misiones, estados etc..
    @classmethod
    def generate_random2(cls, list_elements: list) -> str:
        """
        generate_random, Entrega de manera aleatoria un elemento del tipo cadena de texto        
        
        Args:
            list_elements (list[str]): lista con los elementos que será enviado 1 de ellos de manera aleatoria

        Returns:
            String: Retorna un elemento en cadena de texto
            
        Note:
            -Puede servir para entregar aleatoriamente cualquier dato dentro de esta lista de elementos de cadena de texto
        """

        try:
            index: int  = randrange(start= len(list_elements))
            element: str = list_elements[index]

            return element

        except Exception as e:

            #logger.error("Utils.generate_random", e)

            return

    @classmethod
    def generate_random(cls, initial_value: int, final_value: int) -> int:
        """
        generate_random, Entrega de manera aleatoria un elemento del tipo numérico entero entre dos valores       
        
        Args:
            initial_value (int): número inicial que indica el comienzo de la búsqueda del número aleatorio

            final_value (int): número final hasta donde se dará la búsqueda del número aleatorio

        Returns:
            int: Retorna un número entero

        Note:
            -Puede servir para entregar aleatoriamente cualquier número dentro del rango enviado a la función
        """

        try:
            number_random: int = randrange(initial_value, final_value, 1)

            return number_random

        except Exception as e:

            #logger.error("Utils.generate_random", e)

            return
    
    @classmethod
    def generate_hash(cls, *datos) -> str:
        """        
        generate_random, Entrega de manera aleatoria un elemento del tipo numérico entero entre dos valores       
        
        Args:
            *datos (tuple): tupla con todos los parametros que se envian a la funcion

        Returns:
            str: Retorna un hash encriptado en sha256

        Note:
            -Puede servir para entregar un hash con buena encriptacion
        """
        
        return str(hash(datos))
    
