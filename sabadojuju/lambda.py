
# Lambda ---> anonimas

suma = lambda numeroUno, numeroDos : numeroUno + numeroDos

mayor = lambda numeroUno, numeroDos : numeroUno > numeroDos

print("Estamos usando la suma")
print(suma(2, 3))
print("Estamos consultando si es mayor o menor")
print(mayor(3, 10))

# operadores ternarios --> if else (en python)

mayor_edad = lambda numeroUno, numeroDos : numeroUno if numeroUno > numeroDos else numeroDos

print("Operador ternario")
print(mayor_edad(3, 10))

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Maria", "edad": 35}
]


# map, filter y reduce

# map ---> a una lista le tenemos que aplicar algo
print(map(lambda persona : persona["edad"] + 2, personas))
print(list(map(lambda persona : persona["nombre"], personas)))

# filter
print(list(filter(lambda persona: persona["edad"]>20, personas)))
print(personas)

# reduce
from functools import reduce
print(reduce(lambda personaUno, personaDos: personaUno + personaDos["edad"], personas, 0))

# filter:
lista = []
for persona in personas:
    if persona["edad"] > 30:
        lista.append(persona)


# shallow copy y deep copy

# shallow copy
print("Shallow copy:")
lista_a = [[1,2,3],[4,5,6],[7,8,9]]

lista_b = list(lista_a)

print(lista_a)
print(lista_b)

lista_a.append(['nueva lista'])

print(lista_a)
print(lista_b)

lista_a[1][0] = 'A'

print(lista_a)
print(lista_b)

# deep copy
print("Deep copy:")
from copy import deepcopy

lista_a = [[1,2,3],[4,5,6],[7,8,9]]

lista_b = deepcopy(lista_a)

print(lista_a)
print(lista_b)

lista_a.append(['nueva lista'])

print(lista_a)
print(lista_b)

lista_a[1][0] = 'A'

print(lista_a)
print(lista_b)


# shallow copy
print("Shallow copy en diccionarios:")
import copy

diccionario_original = {"a": 1, "b": 2, "c": [3, 4]}
copia_diccionario = copy.copy(diccionario_original)

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["c"][0] = "A"

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["a"] = "A"

print(diccionario_original)
print(copia_diccionario)

# deep copy
print("Deep copy en diccionarios:")

diccionario_original = {"a": 1, "b": 2, "c": [3, 4]}
copia_diccionario = copy.deepcopy(diccionario_original)

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["c"][0] = "A"

print(diccionario_original)
print(copia_diccionario)

copia_diccionario["a"] = "A"

print(diccionario_original)
print(copia_diccionario)


persona = {"nombre": "Maria", "edad": 35, "altura": 1.60}

print("Get:")
# get deveulve el valor de la clave pasada por parametro
print(persona.get("nombre"))
print(persona.get("dni", "No existe el campo ingresado"))

print("Keys:")
# keys devuelve todas las claves
print(list(persona.keys()))

print("Values:")
# values devuelve todos los valores
print(list(persona.values()))

print("Items:")
# items devuelve tuplas
print(list(persona.items()))

print("keys:")
# keys devuelve todas las claves
print(list(persona.keys()))

print("pop:")
# pop nos permite eliminar una clave de nuestro diccionario y nos retorna el valor
print(persona.pop("altura"))
print(persona)


try:
    numero = int(input("Ingrese un numero: "))
    print(numero)
except ValueError:
    print("Lo ingresado no es un numero")



# map reduce filter
# una explicacion de como funcionan por dentro

def my_map(funcion, lista):
    lista_nueva = []

    for elemento in lista:
        elemento_mapeado = funcion(elemento)
        lista_nueva.append(elemento_mapeado)

    return lista_nueva



# lista_nombre = my_map(lambda serie : serie["nombre"], series)
# print(lista_nombre)

def my_reduce(funcion, lista):
    flag_primer_elemento = True
    for elemento in lista:
        if flag_primer_elemento:
            valor = elemento
            flag_primer_elemento = False
        else:
            valor = funcion(valor, elemento)
    return valor

a = [2,2,3]
print(my_reduce(lambda x,y : x + y, a))

def my_filter(funcion, lista):
    lista_filtrada = []
    for elemento in lista:
        if funcion(elemento):
            lista_filtrada.append(elemento)

    return lista_filtrada

print(my_filter(lambda numero: numero >2, a))








