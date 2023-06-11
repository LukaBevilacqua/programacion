import pygame, sys

WIDTH = 600 # width es ancho
HEIGHT = 400 # height es altura
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 30
SPEED = 5

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

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(NEGRO) 

pygame.display.set_caption("DVD") 


sup_1 = pygame.surface.Surface((100, 70))
sup_1.fill(ROJO)
rect_sup_1 = sup_1.get_rect()
rect_sup_1.center = CENTER

# manejar eventos:
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(NEGRO)
    if right:
        if rect_sup_1.right <= WIDTH:
            rect_sup_1.x += SPEED
        else:
            sup_1.fill(MAGENTA)
            right = False
    else:
        if rect_sup_1.left > 0:
            rect_sup_1.x -= SPEED 
        else:
            sup_1.fill(AMARILLO)
            right = True
    if fall:
        if rect_sup_1.bottom <= HEIGHT:
            rect_sup_1.y += SPEED
        else:
            sup_1.fill(AZUL)
            fall = False
    else:
        if rect_sup_1.top >= 0:
            rect_sup_1.y -= SPEED 
        else:
            sup_1.fill(ROJO)
            fall = True
    
    display.blit(sup_1, rect_sup_1)
    
    pygame.display.flip() 









