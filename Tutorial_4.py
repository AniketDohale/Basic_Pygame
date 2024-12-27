# 23 - 12 - 2024

import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Fourth Tutorial - Optimization, OOP")

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

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jump_Count = 10
        self.left = False
        self.right = False
        self.walk_Count = 0

    def draw(self, win):
        if self.walk_Count + 1 >= 27:
            self.walk_Count = 27
    
        if self.left:
            win.blit(char_Walk_Left[self.walk_Count//3], (self.x, self.y))
            self.walk_Count = self.walk_Count + 1
        elif self.right:
            win.blit(char_Walk_Right[self.walk_Count//3], (self.x, self.y))
            self.walk_Count = self.walk_Count + 1
        else:
            win.blit(char, (self.x, self.y))


def redraw_Game_Window():
    win.blit(background, (0, 0))
    man.draw(win)
    pygame.display.update()

man = player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x = man.x - man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < (500 - man.width - man.vel):
        man.x = man.x + man.vel
        man.right = True
        man.left = False
    
    else:
        man.right = False
        man.left = False
        man.walk_Count = 0

    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walk_Count = 0.
    else:
        if man.jump_Count >= - 10:
            neg = 1
            if man.jump_Count < 0:
                neg = -1
            man.y = man.y - (man.jump_Count ** 2) * 0.5 * neg
            man.jump_Count = man.jump_Count - 1
        else:
            man.isJump = False
            man.jump_Count = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw_Game_Window()

pygame.quit()
