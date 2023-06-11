

notas_p1 = []
notas_p2 = []
promedios = []

notas = []

# carga de notas

for i in range(2):
    d = {}
    auxInt = int(input("Ingrese nota parcial 1: "))
    #  validar auxInt --> que sea numero y este entre 0 y 10
    while auxInt < 1 or auxInt > 10:
        auxInt = int(input("Por favor ingrese una nota valida del parcial 1: "))
    notas_p1.append(auxInt)
    d["nota1"] = auxInt

    auxInt = int(input("Ingrese nota parcial 2: "))
    #  validar auxInt --> que sea numero y este entre 0 y 10
    while auxInt < 1 or auxInt > 10:
        auxInt = int(input("Por favor ingrese una nota valida del parcial 2: "))
    notas_p2.append(auxInt)
    d["nota2"] = auxInt

    prom = (notas_p1[i] + notas_p2[i]) / 2
    promedios.append(prom)
    d["promedio"] = (d["nota1"] + d["nota2"]) / 2

    notas.append(d)

# print(notas)

print(" *** Listado de Notas *** ")
print("parcial 1     parcial 2     promedio")

for calificacion in notas:
    print(f"    {calificacion['nota1']:2d}            {calificacion['nota2']:2d}         {calificacion['promedio']:5.2f}")

# print(" *** Listado de Notas *** ")
# print("parcial 1     parcial 2     promedio")

# for i in range(len(notas_p1)):
#     print(f"    {notas_p1[i]:2d}            {notas_p2[i]:2d}         {promedios[i]:5.2f}")