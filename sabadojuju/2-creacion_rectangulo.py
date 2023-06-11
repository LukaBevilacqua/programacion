import pygame, sys

pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

rectangulo = pygame.Rect(ANCHO / 2, ALTO / 2, 50, 50)
otro_rectangulo = pygame.Rect(ANCHO / 2, 500, 50, 50)

while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    pygame.draw.rect(pantalla, "Red", rectangulo)
    pygame.draw.rect(pantalla, "Blue", otro_rectangulo)
    
    pygame.display.flip()