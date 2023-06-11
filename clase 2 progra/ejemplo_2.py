a = "hola"

try:
    a = int(a)

except ValueError:
    print("Trataste de convertir a entero una cadena")
    ## pass ## se usa cuando no escribi nada pero no quiero que me tire error

else:
    print(a)

finally:
    print("Estoy en el finally")