# Ejercicio 04
# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes para preparar comida al por mayor.
# En total, sabemos que se realizarán 15 compras de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de descuento sobre el precio bruto, 
# o si compro más de 300 kilos en total, tengo un 25% de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.

compras = 0
importe_bruto = 0

for compras in range(1,16):

    peso = int(input("Ingrese el peso, entre 10 y 100 kilos: "))
    while peso < 10 or peso > 100:
        peso = int(input("ERROR. Ingrese el peso, entre 10 y 100 kilos: "))
    
    precio_por_kilo = int(input("Ingrese el precio por kilo: "))
    while precio_por_kilo < 1:
        precio_por_kilo = int(input("ERROR. Ingrese el precio por kilo: "))

    tipo_variedad = input("Ingrese el tipo, vegetal, animal o mezcla: ")
    while tipo_variedad != "vegetal" and tipo_variedad != "animal" and tipo_variedad != "mezcla":
        tipo_variedad = input("ERROR. Ingrese el tipo, vegetal, animal o mezcla: ")
    
    precio = precio_por_kilo*peso
    importe_bruto += precio

if peso > 300:
    descuento = 0.75
else:
    if peso > 100:
        descuento = 0.85
    else:
        descuento = 1

importe_con_descuento = (importe_bruto*(descuento))

print("----------------------------------------------------------")

print("A. El importe bruto es {}".format(importe_bruto))

if peso > 100:
    print("B. El importe con descuento es {}".format(importe_con_descuento))

print("----------------------------------------------------------")