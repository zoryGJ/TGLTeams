#suma

#TIPOS
#int para enteros
#str para cadenas de texto
#bool para datos true false
#float para decilames
#list para arreglos
#dict para dictionarios o jsons


def suma(a: int, b: float):
    return a + b

print(suma(10,20.4))

def resta(a: int, b:int):
    return a - b

print(resta(4, 50))

def multiplicacion(a: int, b:int):
    return a * b

print(multiplicacion(50, 50))

def division(a: int, b:int):
    return int(a / b)

print(division(20, 10))

def modulo(a: int, b:int):
    return a % b

print(modulo(10, 4))


def potencia(a: int, b:int):
    return a ** b

print(potencia(2, 3))

round(2.333, 2) #redondear