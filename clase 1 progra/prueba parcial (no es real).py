# Bienvenidos.
# En el ingreso a un viaje en avión nos solicitan nombre, nacionalidad ,
# edad, sexo("f" o "m") y estado civil("soltero", "casado" o "viudo")y temperatura corporal.
# a) la Nacionalidad de la persona con mas temperatura.
# b) Cuantos mayores de edad( más de 17) estan solteros
# c) La cantidad de Mujeres que hay solteras o viudas.
# d) cuantas personas de la tercera edad( mas de 60 años) , tienen mas de 38 de temperatura
# e) El promedio de edad entre las mujeres casadas.

pregunta = "si"

while pregunta == "si":
    nombre_ingresado = input("Ingrese su nombre")
    nacionalidad_ingresada = input("Ingrese su nacionalidad")
    edad_ingresada = int(input("Ingrese su edad"))
    sexo_ingresado = input("ingrese su sexo siendo f para femenino y m para masculino")
    estado_civil_ingresado =  input("Ingrese su estado civil, soltero casado o viudo")