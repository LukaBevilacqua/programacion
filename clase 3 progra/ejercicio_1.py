# Crea una lista con los números del 1 al 10 e imprime solo los números impares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    if not i % 2 == 0:
        print(i)