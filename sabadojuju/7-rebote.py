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
        # self.mover_y(pantalla.get_height())
        self.draw(pantalla)

class Pelota:
    def __init__(self, tamaño, velocidad, tamaño_pantalla):
        self.surface = pygame.Surface(tamaño)
        self.surface.fill("White")
        self.pos_inicial = (tamaño_pantalla[0] / 2, tamaño_pantalla[1] / 2)
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.center = self.pos_inicial
        self.velocidad = velocidad
        self.orientacion_x = 1
    
    def mover_x(self, ancho_pantalla):
        self.rectangulo.x += self.velocidad * self.orientacion_x
        if self.rectangulo.left > ancho_pantalla or self.rectangulo.right < 0:
            self.rectangulo.center = self.pos_inicial
    
    def vericar_colision(self, paletas):
        for paleta in paletas:
            if self.rectangulo.colliderect(paleta.rectangulo):
                self.orientacion_x = self.orientacion_x * -1

    def draw(self, pantalla):
        pantalla.blit(self.surface, self.rectangulo)

    def update(self, pantalla):
        # self.mover_y(pantalla.get_height())
        self.draw(pantalla)
        self.vericar_colision(paletas)
        self.mover_x(pantalla.get_width())


pygame.init()
RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

paleta_uno = Paleta((30, ALTO / 2), (25, 150), 5, "Red")

paleta_dos = Paleta((ANCHO - 30, ALTO / 2), (25, 150), -5, "Blue")

pelota = Pelota((25, 25), 10, (ANCHO, ALTO))

paletas = [paleta_uno, paleta_dos]

pygame.display.set_caption("PONG")

while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    paleta_uno.update(pantalla)
    paleta_dos.update(pantalla)
    pelota.update(pantalla)

    pygame.display.flip()