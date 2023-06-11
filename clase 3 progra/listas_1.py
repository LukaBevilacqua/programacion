# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.

pregunta = "si"
marcas = []
modelos = []
precios = []

concesionaria = []

while pregunta == "si":
    d = {}
    marca = input("Ingrese la marca del auto: ")
    while not marca.isalpha():
        marca = input("ERROR. Ingrese la marca del auto: ")
    marcas.append(marca)
    d["marcas"] = marca
    
    modelo = input("Ingrese el modelo del auto: ")
    while not modelo.isalnum():
        modelo = input("ERROR. Ingrese el modelo del auto: ")
    modelos.append(modelo)
    d["modelos"] = modelo
    
    precio = input("Ingrese el precio del auto: ")
    while not precio.isdigit():
        precio = input("ERROR. Ingrese el precio del auto: ")
    precios.append(precio)
    d["precios"] = precio

    concesionaria.append(d)

    pregunta = input("Desea agregar un auto mas?: ")

print("----------------------------------------------------")

print("*** Concesionaria de autos ***")
print(" Marcas     Modelos      Precios")

for a in concesionaria:
    print(f"   {a['marcas']}      {a['modelos']}         {a['precios']}")

print("----------------------------------------------------")