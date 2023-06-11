# Crea una lista con 5 números enteros. 
# Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. 
# Finalmente imprime todos los números

lista = [1, 2, 3, 4, 5]

nuevo_numero = int(input("Ingrese un numero entero: "))

lista[2] = nuevo_numero

print(lista)
