a = 2
print(a)
SOY_GLOBAL = "SOY GLOBAL"
b, c, d =  2, 3.233, "string"

print(b)
print(c)
print(d)

def retornar():
   
    return "Soy funcion: Retorne un valor"

def variablesGobal():
    global SOY_GLOBAL
    local = "soy local"
    SOY_GLOBAL = "soy Global CAMBIO DE VALOR"



retornando = retornar()
print(retornando)
print(SOY_GLOBAL)



#comentarios