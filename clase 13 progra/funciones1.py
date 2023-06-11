# funcion objeto de primera clase.
# - cuando puede asignarse a una variable
# - cuando puede pasarse como parametro a una funcion
# - cuando puede ser retornado por una funcion

def saludar():
    print("Hola mundo")

def despedir():
    print("Chau mundo")

def ejecutora(queEjecuto):
    queEjecuto()


# saludar()
# print(type(saludar))

ejecutora(saludar)
ejecutora(despedir)