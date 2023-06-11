# Ejercicio 01
# La división de higiene está trabajando en un control de stock para productos sanitarios.
# Debemos realizar la carga de una compra de productos de prevención de contagio,
# de cada una debe obtener los siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de stock.


while True:

    tipo = input("Ingrese el tipo, barbijo, jabon o alcohol: ")
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
        tipo = input("ERROR por favor ingrese barbijo, jabon o alcohol: ")

    precio = float(input("Ingrese el precio: "))
    while precio < 0:
        precio = float(input("ERROR Ingrese un precio valido: "))

    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    while cantidad_unidades < 1:
        cantidad_unidades = int(input("ERROR Ingrese la cantidad de unidades: "))

    marca = input("Ingrese la marca: ")

    fabricante = input("Ingrese el fabricante: ")

    break

print("--------------------------------------------------------")

print("Usted compro {} unidades de {} al precio de {} de la marca {} y fabricante {}".format(cantidad_unidades, tipo, precio, marca, fabricante))