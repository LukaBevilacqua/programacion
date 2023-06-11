import pygame, sys


pygame.init()
RELOJ = pygame.time.Clock()
FPS = 60
ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

rectangulo = pygame.Rect(ANCHO / 2, ALTO / 2, 50, 50)
otro_rectangulo = pygame.Rect(ANCHO / 2, 500, 50, 50)

def mover_rectangulo(rectangulo: pygame.Rect, velocidad_y, alto_pantalla):
    rectangulo.y += velocidad_y
    if rectangulo.top > alto_pantalla:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    mover_rectangulo(rectangulo, 5, ALTO)
    mover_rectangulo(otro_rectangulo, -5, ALTO)

    pygame.draw.rect(pantalla, "Red", rectangulo)
    pygame.draw.rect(pantalla, "Blue", otro_rectangulo)
    
    pygame.display.flip()