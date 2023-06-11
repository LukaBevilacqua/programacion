from data_stark import lista_personajes

def esta_en_lista(lista:list, key:str)->bool:
    esta = False
    for elemento in lista:
        if elemento == key:
            esta = True
            break
    return esta

lista = []
colores = []

for heroe in lista_personajes:
    lista.append(heroe.copy())

for heroe in lista:
    if not esta_en_lista(colores, heroe["color_pelo"]):
        colores.append(heroe["color_pelo"])

print(colores)

for color in colores:
    print("Color: " + color)
    for heroe in lista:
        if heroe["color_pelo"] == color:
            print(heroe["nombre"], heroe["color_pelo"])
    print("----------------------------------------------------") 
