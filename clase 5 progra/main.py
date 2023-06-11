import sarasa.data as data # se usa para tomar datos de otros lugares, en este caso el archivo "data.py"
from sarasa.data import personas, numero # se usa para tomar de un archivo solo una variable en este caso "personas", "*" se usa para tomar todas las variables

print(data.personas)
print(data.numero) 

print("--------------------------------------")

print(personas)
print(numero)