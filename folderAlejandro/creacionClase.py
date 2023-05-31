
#CLASES CREACION CLASES METODOS ATRIBUTOS
#variables y clases no pueden contener caracteres especiales, niiniciar con un numero Y COMIENXZAN EN MAYUSCULAS


class Perro:

    nombre = '' #es una buena practica tenr los atributos organizados


    def __init__(self, nombre:str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def despedir(self):
        print(f"me despido desde despedir {self.nombre}")

    def saludar(self):
        print(f"hola me llamo {self.nombre} y tengo {self.edad} años")
        self.despedir()

    def asignarColor(self, color): #siempre colocar self como primer parametro
        self.color = color

    def __str__(self):
        return 'soy un objeto perro' #cambiar el tipo de datos de str a int o viceversa se muestra lo que retorno cuando quiero cmabiar
    


perro = Perro('Juanes', 5)

print(perro)

perro.saludar()
perro.despedir()