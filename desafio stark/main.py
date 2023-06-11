
import os
from data_stark import lista_personajes
from funciones import *

lista_heroes = []
flag_lista = False

while True:
    os.system("cls")
    print("------------------------------------------------------------")
    match(menu()):
        case "1":
            cargar_lista(lista_heroes, lista_personajes)
            flag_lista = True
        case "2":
            if flag_lista:
                nombres(lista_heroes, "nombre")
            else:
                print("Primero cargue la lista...")
        case "3":
            if flag_lista:
                nombres_con_alturas(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "4":
            if flag_lista:
                mayor_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "5":
            if flag_lista:
                menor_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "6":
            if flag_lista:
                promedio_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "7":
            if flag_lista:
                mas_pesado(lista_heroes)
                menos_pesado(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "s":
            salir = input("Confirma salida? s/n: ").lower().strip()
            if salir == "s":
                break
        case "0":
            no_se = input("Esta seguro que quiere entrar a STARK 01? s/n: ").lower().strip()
            if no_se == "s":
                input("Bienvenido a STARK 01...")
                while True:
                    os.system("cls")
                    print("------------------------------------------------------------")
                    match(menu_stark01()):
                        case "s":
                            salir = input("Confirma salida? s/n: ").lower().strip()
                            if salir == "s":
                                break
                        case "1":
                            if flag_lista:
                                print("Ya se cargaron los datos anteriormente")
                            else:
                                cargar_lista(lista_heroes, lista_personajes)
                        case "2":
                            mostrar_nombres_por_genero(lista_heroes, "genero", "M", "nombre")
                            
                        case "3":
                            mostrar_nombres_por_genero(lista_heroes, "genero","F", "nombre")
                        case "4":
                            mayor_altura_por_genero(lista_heroes, "genero", "M")
                        case "5":
                            mayor_altura_por_genero(lista_heroes, "genero", "F")
                        case "6":
                            promedio_altura_por_genero(lista_heroes, "genero", "M")
                        case "7":
                            promedio_altura_por_genero(lista_heroes, "genero", "F")
                
                    os.system("pause")
    

    input("Presione enter para continuar...")
