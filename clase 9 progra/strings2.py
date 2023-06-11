
cadena = "eSto Es uNa caDeNa 123"
cadena_larga = """Besa-bésame, mi amor
No sé cuánto tiempo me doy
Aprovechemos el hoy porque es hoy
(Porque es hoy)
Baby, tengo el alma deshidratada
No me ves bien la mirada tapada
Siempre peleando por alguna pavada
Cuando te beso no recibo nada
Sé que la vida no es cuento de hada
Tampoco pesadillas, pesan las alas
Ya no confío en ninguna palabra, el abracadabra
Cuando se va de la discotec'
Usa mi brazo de abrigo, ey
Susi no me ve de amigo, ey
Su novio sí, de enemigo, ey
Tomo, tomo para olvidar
El espejo dice "Convidá"
Abajo desde la mañana, vida así no es sana
Esperando que se me pase como fase
Hace-hace tiempo busco resultados
Y me puse sustancia to' descontrolado'
To' desaforado, sumergí la cara y casi que me ahogo
Y luego yo me dije que este no era el modo
Pero volví, como hacen todos, bueno, casi todos
Es difícil navegar cuando estás dentro del lodo
Difícil confiar, dando la mano te agarran el codo y
Besa-bésame, mi amor
No sé cuánto tiempo me doy
Aprovechemos el hoy porque es hoy
(Porque es hoy)
Yo se, bebé, que te fallé
Que me caí, me levanté
Lo perseguí y no paré
Lo conseguí y ahora me ven
¿Qué esperás de mí?
Si ya mi mitad te di
Y solo enemistad me dis-
Te, después de darte lo que alguna vez pediste
Ya no ando triste
Sé que no vales tanto como dijiste
Yeh, yeh, yeh
Girl, hoy solo yo sé
To' lo que pasé
Como coroné
Con sólo mi fe
Y ahora no ven
Como cambian, eh
Ya no espero na' de nadie, yea-yeah
Y listo, ahora ella me dejó en visto
Si cree que no me resisto
Puedo aguantarme hasta mañana
Si sé que esta noche me hablara y listo
Baby, yo sé que estoy listo
No como todos esos tipos
Yeh-eh-eh-eh
Besa-bésame, mi amor
No sé cuanto tiempo me doy
Aprovechemos el hoy porque es hoy (hoy-)
Porque es hoy (¿cuánto tiempo me doy?)"""

# aux = list(cadena)

# for caracter in aux:
#     if caracter.islower():
#         caracter = caracter.upper()

# print(aux)

# for i in range(len(aux)):
#     if aux[i].islower():
#         aux[i] = aux[i].upper()

# print(aux)

# cadena = "".join(aux) # "".join convierte a aux que era de tipo list a un str

# print(cadena)
#upper, lower, capitalize, isupper, islower, 

cadena2 = "     hola mundo     "

cadena3 = cadena2.strip() # elimina lo que le pase al metodo en este caso como no hay nada elimina los caracteres vacios
print(len(cadena3))

cadena3 = "     hola mundo00000".strip().strip("0")
print(cadena3)

print(cadena_larga.replace("amor", "pudor")) # replace solo acepta 2 valores adentro del parentesis el primero es la palabra a reemplazar y la segunda es lo que se reemplaza


cadena = "El debate siempre es bueno"
cadena3 = cadena.split("a") # dentro de los parentesis se escribe el caracter separador y seria el primero dentro de la cadena

print(cadena3)


