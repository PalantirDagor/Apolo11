class EMessage:
   
   number: int   
   type: str
   message: str 
   part1: str 
   part2: str
   part3: str 

   def __init__(self,number,message):
      self.number = number
      self.message = message
      pass

   def to_dic(self) -> dict:
      
      return {
         "number": self.number,
         "message": self.message
      }
      

def cualquir():

   instancia = EMessage(1,"HOLA MUNDO")

   print(instancia.to_dic())







