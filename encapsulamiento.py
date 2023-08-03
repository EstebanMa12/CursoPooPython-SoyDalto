class Encap:
    def __init__(self):
        self.__soy_muy_privado= "valor"


objeto = Encap()
""" print(objeto.__soy_muy_privado) """
""" AttributeError: 'Encap' object has no attribute '__soy_muy_privado'. Did you mean: '_Encap__soy_muy_privado'? """

""" -------------------------GETTERS Y SETTERS -----------------------------------------------------"""
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,newnombre):
        self.__nombre=newnombre
    
Esteban=Persona("Esteban",15)

nombreEsteban= Esteban.get_nombre()
print(nombreEsteban)

Esteban.set_nombre("Daniel Esteban")
nombreEsteban=Esteban.get_nombre()

print(nombreEsteban)