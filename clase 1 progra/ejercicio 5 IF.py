## Escribir un programa que le pida al usuario que ingrese su nombre, 
## y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", 
## o "Hola desconocido" si el nombre ingresado no es uno de esos tres.

nombre = input("ingrese su nombre")

match(nombre):
    case "Juan" | "Maria" | "Pedro":
        print("hola" + nombre)
    case _:
        print("Hola desconocido")