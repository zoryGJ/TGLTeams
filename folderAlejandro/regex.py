
#IMPORTANTE IMPORTAR re PARAPODER  UTILIZARLO.
#estas cosas son para buscar
import re

def re_match_search(cadena:str):
    if re.match('gato', cadena):
        print('se encontro gato en match')

    if re.search('ato', cadena):
        print('se encontro ato en search')

re_match_search('el gato se encuentra en el techo')

def re_findall(cadena):
    lista_emails = re.findall("\S+@\S+", cadena)
    print(lista_emails)

re_findall('Zoraida-zoryisa9303@gmail.com, velez@m.com, Hola')

#este me cambia palabras solo para texto
def re_sub(cadena):
    nueva_cadena = re.sub('gatos', 'perros', cadena)
    print(nueva_cadena)


re_sub('los gatos brincan en el techo siguiendo gatos')

#para encontrar numeros en cadena

def buscar_numeros(cadena):
    numeros = re.findall(r"[-+?\d+]", cadena)
    print(numeros)

buscar_numeros('cadena 10 numeros debe encontrar 1 vez -1')


def buscar_email(cadena):
    correos = re.findall(r"\b[A-ZA-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", cadena)
    print(correos)

buscar_email('por favor, contactar a ana@example.com o a juan@example.com para mas informacion')

