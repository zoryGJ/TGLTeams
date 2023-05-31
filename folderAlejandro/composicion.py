# es un concepto de diseño orientado a obhetos donde una clase puede contener objetos de otras clases. se utiliza para representar relaciones de "tiene-un" entre objetos

class Motor:

    def cilindraje(self):
        print('2000 cc')

class Llantas:

    def cuantas(self):
        print('4 llantas')

class Auto:
    def __init__(self):
        self.motor = Motor()
        self.llantas = Llantas()

auto = Auto()

auto.motor.cilindraje() #Motor y Llantas dependen de que exista un vehiculo




