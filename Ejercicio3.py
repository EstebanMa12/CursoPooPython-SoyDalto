# Crear un juego de fusión.
# EI juego consiste en crear personajes un juego y que esos personajes se puedan fusionar
# para formar personajes más poderosos que tengan más poder.
# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
# se fusionen, salga un nuevo personaje con habilidades mejoradas,
# una posible es: el promedio de las habilidades de ambos, al cuadrado


class Personaje:
    def __init__(self,nombre, fuerza, velocidad):
        self.nombre= nombre
        self.fuerza = fuerza
        self.velocidad = velocidad 

    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    def __add__(self,otro_pj):
        nuevoNombre= self.nombre[:3] +"-"+otro_pj.nombre[len(otro_pj.nombre)-3:]
        nuevaFuerza= ((self.fuerza +otro_pj.fuerza)/2)**2
        nuevaVelocidad= ((self.velocidad +otro_pj.velocidad)/2)**2
        return Personaje(nuevoNombre, nuevaFuerza, nuevaVelocidad)
    
goku = Personaje("Goku", 100,100)
vegeta= Personaje("Vegeta",200,50)
print(goku+vegeta)

