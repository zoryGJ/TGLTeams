import random 
from enum import Enum


class Dificultad(Enum):
    FACIL = 1    
    MEDIO = 2    
    DIFICIL = 3
    
class GuestYourNumber:
    def __init__(self, dificultad: Dificultad) -> None:
        self.dificultad = dificultad        
        
        if self.dificultad == Dificultad.FACIL:
            self.number = random.randint(1, 10)

        if self.dificultad == Dificultad.MEDIO:
            self.number = random.randint(1, 20)

        if self.dificultad == Dificultad.DIFICIL:
            self.number = random.randint(1, 30)

    def run(self):
        number = random.randint(1, 10)
        trials = 0        
        # flag variable  
              
        win = False    

        while not win:
            guess = int(input("Please enter your guess: "))
            trials += 1            
            
            if guess == number:
                win = True            
            elif guess < number:
                print("Too low")
            else:
                print("Too high")

        with open('scores.txt', 'hola') as file:
            file.write(f'score: {trials}')

        print(f"You win with {trials} trials")

def main():
    nivel = input('porfa ingresa el nivel de dificultad que quieres: facil, medio, dificil:')

    if nivel == 'facil':
        print('Elegiste facil')
        game = GuestYourNumber(Dificultad.FACIL)
        game.run()

    if nivel == 'medio':
        print('Elegiste medio')
        game = GuestYourNumber(Dificultad.MEDIO)
        game.run()

    if nivel == 'dificil':
        print('Elegiste dificil')
        game = GuestYourNumber(Dificultad.DIFICIL)
        game.run()

if __name__ == '__main__':
    main()


#tarea: 
# 1. agregar informacion del usuario: nombre
# 2. al guardar los puntajes, se guarde con elnombre de usuario
# 3. al iniciar el juego mostrar un menu con 3 opciones
        # jugar -> al usuario elegir este, preguntar x nivel de dificultad
        # mostrar puntajes
        # creditos -> tu nombre, casa software
        #salir
