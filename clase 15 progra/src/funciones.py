import pygame


def colision_circulos(rectangulo_1: pygame.rect.Rect, rectangulo_2: pygame.rect.Rect):
    colision = False
    cateto_x = rectangulo_1.centerx - rectangulo_2.centerx
    cateto_y = rectangulo_1.centery - rectangulo_2.centery
    distancia = (cateto_x ** 2 + cateto_y ** 2) ** 0.5
    limite = rectangulo_1.width // 2 + rectangulo_2.width // 2

    if distancia <= limite:
        colision = True

    return colision