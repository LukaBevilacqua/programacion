
import os

flag_saludo = False
flag_brindis = False

while True:
    os.system("cls")
    print("*** Menu de Opciones ***")
    print("------------------------")
    print("1- Saludar")
    print("2- brindar")
    print("3- despedir")
    print("4- salir")
    opcion = input("Ingrese opcion: ")

    print("------------------------")

    if opcion == "1":
        print("Hola")
        flag_saludo = True

    elif opcion == "2":
        if flag_saludo:
            print("Chin chin..")
            flag_brindis = True
        else:
            print("Antes de brindar primero saludame")

    elif opcion == "3":
        if flag_brindis:
            print("chau")
            flag_saludo = False
            flag_brindis= False
        elif flag_saludo:
            print("Antes de despedirnos brindemos")
        else:
            print("Antes de despedirnos primero saludame")

    elif opcion == "4":
        salir = input("Confirma salida? s/n: ")
        if salir == "s":
            break

    # ambos hacen que quede a la espera el programa como para poner una pausa por ej
    input("Presione enter para continuar...")
    # os.system("pause")