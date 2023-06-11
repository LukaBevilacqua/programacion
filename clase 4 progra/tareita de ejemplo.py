lista = []
bandera = True

for i in range(5):
    numero = int(input("ingrese un numero: "))
    lista.append(numero)

for numero in lista:
    if bandera == True or (numeraso < numero):
        bandera = False
        numeraso = numero


print("----------------------------------------------------------------")

print(lista)

print("El numero ingresado mas groso es {}".format(numeraso))

print("----------------------------------------------------------------")
