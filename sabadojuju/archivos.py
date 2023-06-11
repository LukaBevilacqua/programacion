# import csv
import json

# un archivo csv es un archivo de texto que se separa por comas
# csv -> coma separated value
# json -> java script object notation

# con la funcion open nosotros ya podriamos abrir un archivo

rutaSCV = "C:\\Users\\lukab\\OneDrive\\Escritorio\\PRIMER CUATRI\\programacion\\sabadojuju\\usuarios.csv"

# leer -> r/r+ (read) (si abrimos un archivo en r+ se abre para lectura y de forma secundaria para escritura)
# escribir -> w/w+ (write tiene la particularidad de que si el archivo no existe lo va a crear, y si ya lo tiene creado lo sobreescribe, 
# si abrimos con w+ se abre en modo escritura y de forma secundaria de lectura)
# añadir info -> a

# archivo = open(ruta, 'r') # el primer parametro pide lo que va a abrir y el segundo como lo va a abrir

# print(archivo)

# archivo.close()

# # funciones parser (traen informacion del csv y la parsean)
# def leer_csv(path:str)->list:
#     lista_retorno = []
#     with open(ruta:str, 'r') as archivo:
#         # segunda_lista_aux = archivo.readlines() esto es una etapa intermedia en lugar de iterar el objeto file de forma directa
#         for usuario in archivo:
#             usuario = usuario.replace("\n", " ")
#             lista_aux = usuario.split(',')
#             lista_retorno.append(lista_aux)
#     return lista_retorno

# def guardar_csv(ruta:str, lista_usuarios:list):
#     with open(ruta, 'w') as archivo:
#         for usuario in lista_usuarios:
#             archivo.write(",".join(usuario)+'\n')


# lista_usuarios = leer_csv(ruta)
# guardar_csv("prueba.csv", lista_usuarios)
# print(lista_usuarios)

rutaJSON = "C:\\Users\\lukab\\OneDrive\\Escritorio\\PRIMER CUATRI\\programacion\\sabadojuju\\usuario.json"

def leer_json(ruta:str)->list:
    with open(ruta, 'r') as archivo:
        diccionario_usuarios = json.load(archivo)
    return diccionario_usuarios["usuarios"]

def guardar_json(ruta:str, lista_usuarios:list)->None:
    with open(ruta, 'w') as archivo:
        json.dump(lista_usuarios, archivo, indent=4)

lista_usuarios = leer_json(rutaJSON)
guardar_json('prueba.json', lista_usuarios)

print(lista_usuarios)