# 1.Contar letras: Crea una función que tome una cadena
# de texto como argumento y
# cuente el número de letras que contiene.

def contar_letras(cadena:str): # lo que esta adentro de los parentesis de una funcion se llama argumento
    """_summary_

    Args:
        cadena (str): _description_

    Returns:
        _type_: _description_
    """
    if type(cadena) == str:
        largo_cadena = len(cadena)
        return largo_cadena
        # print(largo_cadena)

# cadena = input("Ingrese una palabra: ")
# contar_letras(cadena)


# 2.Eliminar caracteres: Crea una función que tome una
# cadena de texto y un carácter como argumentos, y
# elimine todas las ocurrencias de ese carácter en la
# cadena.

def eliminar_caracteres(cadena:str, carácter):
    if type(cadena) == str:
        cadena_modificada = cadena.removeprefix(carácter)
        return cadena_modificada

# cadena = input("Ingrese un texto: ")
# cadena_modificada = eliminar_caracteres(cadena, "sal")
# print(cadena_modificada)


# 3.Contar palabras: Crea una función que tome una
# cadena de texto como argumento y
# cuente el número de palabras que contiene.
# Suponga que las palabras están separadas por un
# espacio.

def contar_palabras(cadena:str):
    if type(cadena) == str:
        resultado = cadena.count("")
        return resultado

# cadena = "hola puto gil"
# resultado = contar_palabras(cadena)
# print(resultado)


# 4.Reemplazar palabras: Crea una función que tome una
# cadena de texto, una palabra y otra palabra como
# argumentos, y reemplace todas las ocurrencias de la
# primera palabra por la segunda en la cadena.

def reemplazar_palabras(cadena:str,palabra_a_reemplazar,palabra_reemplazo):
    mostrar = cadena.replace(palabra_a_reemplazar,palabra_reemplazo)
    return mostrar

# cadena = "15 03 2002"
# mostrar = reemplazar_palabras(cadena, " ", "/")
# print(mostrar)


# 5.Buscar patrón: Crea una función que tome dos cadenas
# de texto como argumentos: una cadena principal y un
# patrón. La función debe encontrar todas las ocurrencias
# del patrón en la cadena principal y devolver una lista con
# las posiciones donde se encontró el patrón.

def buscar_patron(cadena:str,segunda_cadena:str):
    if type(cadena) == str and type(segunda_cadena) == str:
        resultado = cadena.count(segunda_cadena)
        return resultado

cadena = "Quiero comer milanesas"

