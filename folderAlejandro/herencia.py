#POO  1 HERENCIA

class Animal:

    def __init__(self, color):
        self.color = color

    def colorAnimal(self):
        print(f"soy de color {self.color}")

class Perro:

    ladra = True

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"hola me llamo {self.nombre} y tengo {self.edad} años")


class PerroGuia(Perro, Animal):

    def __init__(self, nombre, raza, edad, entrenado):
        Perro.__init__(self, nombre, edad)
        Animal.__init__(self, 'rojo')
        self.raza = raza
        self.entrenado = entrenado

    def validarEntrenado(self):
        if self.entrenado:
            print('Estoy entrenado')
        else:
            print('No estoy entrenado')

    def perroLadra(self):
        print(f"el perro lada {self.ladra}")


perro = PerroGuia('Juan', 'Rottweiler', '2 años', True)

perro.saludar()
perro.validarEntrenado()
perro.colorAnimal()
perro.perroLadra()