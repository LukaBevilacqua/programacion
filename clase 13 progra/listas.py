def mostarElementos(lista:list):
    for elemento in lista:
        print(elemento, " ", end= "")
    print("\n---------------------------")

def duplicarElementos(lista:list):
    for indice in range(len(lista)):
        lista[indice] = lista[indice] * 2

lista_numerica = [3,2,4,5,6,1]




mostarElementos(lista_numerica)
duplicarElementos(lista_numerica)
mostarElementos(lista_numerica)