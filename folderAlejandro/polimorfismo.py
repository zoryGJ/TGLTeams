#permite utilizar metodos con elmismo nombre pero con comportamientos diferentes en diferentes clases

class Ave:

    def volar(self):
        pass # o hay nada sigua abajo


class Aguila(Ave):

    def volar(self):        
        print('puedo volar')

class Pinguino(Ave):

    def volar(self):        
        print('no puedo volar')

aguila = Aguila()

aguila.volar()

pinguino = Pinguino()

pinguino.volar()