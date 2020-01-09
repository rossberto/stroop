import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True
screen.fill((15,50,200))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill((123,0,0))
            if event.key == pygame.K_LEFT:
                screen.fill((0,123,0))
            if event.key == pygame.K_DOWN:
                screen.fill((0,0,123))

    pygame.display.update()
