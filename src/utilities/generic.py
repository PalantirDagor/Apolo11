import hashlib
from random import (randrange, choice)

# Ajustar los metodos a metodos de clase
class Utils:

    # genera el aleatorio de las listas de misiones, estados etc..
    @classmethod
    def generate_random(cls, list_elements: list) -> str:

        index: int  = randrange(start= len(list_elements))
        element: str = list_elements[index]

        return element

    @classmethod
    def generate_random1(cls, initial_value: int, final_value: int) -> int:
        
        number_random: int = randrange(initial_value, final_value, 1)

        return number_random
    
    @classmethod
    def generate_hash(cls, *datos) -> str:       
        return str(hash(datos)) 
        #return str(hashlib.sha256(''.join(datos).encode).hexdigest())
