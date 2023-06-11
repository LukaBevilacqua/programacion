# Ejercicio con Menú de Opciones
# Realizar un programa utilizando los conceptos de la clase:
# Opciones del menú:
# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
# (terrestre, anfibio, volador).
# 2 Imprimir la lista completa de animales con su tipo.
# 3 Mostrar el porcentaje de animales por tipo.
# 4 Mayor cantidad de animales por tipo.
# 5 Menor cantidad de animales por tipo.
# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
# efectivamente está en la lista.
# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
# 8 Informar la cantidad de animales por cada tipo de animal.
# 9 Vaciar la lista.
#10 Salir.

import os

while True:
    os.system("cls")
    print("""
                        Ejercicio con Menú de Opciones
            Realizar un programa utilizando los conceptos de la clase:
            Opciones del menú:
            1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
            (terrestre, anfibio, volador).
            2 Imprimir la lista completa de animales con su tipo.
            3 Mostrar el porcentaje de animales por tipo.
            4 Mayor cantidad de animales por tipo.
            5 Menor cantidad de animales por tipo.
            6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
            efectivamente está en la lista.
            7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
            8 Informar la cantidad de animales por cada tipo de animal.
            9 Vaciar la lista.
            10 Salir.
    """)
    opcion = input("Ingrese una opcion: ")
    print("---------------------------------------------------------------------------------------------------------------------")

    if opcion == "1":
        pass
    elif opcion == "10":
        salir = input("Confirma salida? s/n: ")
        if salir == "s":
            break

    input("Presione enter para continuar...")