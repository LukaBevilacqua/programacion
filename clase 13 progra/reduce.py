from functools import reduce

def miFuncion(anterior, actual):
    return anterior + actual

def obtenerMayor(a, b):
    mayor = a
    if b > a:
        mayor = b
    return mayor

numeros = [4,5,12,8,7,9]

total = 0
for numero in numeros:
    total+= numero


# total = reduce(miFuncion, numeros)
# total = reduce(lambda ant, act: ant + act, numeros, 0)
# mayor = reduce(obtenerMayor, numeros)
mayor = reduce(lambda ant, act: ant if ant > act else act, numeros)

# print(total)
print(mayor)
