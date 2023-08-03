class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def printName(self):
        print( f'Soy {self.nombre} y mi edad es {self.edad}')
    

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado=grado

    def gradoprint(self):
        print( f'Estoy en grado {self.grado}')
    
nombre=input('Ingrese el nombre: ')
edad= input('Ingrese la edad: ')
grado =input('Ingrese el grado: ') 

estudiante= Estudiante(nombre,edad,grado)

estudiante.printName()
estudiante.gradoprint()
