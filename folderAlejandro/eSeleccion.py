numero = 5
numero2 = 6

texto = 'ASAP' #se toma por defecto vacio por lo q seraia false

zero = 0 # se toma por defecto como vacio, seria false

none_es = None # se toma por defecto como vacio, seria false

lista = [[]] # se toma por defecto como vacio, seria false

listaEngañosa = [[]] #se toma como si tuviera informacion por lo cual seria True

if not texto:
    print('El texto es un string vacio, error')

if lista:
    print('Entre texto')

if numero >= 5 and numero2 <= 6:
    print('ENTRE')

if numero >= 5 and numero2 <= 6:
    print('ENTRE')
elif numero == 4:
    print('numero 4')
else:
    print('entre en else')