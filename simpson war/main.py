import pygame, sys
from config import *
import random
from donas import Dona

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donuts War")

icono = pygame.transform.scale(pygame.image.load("simpson war/assets/images/dona.png").convert_alpha(), SIZE_ICON)
pygame.display.set_icon(icono)

font = pygame.font.Font("simpson war/assets/fonts/simpsons.ttf", 48)

score = 0

sonido = pygame.mixer.Sound("simpson war/assets/sounds/ouch.mp3")
pygame.mixer.music.load("simpson war/assets/sounds/ouch.mp3")
flag_sound = True

fondo = pygame.transform.scale(pygame.image.load("simpson war/assets/images/background.jpg").convert(), SIZE_SCREEN)

donas = []

for i in range(10):
    x = random.randrange(30, WIDTH - 30)
    y = random.randrange(-1000, 0)

    dona = Dona(DONUT_SIZE, (x, y), "simpson war/assets/images/dona.png")

    # dona = pygame.transform.scale(pygame.image.load("simpson war/assets/images/dona.png").convert_alpha(), DONUT_SIZE)
    # dona.get_rect().center = (random.randrange(30, WIDTH - 30), random.randrange(-1000, 0))
    donas.append(dona)
    # rect_dona = dona.get_rect()
    # rect_dona.midtop = (DISPLAY_MIDTOP)
    # flag_dona = True



# homero = pygame.transform.scale(pygame.image.load("simpson war/assets/images/homero.png").convert_alpha(), SIZE_HOMERO)
homero_l = pygame.transform.scale(pygame.image.load("simpson war/assets/images/homer_left.png").convert_alpha(), SIZE_HOMERO)
homero_r = pygame.transform.scale(pygame.image.load("simpson war/assets/images/homer_right.png").convert_alpha(), SIZE_HOMERO)
homero = homero_l
rect_homer = homero_l.get_rect()
rect_homer.midbottom = (CENTER_X, DISPLAY_BOTTOM)
rect_boca = pygame.rect.Rect(0, 0, 50, 10)
rect_boca.x = rect_homer.x + 40
rect_boca.y = rect_homer.y + 130

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if rect_homer.left > DISPLAY_LEFT:
            rect_homer.x -= HOMER_SPEED
            homero = homero_l
            rect_boca.x = rect_homer.x + 40
            rect_boca.y = rect_homer.y + 130

    if keys[pygame.K_d]:
        if rect_homer.right < DISPLAY_RIGHT:
            rect_homer.x += HOMER_SPEED
            rect_boca.x = rect_homer.x + 70
            rect_boca.y = rect_homer.y + 130
            homero = homero_r

    
    if rect_boca.colliderect(dona.rect):
        flag_dona = False
        if flag_sound:
            score += 1
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(0.3)
        flag_sound = False
    else:
        flag_sound = True

    screen.blit(fondo, ORIGIN)

    screen.blit(font.render("Score: "+ str(score), True, GREEN), SCORE_POS)

    pygame.draw.rect(screen, RED, rect_boca)
    screen.blit(homero, rect_homer)

    for i in donas:
        if dona.rect.bottom < DISPLAY_BOTTOM:
            flag_dona = True
            flag_sound = True
            if dona.active:
                dona.update()
            else:
                dona.rect.y = 0
            if rect_boca.colliderect(dona.rect):
                dona.active = False
                if flag_sound:
                    score += 1
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_pos(0.3)
                    flag_sound = False
                else:
                    flag_sound = True

            if dona.active:
                screen.blit(dona.image, dona.rect)

    pygame.display.flip()