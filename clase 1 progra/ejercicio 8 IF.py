# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto, 
# o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

numero = int(input("Ingrese un numero entero positivo"))

raiz = numero ** 0.5

if raiz.is_integrer():
    print("El numero es un cuadrado perfecto")
else:
    print("El numero no es un cuadrado perfecto")
