# caracteristicas
    # cantidad de pasajeros 
    # velocidad
    # km_totales
    # distancia_recorrida

# comportamiento (metodos)

class Transporte:
    def __init__(self, cantidad: int, velocidad: float):
        self.cantidad_pasajeros = cantidad # publico
        self.velocidad = velocidad # privado 
        self.km_totales = 0 # protegido
        self.distancia_recorrida = 0

    def avanzar(self):
        print("esta avanzando...")

    def frenar(self):
        print("esta frenando...")

    def mostrar(self):
        print(f"*********************{type(self)}****************************")
        print(f"cantidad: {self.cantidad_pasajeros} - Velocidad: {self.velocidad} - Destino: {self.km_totales}")