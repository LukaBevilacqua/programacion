import pygame, sys

WIDTH = 600 # width es ancho
HEIGHT = 400 # height es altura
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 30
SPEED = 10

clock = pygame.time.Clock()

fall = True
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

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(NEGRO) 

pygame.display.set_caption("Primer Aplicación") 

sup_1 = pygame.image.load("./clase 15 progra/src/images/espiral.png").convert_alpha() # convert() hace que quede mejor pero pierde la transparencia por eso se usa conver_alpha()
sup_1 = pygame.transform.scale(sup_1, (100, 100))
rect_sup_1 = sup_1.get_rect()
rect_sup_1.center = CENTER

sup_2 = pygame.image.load("./clase 15 progra/src/images/espiral.png").convert_alpha() # convert() hace que quede mejor pero pierde la transparencia por eso se usa conver_alpha()
sup_2 = pygame.transform.scale(sup_2, (100, 100))
rect_sup_2 = sup_2.get_rect()
rect_sup_2.center = CENTER

# manejar eventos:
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # manejo de botones del mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                print("Principal", evento.pos)
            if evento.button == 2:
                print("Medio")
            if evento.button == 3:
                print("Secundario")
            if evento.button == 4:
                print("Scroll arriba")
            if evento.button == 5:
                print("Scroll abajo")
        
        # manejo de teclas presionadas una sola vez
        if evento.type == pygame.KEYDOWN:
            match evento.key:
                case pygame.K_LEFT:
                    print("izquierda")
                
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                print("Izquierda")
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                print("Derecha")
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                print("Arriba")
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                print("Abajo")

    # manejo de teclas que se mantienen presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        print("izquierda")


    pygame.display.flip()









