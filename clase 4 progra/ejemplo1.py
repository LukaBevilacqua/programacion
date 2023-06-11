

lista = []


for i in range(5):
    numero = int(input("ingrese un numero: "))
    lista.append(numero)

acumulador = 0

for numero in lista:
    acumulador += numero

promedio = acumulador/len(lista)

print("----------------------------------------------------")

print("La suma de los numeros ingresados es {}".format(acumulador))

print("El promedio de los numeros ingresados es {}".format(promedio))

print("----------------------------------------------------")

# SON LO MISMO PERO HECHO DE DISTINTAS MANERAS
# for i in range(len(lista)):
    # print(lista[i])
# for numero in lista:
#     print(numero)



# print("La suma de los numeros ingresados es {}".format(acumulador))



# ESTE ES UN METODO PERO NO ES EL MEJOR
# acumulador = 0


# for i in range(5):
#     numero = int(input("ingrese un numero: "))
#     acumulador += numero


# print("La suma de los numeros ingresados es {}".format(acumulador))