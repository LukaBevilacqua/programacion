from transporte import Transporte

class Auto(Transporte):
    def __init__(self, ruedas, marca, cantidad: int, velocidad: float):
        super().__init__(cantidad, velocidad)
        self.cantidad_ruedas = ruedas
        self.marca = marca

    def frenar(self):
        print(f"El auto: {self.marca}")
        super().frenar()
    
    def avanzar(self):
        print(f"El auto: {self.marca}")
        super().avanzar()

    def mostrar(self):
        super().mostrar()
        print(f"Ruedas: {self.cantidad_ruedas} -- Marca: {self.marca}")

    def tocar_bocina(self):
        print("TUTUUUUUUUUUUUUUUUU")