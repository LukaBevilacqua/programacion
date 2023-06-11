## Escribir un programa que le pida al usuario que ingrese un número entero, 
## y luego imprima "El número ingresado es par" si el número es divisible por 2, 
## o "El número ingresado es impar" si el número no es divisible por 2.

edad = int(input("ingrese un numero entero"))

if edad % 2 == 0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")