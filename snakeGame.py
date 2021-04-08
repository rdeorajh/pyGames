import pygame
from snakeObj import *
from snakeFoodObj import *

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
    for i in range(1, snakeObj.tailSize):
        if xHead == snakeObj.X[i] and yHead == snakeObj.Y[i]:
            print("Collision!!!!!!")
            collide = True
    return collide

def eatFoodCheck(foodObj,snakeObj):
    pass


#Game Variables
crash = False
scrWidth = 800
scrHeight = 600
delayTime = 150
blockSize = 20
snakeLenInc = 5
foodHitbox = True


snakeWin = windowObject(scrWidth,scrHeight)
snakeWin.drawWindow()
while run:
    clock.tick(60)

    #On Startup
    snake1 = snake(scrWidth/2,scrHeight/2,blockSize)
    snake1.updateSnakeSize(20)
    snake1.left = True #Get rid of this later
    food = snakeFood(blockSize,snakeWin)
    food.newFoodPos(snake1,snakeWin)
    
    food.drawFood(snakeWin, foodHitbox)
    snake1.draw(snakeWin) 

    #Main Game Loop
    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                crash = False
                break

        keys = pygame.key.get_pressed()
        snake1.updateHeadPos(keys,snakeWin)

        #Draw
        snakeWin.drawWindow()
        snake1.draw(snakeWin)
        food.drawFood(snakeWin,foodHitbox)
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