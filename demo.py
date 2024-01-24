from src.utilities.generic import Utils as util


myclass = util()
prueba1 = myclass.generate_random(["a", "b", "c", "d", "e", "f"])
prueba2 = myclass.generate_random(1,15)
print(prueba1)
print(prueba2)