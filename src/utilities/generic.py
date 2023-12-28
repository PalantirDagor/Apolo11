from random import (randrange, choice)

# Ajustar los metodos a metodos de clase
class Utils:

    # genera el aleatorio de las listas de misiones, estados etc..
    def generate_random(self, list_elements: list) -> str:

        index: int  = randrange(start= len(list_elements))
        element: str = list_elements[index]

        return element

    def generate_random(self, initial_value: int, final_value: int) -> int:
        
        number_random: int = randrange(initial_value, final_value, 1)

        return number_random
    
    def generate_hash(self, *datos) -> str:
        
        hash_str = ''.join(datos)

        return hash_str
