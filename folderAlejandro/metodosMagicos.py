#son metodos especiales con doble guon bajo antes y despues del nombre. Estos proporcionan la capacidad de cambiar el comportamiento predeterminado de las clases en python


class PruebasMetodosMagicos:

    def __init__(self):
        print('Soy el constructor, puedo inicializar variables')

        self.magico = True

    def __str__(self):

        return f"soy un metodo magico {self.magico}"

prueba = PruebasMetodosMagicos()

print(str(prueba))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"Vector{self.x, self.y}"

v1 = Vector(2, 3)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)

class Caja:
    def __init__(self, elementos):

        self.elementos = elementos
    
    def __len__(self):
        return len(self. elementos)

mi_caja = Caja(['Manzana', 'banano', 'pera'])

print(len(mi_caja))

class Caja:
    def __init__(self, elementos):

        self.elementos = elementos
    
    def __getitem__(self, indice):
        return self.elementos[indice]

mi_caja = Caja(['Manzana', 'banano', 'pera'])

print(mi_caja[1])


