

def funcionParametro():
    print('soy la funcion parametro')

def primeros_kwargs(primerParametro,**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} {value}")
        if callable(value):
            value()
    print(primerParametro)



diccionario = {'hola': 'persona', 'edad': 23, 'funcion': funcionParametro}

primeros_kwargs(primerParametro='primero', **diccionario)