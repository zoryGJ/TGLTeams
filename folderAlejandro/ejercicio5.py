class Auto:

    def __init__(self, marca: str, modelo: str, año: int, velocidad: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        print(f"la velocidad aumento {self.velocidad}")

    def frenar(self):
        self.velocidad = 0
        print(f"la velicidad se detuvo a: {self.velocidad}")

class AutoElectrico(Auto):

    def __init__(self, marca, modelo, año, velocidad, autonomia, porcentajeBateria):
        Auto.__init__(self, marca, modelo, año, velocidad)
        self.autonomia = autonomia
        self.porcentajeBateria = porcentajeBateria

    def cargarBateria(self):

        while self.porcentajeBateria < 100:
            print(f"carga bateria aumento {self.porcentajeBateria} %")
            self.porcentajeBateria += 10
        else:
            print(f"carga finalizada en {self.porcentajeBateria} %")

auto = AutoElectrico('toyota', 'prado', 2022, 40, True, 60)

print(auto)
print(auto.porcentajeBateria)
auto.acelerar()
auto.frenar()
auto.cargarBateria()
