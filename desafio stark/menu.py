
import os
from data_stark import lista_personajes
from funciones import *

lista_heroes = []

while True:
    os.system("cls")
    # print("  *** Menu de Opciones ***  ")
    # print("------------------------------------------------------------")
    # print("  1- Mostrar nombres")
    # print("  2- Mostrar nombres y alturas")
    # print("  3- Mostrar el superheroe mas alto")
    # print("  4- Mostrar el superheroe mas bajo")
    # print("  5- Mostrar la altura promedio")
    # print("  6- Mostrar el superheroe mas y menos pesado")
    # print("  0- STARK 01")
    # print("  s- salir")
    # opcion = input("Ingrese opcion: ")
    menu()

    print("------------------------------------------------------------")

    match(menu()):
        case "1":
            for heroe in lista_personajes:
                lista_heroes.append(heroe)
            print(lista_heroes)
        case "2":
            nombres()
        case "3":
            nombres_con_alturas()
        case "4":
            mayor_altura()
        case "5":
            menor_altura()
        case "6":
            promedio_altura()
        case "7":
            mas_pesado()
            menos_pesado()
        case "s":
            salir = input("Confirma salida? s/n: ").lower()
            if salir == "s":
                break
        case "0":
            no_se = input("Esta seguro que quiere entrar a STARK 01? s/n: ").lower()
    

    input("Presione enter para continuar...")