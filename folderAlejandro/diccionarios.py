diccionario = {
    'nombre': 'Zoraida',
    'edad': '30',
    'trabajo': 'desarrolador',
    'mascotas': ['Gea', 'MI corazon'],
}

print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

print(diccionario['nombre'])#no seguro
print(diccionario.get('apellido', 'no tiene apellido')) # me trae un valor si no esta no da error si no none

diccionario['mascotas'].append('Mascotas3') #agrega el valor solo agrega a arreglos
print(diccionario)
print(diccionario['mascotas'][0])


diccionario.update({'nombre': 'Zoraida Garcia'})
diccionario.update({'apellido': 'Julio'})

diccionario['array'] = diccionario.keys()

print(diccionario)