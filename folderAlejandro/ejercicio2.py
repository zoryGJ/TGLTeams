

nombre = input('Ingresar Nombre del Estudiante: ')
edad = int(input('Ingresar Edad del Estudiante: '))


diccionario = {
    'nombre': '',
    'edad': '',
    'notas': [],
    'aprobado': '',
}

diccionario['nombre'] = nombre
diccionario['edad'] = edad

nota1 = float(input('Ingresar nota 1: '))
nota2 = float(input('Ingresar nota 2: '))
nota3 = float(input('Ingresar nota 3: '))
nota4 = float(input('Ingresar nota 4: '))
nota5 = float(input('Ingresar nota 5: '))

diccionario['notas'].append(nota1)
diccionario['notas'].append(nota2)
diccionario['notas'].append(nota3)
diccionario['notas'].append(nota4)
diccionario['notas'].append(nota5)
suma = sum(diccionario['notas'])
media = suma / 5

if media >= 3:
    diccionario.update({'aprobado': True})
else:
    diccionario.update({'aprobado': False})

print(diccionario)

