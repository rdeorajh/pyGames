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
        self.win.fill((255,255,255))

def collision(snakeWinObj,snakeObj):
    collide = False
    xHead = snakeObj.X[0]
    yHead = snakeObj.Y[0]
    #Collision with itself
    for i in range(1, snakeObj.tailSize):
        if xHead == snakeObj.X[i] and yHead == snakeObj.Y[i]:
            #print("Collision!!!!!!")
            collide = True
    return collide

def eatFoodCheck(foodObj,snakeObj):
    eatFood = False
    xHead = snakeObj.X[0]
    yHead = snakeObj.Y[0]
    
    if xHead == foodObj.xFood and yHead == foodObj.yFood:
        #print("Food!")
        eatFood = True
    
    return eatFood


#Game Variables
crash = False
score = 0
scrWidth = 800
scrHeight = 600
delayStep = 10
blockSize = 20
snakeLenInc = 5
foodHitbox = False


snakeWin = windowObject(scrWidth,scrHeight)
snakeWin.drawWindow()
while run:
    clock.tick(60)

    #On Startup
    delayTime = 150
    snake1 = snake(scrWidth/2,scrHeight/2,blockSize)
    snake1.updateSnakeSize(snakeLenInc)
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

        crash = collision(snakeWin,snake1)

        if eatFoodCheck(food,snake1):
            score += 10
            #print(score)
            snake1.updateSnakeSize(snakeLenInc)
            food.newFoodPos(snake1,snakeWin)
            if delayTime > 50:
                delayTime -= delayStep
            elif delayTime > 0:
                delayTime -= delayStep//2
            print(delayTime) 

        #Draw
        snakeWin.drawWindow()
        snake1.draw(snakeWin)
        food.drawFood(snakeWin,foodHitbox)
        pygame.display.update()
        
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