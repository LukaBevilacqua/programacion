# Ejercicio 02
# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de python, 
# entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error, regla de estilo inexistente”

reglas_estilo = {
    1: "Utiliza espacios en lugar de tabulaciones para indentar.",
    2: "Utiliza cuatro espacios para indentar.",
    3: "Limita la cantidad de caracteres por línea a 79.",
    4: "Separa las funciones y clases con dos líneas en blanco.",
    5: "Utiliza comentarios para explicar el código y no para describir lo que hace.",
    6: "Utiliza nombres descriptivos para las variables, funciones y clases.",
    7: "Utiliza mayúsculas para las constantes.",
    8: "Utiliza espacios alrededor de los operadores y después de las comas."
}

numero = int(input("Ingresa un numero entre 1 y 8: "))


if numero in range(1, 9):
    print(f"Regla de estilo #{numero}: {reglas_estilo[numero]}")
else:
    print("Error, regla de estilo inexistente")


