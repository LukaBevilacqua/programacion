a = 30
b = 2

while True:
    try:
        resultado = a / b

    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print(resultado)



