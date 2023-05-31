
import re
def extraer_numeros(cadena):
    """
    esta funcion me muestra como lista los numeros enteros que encuentre en la cadena
    """
    enteros = re.findall(r"[+\d]", cadena)
    print(enteros)

extraer_numeros('mostrar como lista los enteros: 1/2, 0.75, 3.14, 1, 2, 3, 4, 5') 