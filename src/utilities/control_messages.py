import os
import yaml


class Message:

    __path = os.path.join("settings", "message.yaml")

    with open(__path) as file:
        __message_list = yaml.safe_load(file.read())

    @classmethod
    def build_message(cls,
                      id_mesage: int,
                      type: str,
                      default_mesage: str = "",
                      part1_mesage: str = "",
                      part2_mesage: str = "",) -> dict:

        """
       build_message, retorna un dict{} una que contiene un control de mensaje para mostrar como resultado
       de una operación

       Args:
          -id_mesage (int): Identifica el mensaje a retornar
          -type_mesage (str): Identifica el tipo de mensaje (E = error , S = exitoso, W = alerta, I = Info)
          -default_mesage (str): Argumento opcional, si se indica valor se retorna una estructura establecida
          en caso contrario se retorna el mensaje del archivo de configuracion
          -part1_mesage (str): Argumento opcional de complementa el mensaje principal
          -part2_mesage (str): Argumento opcional de complementa el mensaje principal

       Returns:
          dict: Retorna diccionario con los siguientes claves:
          - "state"         : True indicando la operacion se efectuo con exito False en caso contrario
          - "message"       : Mensaje principal
          - "part1"         : Complemento 1 opcional del mensaje
          - "part2"         : Complemento 2 opcional del mensaje
          - "message_build" : Mensaje principal + Complemento 1 + Complemento 2
       """

        __message = default_mesage
        __part1 = part1_mesage
        __part2 = part2_mesage

        # self.lectura(self)

        if default_mesage == "":
            __message = Message.__message_list[id_mesage]

        if type.upper() == 'S' or type.upper() == 'W' or type.upper() == 'I':
            __state = True
        else:
            __state = False

        __message_build = (f"{__message} {__part1} {__part2}").strip()

        return {"state": __state,
                "message": __message,
                "message_build": __message_build,
                "part1": __part1,
                "part2": __part2}
