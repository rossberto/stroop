import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

font = pygame.font.Font('freesansbold.ttf', 32)
textX = 400
textY = 300

text = font.render('Color', True, (255,255,255))
screen.blit(text, (textX, textY))


running = True
screen.fill((15,50,200))

def newBattle():
    colors = ['Rojo', 'Verde', 'Azul']
    rgb_colors = [(255,0,0), (0,255,0), (0,0,255)]

    background_color = random.choice(rgb_colors)
    font_color = random.choice(rgb_colors)
    while font_color == background_color:
        font_color = random.choice(rgb_colors)

    screen.fill(background_color)
    text = font.render(random.choice(colors), True, font_color)
    screen.blit(text, (textX, textY))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mensaje = ''

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mensaje = 'Se presiono A'
            if event.key == pygame.K_s:
                mensaje = 'Se presiono S'
            if event.key == pygame.K_d:
                mensaje = 'Se presiono D'

            newBattle()

        pygame.display.update()
