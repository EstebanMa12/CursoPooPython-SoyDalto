def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a ala función ")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada


# def saludo():
#     print("Hola mundo desde la función decorador")


# saludo_modificado=decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola mundo desde la función decorador")

""" saludo()
 """


# EJEMPLO CON UNA FUNCIÓN MÁS COMPLEJA-------------

def temperatura_valida(funcion):
    def validation(temperatura):
        if 25 <= temperatura <=100:
            result = funcion(temperatura)
            return result
        else:
            print("Error: Ingrese una temperatura correcta")
    return validation

@temperatura_valida
def otra_funcion(temperatura):
    print(f"Otra función con {temperatura}°C. en este caso la temperatura es correcta")


while True:
    try:
        temperatur= float(input("Ingrese la temperatura en °C: "))
        otra_funcion(temperatur)
    except ValueError:
        break