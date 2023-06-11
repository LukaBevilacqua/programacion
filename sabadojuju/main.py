from bicicleta import Bicicleta
from auto import Auto

mi_auto = Auto(4, "Ford", 5, 170)
mi_bicicleta = Bicicleta(16, 24, 1, 50)
otro_auto = Auto(5, "Fiat", 8, 200)
otra_bicicleta = Bicicleta(8, 12, 2, 25)

lista_transporte = [mi_auto, mi_bicicleta, otro_auto, otra_bicicleta]

for t in lista_transporte:
    t.mostrar() # polimorfismos
    t.avanzar()
    t.frenar()
    if type(t) == Auto:
        t.tocar_bocina()



