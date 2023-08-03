class  Estudiante:
    def __init__(self, Nombre,Edad, Grado):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Grado=Grado

    def estudiar(self):
        print(f'El  estudiante {self.Nombre} esta estudiando')

nombre = input("Ingrese el nombre del estudiante ")
edad = input('Ingrese la edad')
grado = input('Ingrese el grado ')


estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre:{estudiante.Nombre}\n
      Edad: {estudiante.Edad}\n
      Grado: {estudiante.Grado}\n """)

while True:
    estudiar=input()
    if (estudiar.lower()== "estudiar"):
        estudiante.estudiar()
    elif (estudiar.lower()=="salir"):
        break