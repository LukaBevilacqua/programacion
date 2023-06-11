import pygame, sys
from funciones import colision_circulos

WIDTH = 600 # width es ancho
HEIGHT = 400 # height es altura
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 30
SPEED = 10

clock = pygame.time.Clock()

fall = True # es una bandera
right = True

# cada color ocupa un 1byte
# (rojo, verde, azul)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CUSTOM = (157, 123, 236)
AMARILLO = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# configuracion:
pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT)) # esto es para configurar la pantalla
display.fill(NEGRO) # esto lo que hace es llenarlo, osea pintarlo del color que elija

# fuentes = pygame.font.get_fonts() # esto es para saber que fuentes tiene la pc
# print(fuentes)

sonido = pygame.mixer.music
sonido.load("./clase 15 progra/src/sounds/pum.mp3")
sonido_2= pygame.mixer.Sound("./clase 15 progra/src/sounds/pum.mp3")



fuente = pygame.font.SysFont("rage", 48)
texto = fuente.render("", True, AMARILLO)



fondo = pygame.image.load("./clase 15 progra/src/images/noche.jpg").convert() # convert() hace que quede mejor pero pierde la transparencia por eso se usa conver_alpha()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))



pygame.display.set_caption("Primer Aplicación") # esto le pone nombre a la ventana

# un rectangulo se hace con rect cuando despues lo queremos manipular/mover etc
rect_1 = pygame.rect.Rect(100, 50, 120, 70) # esto crea un rectangulo, (x, y, width, height)
rect_1.center = CENTER
# en cambio si no quiero que se mueva y tan solo quiero que este de fondo lo deberia hacer con una tupla
rect_2 = (200, 200, 120, 60)# esto crea un rectangulo pero con tuplas, (x, y, width, height)



sup_1 = pygame.image.load("./clase 15 progra/src/images/espiral.png").convert_alpha() # convert() hace que quede mejor pero pierde la transparencia por eso se usa conver_alpha()
sup_1 = pygame.transform.scale(sup_1, (100, 100))
# sup_1 = pygame.surface.Surface((70, 70)) # esto crea una superficie
# sup_1.fill(ROJO)
rect_sup_1 = sup_1.get_rect()
rect_sup_1.center = CENTER


sup_2 = pygame.image.load("./clase 15 progra/src/images/espiral.png").convert_alpha() # convert() hace que quede mejor pero pierde la transparencia por eso se usa conver_alpha()
sup_2 = pygame.transform.scale(sup_2, (100, 100))
# sup_2 = pygame.surface.Surface((70, 70)) # esto crea una superficie
# sup_2.fill(AZUL)
rect_sup_2 = sup_2.get_rect()
rect_sup_2.center = CENTER

explosion = pygame.image.load("./clase 15 progra/src/images/explosion.png").convert_alpha()
explosion = pygame.transform.scale(explosion, (rect_sup_1.width, rect_sup_1.height))



# manejar eventos:
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit() # esto es lo contrario al ".init"
            sys.exit() # esto cierra desde el sistema el juego(?

    # display.fill(CYAN)

    if right:
        if rect_sup_2.right <= WIDTH:
            rect_sup_2.x += SPEED
        else:
            right = False
    else:
        if rect_sup_2.left > 0:
            rect_sup_2.x -= SPEED # con esto controlo el desplazamiento
        else:
            right = True

    # if rect_1.colliderect(rect_2):
    if colision_circulos(rect_sup_1, rect_sup_2):
        texto = fuente.render("PUM!!!", True, AMARILLO)
        display.blit(explosion, rect_sup_1)
        display.blit(explosion, rect_sup_2)
        sonido_2.play()
    else:
        texto = fuente.render("", True, AMARILLO)

    if fall:
        if rect_sup_1.bottom <= HEIGHT:
            rect_sup_1.y += SPEED
        else:
            fall = False
    else:
        if rect_sup_1.top >= 0:
            rect_sup_1.y -= SPEED # con esto controlo el desplazamiento
        else:
            fall = True



    
    display.blit(fondo, (0, 0))
    display.blit(sup_2, rect_sup_2) # blitear: calcar elementos
    display.blit(sup_1, rect_sup_1) # blitear: calcar elementos
    display.blit(texto, (0, 0))

    pygame.draw.line(display, MAGENTA, (WIDTH // 2, 0),(WIDTH // 2, HEIGHT))
    pygame.draw.line(display, MAGENTA, (0, HEIGHT // 2),( WIDTH, HEIGHT // 2))

    # pygame.draw.rect(display, VERDE, rect_1) # esto es un rectangulo

    # pygame.draw.rect(display, AZUL, (200, 200, 120, 70), 5) # esto es un rectangulo

    # pygame.draw.circle(display, ROJO,(300, 250), 50, 2, True, False, True, False) # esto es un circulo
    # pygame.draw.circle(display, VERDE,(300, 250), 50, 2, False, True, False, True) # esto es un circulo

    # pygame.draw.line(display, MAGENTA, (WIDTH // 2, HEIGHT // 2), (WIDTH, HEIGHT), 5) # esto es una linea

    # pygame.draw.rect(display, AZUL, (50, 70, 120, 120), 5) # esto es un cuadrado

    # pygame.draw.ellipse(display, CYAN, (200, 300, 120, 70), 3) # esto es una elipse

    # pygame.draw.polygon(display, AMARILLO, [(20, 20), (200, 75), (170, 300)], 4) # esto es un poligono
    
    pygame.display.flip() # el metodo flip() sirve para actualizar/refrezcar la pantalla









