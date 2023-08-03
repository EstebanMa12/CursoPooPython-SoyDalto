class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def origen(self):
        print(f'{self.nombre} es de {self.nacionalidad}')

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def decirHabilidad(self):
        print(f'Mi habilidad es {self.habilidad}')

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

Aurelio = EmpleadoArtista("Aurelio",34,"Paraguayo","Cascar re duro",5000000, "Guardias del sur")
Aurelio.decirHabilidad()
Aurelio.origen()


