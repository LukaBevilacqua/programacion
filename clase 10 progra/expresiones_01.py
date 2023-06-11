# EXPRESIONES REGULARES

import re # se importa re para poder usar las expresiones regulares

"""
- preguntar si un texto coincide con un patron


"""

patron_email = re.compile("[a-z0-9_]+@(hotmail.com|gmail.com)")

frase = "Esto es un 102 texto de prueba para 7practicar expresiones 94 regulares en textos y no hay pretexto"


# match = patron_email.match("juanperez89@gmail.com")

# if(match):
#     print("patente valida", match.group())
# else:
#     print("No hubo coincidencias")

# print(re.findall("\d+", frase))





# patron_patente_vieja = re.compile("[A-Z]{3} [0-9]{3}")
# patron = re.compile("\d") # \d es una expresion que toma todos los digitos por separado

# match = patron.match(texto)
# match = patron_patente_vieja.match("ABC 123")
# if(match):
#     print("patente valida", match.group())
# else:
#     print("No hubo coincidencias")

# lista = patron.findall(frase)

# lista = re.findall("\d", frase)

# print(lista)







frase2 = """esta es la primer linea
esta es la segunda linea
esta es la tercer linea
esta es la cuarta linea
"""

print(re.findall("esta", frase2))