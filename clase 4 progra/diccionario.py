lista = [1, 2, 3]

diccionario = {"nota1":2, "nota2":4, "promedio":2.0}

alumno = {
    "legajo":103450,
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juancito@gmail.com",
    "edad": 20
}

# print(type(diccionario)
# print(diccionario)

# print(lista[0])
# print(diccionario["promedio"])

# for elemento in lista:
#     print(elemento)

# print("------------------------------------------")

# for clave in diccionario:
#     print(clave, diccionario[clave])

print(alumno["nombre"])

print("------------------------------------------")

alumno["nombre"] = "Jose"

print(alumno)

print("------------------------------------------")

alumno["localidad"] = "Avellaneda"

print(alumno)

print("------------------------------------------")

del alumno["email"] # del: deletea una variable dentro de una lista o un diccionario

print(alumno)

print("------------------------------------------")

# for key in alumno.keys():
#     print(key)

print(alumno.values())

print("------------------------------------------")

for valor in alumno.values():
    print(valor)

print("------------------------------------------")

campo = "nombre"

print(alumno.get(campo))
print(alumno[campo])

print("------------------------------------------")
