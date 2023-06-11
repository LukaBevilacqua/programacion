# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.

español = []
ingles = []

r = "s"

while r == "s":
    palabra_en_español = input("Ingrese una palabra en español: ")
    while not palabra_en_español.isalpha():
        palabra_en_español = input("Por favor ingrese una palabra en español: ")
    español.append(palabra_en_español)

    traduccion_al_ingles = input("Ingrese lo mismo pero en ingles: ")
    while not traduccion_al_ingles.isalpha:
        traduccion_al_ingles = input("Por favor ingrese lo mismo pero en ingles: ")
    ingles.append(traduccion_al_ingles)

    for palabra in español:
        pass

    r = input("Desea continuar? s/n: ")

print("-------------------------------------------")
print(español)
print(ingles)
print("-------------------------------------------")
