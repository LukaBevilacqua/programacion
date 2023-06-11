import pygame, sys

class Paleta:
    def __init__(self, posicion_inicial, tamaño, velocidad_y, color):
        self.surface = pygame.Surface(tamaño)
        self.surface.fill(color)
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.center = posicion_inicial
        self.velocidad = velocidad_y

    def mover_y(self, alto_pantalla):
        self.rectangulo.y += self.velocidad
        if self.rectangulo.top > alto_pantalla:
            self.rectangulo.bottom = 0
        elif self.rectangulo.bottom < 0:
            self.rectangulo.top = alto_pantalla

    def verificar_colision(self, otra_paleta):
        if self.rectangulo.colliderect(otra_paleta.rectangulo):
            self.surface.fill("Green")
            otra_paleta.surface.fill("Yellow")

    def draw(self, pantalla):
        pantalla.blit(self.surface, self.rectangulo)

    def update(self, pantalla):
        self.mover_y(pantalla.get_height())
        self.draw(pantalla)


pygame.init()
RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

paleta_uno = Paleta((ANCHO / 2, ALTO / 2), (50, 50), 5, "Red")

paleta_dos = Paleta((ANCHO / 2, ALTO / 2), (50, 50), -5, "Blue")

while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    paleta_uno.update(pantalla)
    paleta_dos.update(pantalla)

    pygame.display.flip()