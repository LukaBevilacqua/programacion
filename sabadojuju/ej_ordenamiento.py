# 1. Crea una función que ordene una lista de números enteros de menor a mayor. Puedes utilizar cualquier método de ordenamiento que conozcas.

lista_numerica = [3, 4, 21, 2, 11, 44, 0, 22, 99, 1]

def ordenar_lista_numerica_menor_mayor(lista:list):
    flag_cambio = True
    contador = 1
    while flag_cambio:
        flag_cambio = False
        for i in range(len(lista) - contador):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_cambio = True
        contador = contador + 1


ordenar_lista_numerica_menor_mayor(lista_numerica)
print(lista_numerica)

# 2. Crea una función que ordene una lista de cadenas alfabéticamente de A a Z.

lista_alfabetica = ["arriba", "abajo", "izquierda", "derecha"]

def ordenar_lista_alfabetica(lista:list):
    flag_cambio = True
    contador = 1
    while flag_cambio:
        for i in range(len(lista) - contador):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag_cambio = True
        contador = contador + 1

ordenar_lista_alfabetica(lista_alfabetica)
print(lista_alfabetica)










# 3. Crea una función que ordene un diccionario de estudiantes por calificación de mayor a menor.

# 4. Crea una función que ordene una lista de diccionarios con información sobre libros 
# (título, autor, año de publicación) por año de publicación de menor a mayor.

# 5. Crea una función que ordene un diccionario que mapee nombres de frutas a su precio por kilogramo de menor a mayor.

# 6. Crea una función que ordene una lista de tuplas (nombre, edad, altura) primero por edad de menor a mayor y luego por altura de menor a mayor.
