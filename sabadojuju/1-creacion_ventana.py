import pygame, sys

pygame.init()

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()