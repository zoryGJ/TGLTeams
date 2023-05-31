def primeros_args(*args):
    print(args[0])

    operacion = args[0] + sum(args[2])
    print(operacion)
    #for value in args:
    #   print(value)

#primeros_args(2, 'hola', [1,2,3], 'adios')
# el * es para q salga sin los [] en la consola

lista_args = ['lista', 'Argumentos', 'prueba']

primeros_args(*lista_args)

