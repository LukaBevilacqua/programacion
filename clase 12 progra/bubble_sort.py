

lista = [3, 6, 5, 8, 12, 3, 9, 21, 5, 17]
# lista_nombres = ["Marcos", "Andrea", "Ramiro", "Jose", "Lucia"]

print(lista)
def ordenar_lista_creciente(lista:list):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if(lista[i] > lista[j]): # criterio de ordenamiento
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

print(lista)

def ordenar_lista_decreciente(lista:list):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if(lista[i] < lista[j]): # criterio de ordenamiento
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista(lista:list, key:str, ascendente = True):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (ascendente and lista[i][key] > lista[j][key]) or (not ascendente and lista[i][key] < lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux




