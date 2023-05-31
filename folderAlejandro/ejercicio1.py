
numeroUno = int(input("Ingresa primer numero:"))
numeroDos = int(input("Ingresa segundo numero:"))


def suma(a,b):
    return a+b

suma = suma(numeroUno, numeroDos)   

def resta(a,b):
    return a-b

resta = resta(numeroUno, numeroDos)

def multiplicacion(a,b):
    return  a*b

multiplicacion = multiplicacion(numeroUno, numeroDos)


def division(a: int,b: int):
    return a/b

division = division(numeroUno, numeroDos)

print(f"La suma de: {numeroUno} + {numeroDos} es = {suma}")
print(f"La resta de: {numeroUno} + {numeroDos} es = {resta}")
print(f"La multiplicacion de: {numeroUno} * {numeroDos} es {multiplicacion}")
print(f"La division de: {numeroUno} / {numeroDos} es = {division}")