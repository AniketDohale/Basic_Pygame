# 22 - 12 - 2024

import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Tutorial")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - vel
    if keys[pygame.K_RIGHT]:
        x = x + vel
    if keys[pygame.K_DOWN]:
        y = y + vel
    if keys[pygame.K_UP]:
        y = y - vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
