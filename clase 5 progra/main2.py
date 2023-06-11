from data import personas

flag = True


for persona in personas:
    if flag or (persona["edad"] > mayor_edad):
        flag = False
        mayor_edad = persona["edad"]
        nombre_mayor_edad = persona["nombre"]

print("------------------------------------------------------------------------------------------------------------------------------------")

print("Edad mayor: {}".format(mayor_edad))

print("El nombre de la persona mas longeva: {}".format(nombre_mayor_edad))

print("------------------------------------------------------------------------------------------------------------------------------------")


# *********FORMA BAUS********* 

persona_mayor = personas[0]

for poersona in personas:
    if persona["edad"] > persona_mayor["edad"]:
        persona_mayor = persona

print(persona_mayor)

for persona in personas:
    if persona["edad"] == mayor_edad:
        print(persona)