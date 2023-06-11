import re
# path relativo/absoluto
# relativo es desde donde estamos parados
# 

file = open("clase 11 progra\carta.txt", "r")

# r lectura de texto
# w escritura de texto
# rb lectura binaria
# wb escritura binaria
# a para hacer un agregado tipo append o una concatenacion
# ab es lo mismo que a pero en binario

contenido = file.read()
print(contenido)
contenido = contenido.split("\n")
print(contenido)

file.close()

for i in range(len(contenido)):
    # contenido[i] = contenido[i].replace("\n", "")
    # contenido[i] = contenido[i].strip("\n")
    contenido[i] = re.sub("\n$", "", contenido[i])
    print(contenido[i])