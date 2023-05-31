

def funcionMixta(*args, **kwargs):
    print(args) #salen en ()
    print(kwargs) #salen en {}


funcionMixta(1,2,3, nombre='pepe', edad='perez')

lista = [1,2,3]

funcionMixta(*lista)

funcionMixta('pepe', 'perez', *lista)