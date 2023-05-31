def rangeUnico():
    for i in range(4):
        print(i)


def rangeMultiple():
    for i in range(2,10):
        print(i)

def rangeSteps():
    for i in range(2,10,2):
        print(i)

#formas de contar los valores

def iterarLista():
    lista = ['valor 1', 'valor 2', 'valor 3']
    for valor in lista:
        print(valor)
    
    for indice, valor in enumerate(lista):
        print(f"{indice} {valor}")


def iterarListaRange():
    lista = ['valor 1', 'valor 2', 'valor 3']
    for indice in range(len(lista)):
        print(lista[indice])


def iterarDiccionario():
    diccionario = {'nombre': 'Pepe', 'Apellido': 'perez', 'edad': 5}
    
    for clave in diccionario:
        print(clave)

    for clave in diccionario.key():
        print(clave)

    for valor in diccionario.values():
        print(valor)

    for clave, valor in diccionario.items():
        print(f"{clave} {valor}")



def whileGenerico():
    numero = 1
    while numero < 5:
        print(numero)
        numero += 1

def do_while():

    numero = 1
    while True:
        if numero == 5:
            break
        print(numero)
        numero += 1
    print('finalicé')

def continueList():

    lista = ['valor 1', 'valor 2', 'valor 3']

    for valor in lista:
        if valor == 'valor 2':
            continue
        print(valor)

continueList()


# for i in range(4):
#     print(i)


# for i in range(2,10):
#     print(i)


# for i in range(2, 10, 2):
#     print(i)