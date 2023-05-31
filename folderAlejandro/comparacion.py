#f-string

def igualdad(a,b):
    print(a == b)

igualdad(2, 3)
igualdad(2, 2)

def desigualdad(a, b):
    print("Desigualdad: " + str(a != b))

desigualdad(2, 3)
desigualdad(2, "string")

def mayor_que(a, b):
    print("mayor que:", a > b)

mayor_que(2, 3)
mayor_que(3, 2)

def menor_que(a, b):
    print(f"{a} Menor que {b} {a < b}")

menor_que(2, 3)
menor_que(3, 2)


def mayor_igual(a,b):
    print(f"{a} es mayor o igual que {b} {a >= b}")

mayor_igual(2, 2)

def menor_igual(a,b):
    print(f"{a} es menor o igual que {b} {a <= b}")

menor_igual(2, 2)