# 22 - 12 - 2024

import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Second Tutorial - Borderline, Jumping")

x = 50
y = 425
width = 40
height = 60
vel = 5
jump_Count = 10

isJump = False
run = True

while run:
    pygame.time.delay(100)

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < (500 - width - vel):
        # print(500 - width - vel)
        x = x + vel

    if not(isJump):
        if keys[pygame.K_DOWN] and y < (500 - height - vel):
            y = y + vel
        if keys[pygame.K_UP] and y > vel:
            y = y - vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_Count >= - 10:
            neg = 1
            if jump_Count < 0:
                neg = -1
            y = y - (jump_Count ** 2) * 0.5 * neg
            jump_Count = jump_Count - 1
        else:
            isJump = False
            jump_Count = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
