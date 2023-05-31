# ocultamiento de datos internos de un objeto. en python se logra con metodos y atributos privados prejitos "__"

class Perro:

    ladra = True
    _protegido = True

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"hola me llamo {self.nombre} y tengo {self.edad} años")

    def __privado(self):
        print('soy privado')
    
    def acceso_protegido_padre(self):
        print(f"Puedo acceder a protegido {self._protegido}")


class PerroGuia(Perro):

    __patas = 4

    def __init__(self, nombre, raza, edad, entrenado):
        Perro.__init__(self, nombre, edad)
        self.raza = raza
        self.entrenado = entrenado

    def validarEntrenado(self):
        if self.entrenado:
            print('Estoy entrenado')
        else:
            print('No estoy entrenado')

    def perroLadra(self):
        print(f"el perro lada {self.ladra}")

    #para definir un atributo o metodo privado se coloca dos guinoes bajos al inicio y el nombre __pepe

    def llamar_a_privado(self):
        self.__privado()

    def cuantas_patas(self):
        print(f"tengo {self.__patas} patas")



perro = PerroGuia('Juan', 'Rottweiler', '2 años', True)

perro.cuantas_patas()
perro.acceso_protegido_padre()


print(perro.raza)
print(perro._protegido) #No arroja error, pero no lo deberiamos usar, ya que esta protegido
# se puede usar desde las clases que se hereden al padre, pero no lo usamos desde el objeto

