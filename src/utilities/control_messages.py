import os
import yaml

class Mensage:
   
   __path = os.path.join("setting","message.yaml")
   
   __number: int   
   __type: str
   __message: str 
   __message_build: str 
   __part1: str 
   __part2: str
  
  
   def message_to_dic(self) -> dict:
      return {
         "number": self.__number,
         "type": self.__type,
         "message": self.__message,
         "message_build": self.__message_build,
         "part1": self.__part1,
         "part2": self.__part2,
      }
   
      
   def get_message(self, id_mesage:int) -> dict: 
         with open(self.__path) as file:
            contend = yaml.safe_load(file.read())
         return  contend[id_mesage]
      
   @classmethod
   def build_message(
                     self,
                     id_mesage:int,
                     default_mesage:str = "",
                     part1_mesage:str = "",
                     part2_mesage:str = "",
                     ) -> dict:
      
      """
         build_message, retorna un dict{} una que contiene un control de mensaje para mostrar como resultado de una operación         
        
        Args:
            id_mesage (int): Identifica el mensaje a retornar
            
            default_mesage (str): Argumento opcional, si se indica valor se retorna una estructura etablecida en caso contrario se retorna el mensaje del archivo de configuravion
            
            part1_mesage (str): Argumento opcional de complementa el mensaje principal
            
            part2_mesage (str): Argumento opcional de complementa el mensaje principal

        Returns:
            dict: Retorna diccionario con los siguientes claves:
                                                               - "number"        : Idenficidaroe del mensaje
                                                               - "type"          : Tipo de mensaje (warning, error, successful)
                                                               - "message"       : Mensaje principal
                                                               - "part1"         : Complemento 1 opcional del mensaje
                                                               - "part2"         : Complemento 2 opcional del mensaje
                                                               - "message_build" : Mensaje principal + Complemento 1 + Complemento 2
      """
      
      self.__number   = id_mesage
      self.__message  = default_mesage
      self.__type     = "warning"
      self.__part1    = part1_mesage
      self.__part2    = part2_mesage
      
      if default_mesage == "":
         contend = self.get_message(id_mesage)
         self.__message = contend["mensaje"]
         self.__type = contend["tipo"]
      
      self.__message_build = (f"{self.__message} {self.__part1} {self.__part2}").strip()

      return self.message_to_dic()
      
      






