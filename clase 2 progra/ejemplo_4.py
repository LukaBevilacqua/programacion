
while True:
    edad = input("Ingrese edad 18-65: ")

    if(edad.isdigit()):
        edad = int(edad)
        if not edad < 18 or edad > 65:
            break
        else:
            print("Edad fuera del rango")
    else:
        print("Eso no es un numero")

print(edad)










## variable = "hola"

## print(variable.isalpha())

## print("12345".isdigit())
