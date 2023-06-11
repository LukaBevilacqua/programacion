from functools import *
series = [
    {"nombre": "Dragon BallZ", "año": 1989},
    {"nombre": "Sailor Moon", "año": 1992},
    {"nombre": "Pokemon", "año": 1997},
    {"nombre": "Digimon Adventure", "año": 1999},
    {"nombre": "Yu Yu Hakusho", "año": 1992},
    {"nombre": "Neon Genesis Evangelion", "año": 1995},
    {"nombre": "One Piece", "año": 1999},
    {"nombre": "Rurouni Kenshin", "año": 1996}
]

# 1.      Obtener una lista con los nombres de
# todas las series de anime.

print("Punto 1:")

nombres_series = []
for anime in series:
    nombre = anime.get("nombre")
    nombres_series.append(nombre)
print(nombres_series)

# 2.      Obtener las series de anime lanzadas
# después de 1995.

print("Punto 2:")

print(list(filter(lambda anime: anime["año"]>1995, series)))

# 3.      Obtener la suma de los años de
# lanzamiento de las series.

print("punto 3:")

print(reduce(lambda anime, animeSig: anime + animeSig["año"], series, 0))

# 4.      Realizar una copia superficial de la
# lista de series.


# 5.      Realizar una copia profunda de la
# lista de series.


# 6.      Obtener el año de lanzamiento de una
# serie utilizando una función de diccionario.


# 7.      Obtener una lista de tuplas con los
# pares clave-valor de una serie utilizando una función de diccionario.


# 8.      Eliminar una serie de la lista por su
# índice utilizando una función de lista.


# 9.      Obtener una lista con los nombres de
# las series en mayúsculas utilizando una función de transformación.


# 10.   Obtener las series de anime con
# nombres que contengan la palabra "Adventure" utilizando una función
# de filtrado.


# 11.   Generar una función que busque los
# nombres de las series con el rating mayor a 8.5
