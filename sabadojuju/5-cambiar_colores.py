import pygame, sys

pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

superficie_rectangulo = pygame.Surface((50, 50))
superficie_rectangulo.fill("Red")
rectangulo = superficie_rectangulo.get_rect()
rectangulo.center = (ANCHO / 2, ALTO / 2)

superficie_otro_rectangulo = pygame.Surface((50, 50))
superficie_otro_rectangulo.fill("Blue")
otro_rectangulo = superficie_otro_rectangulo.get_rect()
otro_rectangulo.center = (ANCHO / 2, ALTO / 2)

def mover_rectangulo(rectangulo: pygame.Rect, velocidad_y, alto_pantalla):
    rectangulo.y += velocidad_y
    if rectangulo.top > alto_pantalla:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

def verificar_colision(rectangulo: pygame.Rect, superficie_rectangulo, otro_rectangulo: pygame.Rect, superficie_otro_rectangulo):
    if rectangulo.colliderect(otro_rectangulo):
        superficie_rectangulo.fill("Green")
        superficie_otro_rectangulo.fill("Yellow")
    else:
        superficie_rectangulo.fill("Red")
        superficie_otro_rectangulo.fill("Blue")


while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    mover_rectangulo(rectangulo, 5, ALTO)
    mover_rectangulo(otro_rectangulo, -5, ALTO)

    verificar_colision(rectangulo,superficie_rectangulo, otro_rectangulo, superficie_otro_rectangulo)

    pantalla.blit(superficie_rectangulo, rectangulo)
    pantalla.blit(superficie_otro_rectangulo, otro_rectangulo)
    
    pygame.display.flip()