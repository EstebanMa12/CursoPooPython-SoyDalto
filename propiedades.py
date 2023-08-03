class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,newnombre):
        self.__nombre=newnombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
Esteban=Persona("Esteban",15)

nombreEsteban= Esteban.nombre
print(nombreEsteban)

