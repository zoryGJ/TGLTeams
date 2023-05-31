
def ejercicio():
    
    lista = [1,2,3,4,5]

    return {
    'promedio': sum(lista)/len(lista),
    'pares': [a for a in lista if a % 2 == 0],
    'impares': [a for a in lista if a % 2 != 0],
    }

print(ejercicio())