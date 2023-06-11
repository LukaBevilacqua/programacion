## Escribir un programa que le pida al usuario que ingrese dos números enteros, 
## y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, 
## "El segundo número es mayor" si el segundo número es mayor que el primero, 
## o "Los dos números son iguales" si los dos números son iguales.

primer_numero = int(input("Ingrese el primer numero"))
segundo_numero = int(input("Ingrese el segundo numero"))

if primer_numero > segundo_numero:
    print("El primer número es mayor")
else:
    if segundo_numero > primer_numero:
        print("El segundo número es mayor")
    else:
        print("Los dos números son iguales")