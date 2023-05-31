def funcionDesdeCase():
    print('entre a funcion desde case')


def funcionMatch(code):
    match code:
        case 300: 
            print('entre a 300')
        case 200:
            print('entre a 200')
        case 400:
            funcionDesdeCase()
        case _:
            print('Cse x defecto')


def funcionDiccionario(code):
    diccionario = {
        300: print('entre a 300'),
        200: print('entre a 200'),
        400: funcionDesdeCase()
    }


    match code:
        case 300: 
            print('entre a 300')
        case 200:
            print('entre a 200')
        case 400:
            funcionDesdeCase()
        case _:
            print('Case x defecto')

funcionMatch(400)