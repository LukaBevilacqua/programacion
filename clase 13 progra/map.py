numeros = [4,5,2,8,7,9]


# duplicados = []
# for item in numeros:
#     duplicados.append(item * 2)

duplicados = list(map(lambda value: value * 2, numeros))

print(numeros)
print(duplicados)

def contarCaracteres(cadena):
    return len(cadena)

print("----------------------------------------------------")

nombres = ["Juan", "Pedro", "Sebastian", "Carolina", "Mariana"]

largo_nombres = list(map(contarCaracteres, nombres))
largo_nombres2 = list(map(lambda nombre: len(nombre), nombres))

print(largo_nombres)
print(largo_nombres2)