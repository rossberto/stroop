import pygame
import random

# pygame initialization
pygame.init()

# Screen creation
screen = pygame.display.set_mode((720,720))

# Start Background
start_background = pygame.image.load('intersection-rgb.png')

# Color font
color_font = pygame.font.Font('freesansbold.ttf', 128)
# Color word position
textX = 250
textY = 300

# Score font
score_font = pygame.font.Font('freesansbold.ttf', 32)
# Player 1 score position
scoreX = 10
scoreY = 10

player_1_score = 0
player_2_score = 0

running = True
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def newBattle():
    colors = ['Rojo', 'Verde', 'Azul']

    rgb_colors = [RED, GREEN, BLUE]

    background_color = random.choice(rgb_colors)
    font_color = random.choice(rgb_colors)
    while font_color == background_color:
        font_color = random.choice(rgb_colors)

    screen.fill(background_color)
    text = color_font.render(random.choice(colors), True, font_color)
    screen.blit(text, (textX, textY))

    return font_color

def showScore():
    score_text = score_font.render('Player 1: ' + str(player_1_score), True, (255,255,255))
    screen.blit(score_text, (scoreX, scoreY))
    score_text = score_font.render('Player 2: ' + str(player_2_score), True, (255,255,255))
    screen.blit(score_text, (scoreX + 500, scoreY))

game_state = 'START'
color = BLUE
release = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == 'START':
            screen.blit(start_background, (0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if color == BLUE:
                        game_state = 'GAME'
                    release = True
        elif game_state == 'GAME':
            if event.type == pygame.KEYUP and release:
                release = False
                color = newBattle()
                showScore()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if color == RED:
                        player_1_score += 1
                    release = True
                if event.key == pygame.K_s:
                    if color == GREEN:
                        player_1_score += 1
                    release = True
                if event.key == pygame.K_d:
                    if color == BLUE:
                        player_1_score += 1
                    release = True
                if event.key == pygame.K_KP4:
                    if color == RED:
                        player_2_score += 1
                    release = True
                if event.key == pygame.K_KP5:
                    if color == GREEN:
                        player_2_score += 1
                    release = True
                if event.key == pygame.K_KP6:
                    if color == BLUE:
                        player_2_score += 1
                    release = True


        pygame.display.update()
