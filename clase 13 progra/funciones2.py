


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(operando_a, operando_b, operacion):
    return operacion(operando_a, operando_b)

# def calcularSuperficie(base, altura):
#     return base * altura

calcularSuperficie = lambda base, altura: base * altura

print(calcular(5, 6, calcularSuperficie))



# print(calcular(3, 4, sumar))
# print(calcular(3, 4, restar))
# print(calcular(3, 4, multiplicar))
# print(calcular(3, 4, dividir))




