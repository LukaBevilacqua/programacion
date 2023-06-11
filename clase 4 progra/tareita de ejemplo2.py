
# ESTE ES MI METODO NO ESTA DEL TODO MAL PERO PODRIA SER MEJOR, es la solucion mas corta, mas directa:
lista = [23, 21, 45, 33, 78]

# for i in range(5):
#     numero = int(input("ingrese un numero: "))
#     lista.append(numero)

numero_buscado = int(input("Ingrese numero a busacar: "))

if numero_buscado in lista:
    print("{} esta en la lista".format(numero_buscado))
else:
    print("{} no esta en la lista".format(numero_buscado))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

# METODO BAUS:
lista = [23, 21, 45, 33, 78]

numero_buscado = int(input("Ingrese numero a busacar: "))

flag_esta = False

for numero in lista:
    if(numero == numero_buscado):
        flag_esta = True
        break


if flag_esta: #no hace falta poner == True porque al ser un buliano es true o false es redundante preguntar
    print("El numero esta en la lista")
else:
    print("El numero no esta en la lista")