# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. 
# Luego, muestra la suma de todos los números ingresados.

lista = [0]

acumulador = 0

for i in lista:
    numero = int(input("Ingrese un numero entero: "))
    if numero < 0:
        break
    lista.append(numero)

for numero in lista:
    acumulador += numero

print("La suma de todos los numeros ingresados: {} ".format(acumulador))
