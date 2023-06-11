numeros = [4,5,2,8,7,9]

def esPar(valor):
    return not valor % 2

pares = list(filter(esPar, numeros))
pares2 = list(filter(lambda valor: not (valor % 2 == 0), numeros))

pares3 = []
for item in numeros:
    if item % 2 == 0:
        pares.append(item)

# print(esPar(47))
print(pares)
print(pares2)
print(pares3)








