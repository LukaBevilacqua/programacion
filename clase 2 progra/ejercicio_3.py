# Ejercicio 03
# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.
# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género femenino
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
# C. Nombre del votante más joven que votó a Nacho.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos).


votantes_femeninos = 0
edad_feminas = 0
cant_masculino = 0
bandera_votante_joven = True
edad_mas_joven = 0
voto_julieta = 0
voto_nacho = 0
voto_marcos = 0
cantidad_votantes = 0 
respuesta = "si"

while respuesta == "si":
    nombre_votante = input("Ingrese su nombre: ")
    while not nombre_votante.isalpha():
        nombre_votante = input("ERROR. Ingrese su nombre: ")
    
    edad_votante = int(input("Ingrese su edad, debe ser mayor de 13 años: "))
    while edad_votante < 14:
        edad_votante = int(input("ERROR. Ingrese su edad, debe ser mayor de 13 años: "))
    
    genero_votante = input("Ingrese su genero, femenino, masculino u otro: ")
    while genero_votante != "femenino" and genero_votante != "masculino" and genero_votante != "otro":
        genero_votante = input("ERROR. Ingrese su genero, femenino, masculino u otro: ")
    
    voto = input("Ingrese a quien quiere votar: ")
    while voto != "nacho" and voto != "julieta" and voto != "marcos":
        voto = input("ERROR. Ingrese a quien quiere votar: ")
    
    if genero_votante == "femenino":
        votantes_femeninos+=1
        edad_feminas = edad_feminas + edad_votante
    
    match(voto):
        case "julieta":
            voto_julieta += 1
            if genero_votante == "masculino" and (edad_votante > 24 or edad_votante < 41):
                cant_masculino+=1

        case "nacho":
            voto_nacho += 1

            if bandera_votante_joven == True or (edad_mas_joven > edad_votante):
                edad_mas_joven = edad_votante
                nombre_votante_mas_joven = nombre_votante
                bandera_votante_joven = False

            if genero_votante == "masculino" and (edad_votante > 24 or edad_votante < 41):
                cant_masculino+=1

        case "marcos":
            voto_marcos += 1
    
    cantidad_votantes += 1
    
    respuesta = input("[si] para volver a votar, [no] para salir: ")

promedio_edad_feminas = edad_feminas / votantes_femeninos

promedio_votos_julieta = (voto_julieta/cantidad_votantes)*100
promedio_votos_nacho = (voto_nacho/cantidad_votantes)*100
promedio_votos_marcos = (voto_marcos/cantidad_votantes)*100

if voto_julieta > voto_marcos and voto_julieta > voto_nacho:
    
    mensajeE = "JULIETAAAAAAAAAAAAAAAAAAAAAAAA"
    
else:
    if voto_marcos>voto_nacho:
        
        mensajeE = "MARCOOOOOOOOOOOOOOOOOOOOSSS"

    else:
        mensajeE = "NACHOOOOOOOOOOOOOOOOOOOOOOOOO"
        
    

print("---------------------------------------------------------------------------------------------")

if votantes_femeninos != 0:
    print("A. El promedio de edad de las votantes femeninas es de: {}".format(promedio_edad_feminas))

if cant_masculino != 0:
    print("B. La cantidad de hombres de entre 25 y 40 años que votaron a julieta o nacho es de: {}".format(cant_masculino))

if edad_mas_joven != 0:
    print("C. La persona mas joven que voto a nacho es {}".format(nombre_votante_mas_joven))

print("D. El promedio de votos de julieta fue de {}%, el promedio de votos de marcos fue de {}% y el promedio de votos de nacho fue de {}%".format(promedio_votos_julieta, promedio_votos_marcos, promedio_votos_nacho))

print("E. El ganador del programa es......................................... {}".format(mensajeE))

print("---------------------------------------------------------------------------------------------")