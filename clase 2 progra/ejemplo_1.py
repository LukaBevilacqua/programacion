
while True:
    try:
        edad = int(input("Ingrese edad 18-65: "))
        
        if(not(edad < 18 or edad > 65)):
            break
        else:
            print("Edad fuera del rango")

    except ValueError:
        print("Eso no es un numero")


print(edad)
