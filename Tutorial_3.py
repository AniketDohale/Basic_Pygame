# 23 - 12 - 2024

import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Third Tutorial - Character Animation, Sprites")

clock = pygame.time.Clock()

char_Walk_Right = [pygame.image.load('imgs/Character_1/R1.png'),
                   pygame.image.load('imgs/Character_1/R2.png'),
                   pygame.image.load('imgs/Character_1/R3.png'),
                   pygame.image.load('imgs/Character_1/R4.png'),
                   pygame.image.load('imgs/Character_1/R5.png'),
                   pygame.image.load('imgs/Character_1/R6.png'),
                   pygame.image.load('imgs/Character_1/R7.png'),
                   pygame.image.load('imgs/Character_1/R8.png'),
                   pygame.image.load('imgs/Character_1/R9.png')]

char_Walk_Left = [pygame.image.load('imgs/Character_1/L1.png'),
                   pygame.image.load('imgs/Character_1/L2.png'),
                   pygame.image.load('imgs/Character_1/L3.png'),
                   pygame.image.load('imgs/Character_1/L4.png'),
                   pygame.image.load('imgs/Character_1/L5.png'),
                   pygame.image.load('imgs/Character_1/L6.png'),
                   pygame.image.load('imgs/Character_1/L7.png'),
                   pygame.image.load('imgs/Character_1/L8.png'),
                   pygame.image.load('imgs/Character_1/L9.png')]

background = pygame.image.load('imgs/Backgrounds/bg.jpg')

char = pygame.image.load('imgs/Character_1/standing.png')

x = 50
y = 400
width = 64
height = 64
vel = 5
jump_Count = 10

isJump = False
run = True

left = False
right = False
walk_Count = 0


def redraw_Game_Window():
    global walk_Count
    win.blit(background, (0, 0))

    if walk_Count + 1 >= 27:
        walk_Count = 27
    
    if left:
        win.blit(char_Walk_Left[walk_Count//3], (x,y))
        walk_Count = walk_Count + 1
    elif right:
        win.blit(char_Walk_Right[walk_Count//3], (x,y))
        walk_Count = walk_Count + 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


while run:
    clock.tick(27)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < (500 - width - vel):
        # print(500 - width - vel)
        x = x + vel
        right = True
        left = False
    
    else:
        right = False
        left = False
        walk_Count = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walk_Count = 0
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

    redraw_Game_Window()

pygame.quit()
