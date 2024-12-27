# 24 - 12 - 2024

import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Sixth Tutorial - Enemy")

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
        self.standing = True

    def draw(self, win):
        if self.walk_Count + 1 >= 27:
            self.walk_Count = 27

        if not(self.standing):
            if self.left:
                win.blit(char_Walk_Left[self.walk_Count//3], (self.x, self.y))
                self.walk_Count = self.walk_Count + 1
            elif self.right:
                win.blit(char_Walk_Right[self.walk_Count//3], (self.x, self.y))
                self.walk_Count = self.walk_Count + 1
        else:
            # win.blit(char, (self.x, self.y))
            if self.right:
                win.blit(char_Walk_Right[0], (self.x, self.y))
            else:
                win.blit(char_Walk_Left[0], (self.x, self.y))


class enemey(object):
    enemey_Walk_Right = [pygame.image.load('imgs/Character_2/R1E.png'),
                   pygame.image.load('imgs/Character_2/R2E.png'),
                   pygame.image.load('imgs/Character_2/R3E.png'),
                   pygame.image.load('imgs/Character_2/R4E.png'),
                   pygame.image.load('imgs/Character_2/R5E.png'),
                   pygame.image.load('imgs/Character_2/R6E.png'),
                   pygame.image.load('imgs/Character_2/R7E.png'),
                   pygame.image.load('imgs/Character_2/R8E.png'),
                   pygame.image.load('imgs/Character_2/R9E.png'),
                   pygame.image.load('imgs/Character_2/R10E.png'),
                   pygame.image.load('imgs/Character_2/R11E.png')]

    enemey_Walk_Left = [pygame.image.load('imgs/Character_2/L1E.png'),
                   pygame.image.load('imgs/Character_2/L2E.png'),
                   pygame.image.load('imgs/Character_2/L3E.png'),
                   pygame.image.load('imgs/Character_2/L4E.png'),
                   pygame.image.load('imgs/Character_2/L5E.png'),
                   pygame.image.load('imgs/Character_2/L6E.png'),
                   pygame.image.load('imgs/Character_2/L7E.png'),
                   pygame.image.load('imgs/Character_2/L8E.png'),
                   pygame.image.load('imgs/Character_2/L9E.png'),
                   pygame.image.load('imgs/Character_2/L10E.png'),
                   pygame.image.load('imgs/Character_2/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_Count = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walk_Count + 1 >= 33:
            self.walk_Count = 0
        
        if self.vel > 0:
            win.blit(self.enemey_Walk_Right[self.walk_Count // 3], (self.x, self.y))
            self.walk_Count = self.walk_Count + 1
        else:
            win.blit(self.enemey_Walk_Left[self.walk_Count // 3], (self.x, self.y))
            self.walk_Count = self.walk_Count + 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x = self.x + self.vel
            else:
                self.vel = self.vel * -1
                self.walk_Count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x = self.x + self.vel
            else:
                self.vel = self.vel * -1 
                self.walk_Count = 0


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing 

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redraw_Game_Window():
    win.blit(background, (0, 0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

man = player(200, 410, 64, 64)
goblin = enemey(100, 410, 64, 64, 450)
bullets = []
run = True
while run:
    clock.tick(27)

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x = bullet.x + bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x = man.x - man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < (500 - man.width - man.vel):
        man.x = man.x + man.vel
        man.right = True
        man.left = False
        man.standing = False
    
    else:
        # man.right = False
        # man.left = False
        man.standing = True
        man.walk_Count = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
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
