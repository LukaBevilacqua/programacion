file = open("carta2.txt", "w")

file.write("Hola esto es un nuevo archivo\n")
file.write("Hola esto es un nuevo archivo\n")
file.write("Hola esto es un nuevo archivo\n")
file.write("Hola esto es un nuevo archivo")

file.close()







lista = []
with open("carta2.txt", "w") as file:
    linea = file.writelines()
    lista.append(linea.replace("\n", ""))