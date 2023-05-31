lista1 = [1, 2, 'texto', ['otra lista', 2, 4]]

print(lista1)
print(type(lista1))#obtenemos el tipo de datos

listaAppend = [5, 2, 34]

listaAppend.append('final')

print(listaAppend)

listaRemove = [5, 6, 7, 76]

print(listaRemove)

listaSort = [564, 4, 778, 0, 699]
listaSort.sort(reverse=True) #reverse es para ordenar en reversa si no esta reverse organiza de menor a mayor, igual ordena en order alfabetico los string SOLO CON LOS MISMOS TIPOS DE DATOS
print(listaSort)

listaReverse = ['B', 'Manuela', 'pepito', 'a']

listaReverse.reverse()

print(listaReverse)

print(listaReverse.index('B'))

lista = ['B', 'Manuela', 'pepito', 'a']

print(lista.index('B'))
print(lista.count('B'))

print(len(lista))
print(sum([5, 1, 2]))

print(lista[0:3])

print(lista[-1])
print(lista[len(lista) - 1])




