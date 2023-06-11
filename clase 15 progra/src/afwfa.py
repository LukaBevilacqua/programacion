import pygame, sys

WIDTH = 600 # width es ancho
HEIGHT = 400 # height es altura
CENTER = (WIDTH // 2, HEIGHT // 2)
MIDBOTTOM = (WIDTH // 2, HEIGHT)
MIDTOP = (WIDTH // 3, HEIGHT // 8)
FPS = 30
SPEED = 5
SPEED2 = 4

clock = pygame.time.Clock()

fall = True # es una bandera
right = True
fall2 = True # es una bandera
right2 = True
up = True
left = True

# cada color ocupa un 1byte
# (rojo, verde, azul)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_NO_TAN_AZUL = (0, 0, 155)
AZUL_NO_AZUL = (0, 0, 100)
AZULILLO = (0, 0, 200)
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

pygame.display.set_caption("BEYI GAME´S") 


sup_1 = pygame.surface.Surface((50, 50))
sup_1.fill(AZUL_NO_TAN_AZUL)
rect_sup_1 = sup_1.get_rect()
rect_sup_1.midbottom = MIDBOTTOM

sup_2 = pygame.surface.Surface((50, 50))
sup_2.fill(AZUL)
rect_sup_2 = sup_2.get_rect()
rect_sup_2.midbottom = MIDBOTTOM

sup_4 = pygame.surface.Surface((50, 50))
sup_4.fill(AZULILLO)
rect_sup_4 = sup_4.get_rect()
rect_sup_4.midbottom = MIDBOTTOM

sup_5 = pygame.surface.Surface((50, 50))
sup_5.fill(AZUL_NO_AZUL)
rect_sup_5 = sup_5.get_rect()
rect_sup_5.midbottom = MIDBOTTOM

fuente = pygame.font.SysFont("arial black", 30)
texto = fuente.render("BEYI GAME´S", True, BLANCO)

# manejar eventos:
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill(NEGRO)

    if right2:
        if rect_sup_4.left > 0:
            rect_sup_4.x -= SPEED
        else:
            right2 = False
    else:
        if rect_sup_4.right <= WIDTH:
            rect_sup_4.x += SPEED
        else:
            right2 = True
    if fall2:
        if rect_sup_4.top >= 0:
            rect_sup_4.y -= SPEED
        else:
            fall2 = False
    else:
        if rect_sup_4.bottom <= HEIGHT:
            rect_sup_4.y += SPEED
        else:
            fall2 = True
    
    display.blit(sup_4, rect_sup_4)

    if right2:
        if rect_sup_5.left > 0:
            rect_sup_5.x -= SPEED
        else:
            right2 = False
    else:
        if rect_sup_5.right <= WIDTH:
            rect_sup_5.x += SPEED
        else:
            right2 = True
    if fall2:
        if rect_sup_5.top >= 0:
            rect_sup_5.y -= SPEED
        else:
            fall2 = False
    else:
        if rect_sup_5.bottom <= HEIGHT:
            rect_sup_5.y += SPEED
        else:
            fall2 = True
    
    display.blit(sup_5, rect_sup_5)

    display.blit(texto, MIDTOP)

    if right:
        if rect_sup_2.left > 0:
            rect_sup_2.x -= SPEED
        else:
            right = False
    else:
        if rect_sup_2.right <= WIDTH:
            rect_sup_2.x += SPEED
        else:
            right = True
    if fall:
        if rect_sup_2.top >= 0:
            rect_sup_2.y -= SPEED
        else:
            fall = False
    else:
        if rect_sup_2.bottom <= HEIGHT:
            rect_sup_2.y += SPEED
        else:
            fall = True
    
    display.blit(sup_2, rect_sup_2)

    if right:
        if rect_sup_1.right <= WIDTH:
            rect_sup_1.x += SPEED
        else:
            right = False
    else:
        if rect_sup_1.left > 0:
            rect_sup_1.x -= SPEED 
        else:
            right = True
    if fall:
        if rect_sup_1.bottom <= HEIGHT:
            rect_sup_1.y += SPEED
        else:
            fall = False
    else:
        if rect_sup_1.top >= 0:
            rect_sup_1.y -= SPEED 
        else:
            fall = True
    
    display.blit(sup_1, rect_sup_1)

    
    pygame.display.flip() 









