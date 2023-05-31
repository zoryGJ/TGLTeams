# es un patron de diseño de software que se utiliza para aumentar la eficiendia y modularidad del codigo, se inyectan en el componente que las  necesita en lugar de ser creada alli.


class Servicio:
    def hacerAlgo(self):
        print('Este servicio hace algo')

class Cliente:

    def __init__(self, servicio: Servicio):
        self.servicio = servicio

    def userServicio(self):
        self.servicio.hacerAlgo()
        print('Este servicio fue usado')

servicio = Servicio()
cliente_1 = Cliente(servicio)
cliente_1.userServicio()

cliente_2 = Cliente(servicio)
cliente_2.userServicio()

