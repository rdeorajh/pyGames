import pygame
from snakeObj import *
pygame.init()
clock = pygame.time.Clock()
run = True

class windowObject(object):
    def __init__(self,screenWidth,screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.win = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("Snaaaake")
    
    def drawWindow(self):
        self.win.fill((0,0,0))

def collision(snakeWinObj,snakeObj):
    collide = False
    
    xHead = snakeObj.X[0]
    yHead = snakeObj.Y[0]

    #Collision with itself
    for i in range(2, snakeObj.tailSize):
        if xHead == snakeObj.X[i] and yHead == snakeObj.Y[i]:
            print("Collision!!!!!!")
            collide = True

    return collide



snakeWin = windowObject(640,480)
snakeWin.drawWindow()
snake1 = snake(640/2,480/2,20)
snake1.updateSnakeSize(20)
snake1.left = True #Get rid of this later
snake1.draw(snakeWin)

snakeWin = windowObject(640,480)
snakeWin.drawWindow()
delayTime = 150
crash = False

while run:
    clock.tick(60)

    #On Startup
    snake1 = snake(640/2,480/2,20)
    snake1.updateSnakeSize(20)
    snake1.left = True #Get rid of this later
    snake1.draw(snakeWin)

    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    

        keys = pygame.key.get_pressed()
        snake1.updateHeadPos(keys,snakeWin)

        #Draw
        snakeWin.drawWindow()
        snake1.draw(snakeWin)
        pygame.display.update()

        crash = collision(snakeWin,snake1)

        #DelayTimer
        pygame.time.delay(delayTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        crash = False
        del snake1

pygame.quit()