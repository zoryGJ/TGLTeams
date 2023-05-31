

def listaComprension():
    listaCuadrado = [a**2 for a in range(5)]
    print(listaCuadrado)
    lista = []
    for a in range(5):
        lista.append(a**2)
    print(lista)

#listaComprension()

def ifListaCompresion():
    lista_pares = [a for a in range(6) if a%2 == 0]
    print(lista_pares)

#print(ifListaCompresion())

def dicCompresion():
    dict_alcuadrado = {a: a**2 for a in range(5)}
    print(dict_alcuadrado)

def if_dicCompresion():
    dict_alcuadrado = {a: a**2 for a in range(5) if a == 2}
    print(dict_alcuadrado)

dicCompresion()