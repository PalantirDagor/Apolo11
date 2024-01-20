import os
import yaml


class Mensage:
   __path = os.path.join("setting", "message.yaml")

   __number: int
   __type: str
   __state: bool
   __message: str
   __message_build: str
   __part1: str
   __part2: str
   __object: None

   @classmethod
   def message_to_dic(self) -> dict:
      return {"number": self.__number,
              "type": self.__type,
              "state": self.__state,
              "message": self.__message,
              "message_build": self.__message_build,
              "part1": self.__part1,
              "part2": self.__part2,
              "object": self.__object
              }

   @classmethod
   def get_message(self, id_mesage: int) -> dict:
      with open(self.__path) as file:
         contend = yaml.safe_load(file.read())
      return contend[id_mesage]

   @classmethod
   def build_message(self,
                     id_mesage: int,
                     default_mesage: str = "",
                     part1_mesage: str = "",
                     part2_mesage: str = "",
                     obj: None = None) -> dict:
      
      """
      build_message, retorna un dict{} una que contiene un control de mensaje para mostrar como resultado
      de una operación

      Args:
         -id_mesage (int): Identifica el mensaje a retornar
         -type_mesage (str): Identifica el tipo de mensaje
         -default_mesage (str): Argumento opcional, si se indica valor se retorna una estructura establecida
         en caso contrario se retorna el mensaje del archivo de configuracion
         -part1_mesage (str): Argumento opcional de complementa el mensaje principal
         -part2_mesage (str): Argumento opcional de complementa el mensaje principal
         -obj (None): Argumento opcinal que puede capturar un objeto

      Returns:
         dict: Retorna diccionario con los siguientes claves:

         - "number"        : Idenficidaroe del mensaje
         - "type"          : Tipo de mensaje (warning, error, successful)
         - "state"         : True indicando la operacion se efectuo con exito False en caso contrario
         - "message"       : Mensaje principal
         - "part1"         : Complemento 1 opcional del mensaje
         - "part2"         : Complemento 2 opcional del mensaje
         - "message_build" : Mensaje principal + Complemento 1 + Complemento 2
         - "object"        : Object
      """
      self.__number = id_mesage
      self.__message = default_mesage
      self.__type = "warning"
      self.__state = False
      self.__part1 = part1_mesage
      self.__part2 = part2_mesage
      self.__object = obj

      if default_mesage == "":
         contend = self.get_message(id_mesage)
         self.__message = contend["mensaje"]
         self.__type = contend["tipo"]
         self.__state = contend["estado"]

      self.__message_build = (f"{self.__message} {self.__part1} {self.__part2}").strip()

      contenido = self.message_to_dic()
      return contenido
