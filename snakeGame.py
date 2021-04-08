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

def displayTitleText(titleTextString, winObj):
    font = pygame.font.SysFont('Comic Sans MS',75)
    screenSurf = font.render(titleTextString,1,(0,0,0))
    winObj.win.blit(screenSurf,(winObj.screenWidth//8, winObj.screenHeight//4))

    #prompt
    font2 = pygame.font.SysFont('Comic Sans MS',25)
    prompt = font2.render("Press Spacebar to play",1,(0,0,0))
    winObj.win.blit(prompt,(winObj.screenWidth//3, winObj.screenHeight//1.1))

def displayPlayAgainText(winObj, score):
    font = pygame.font.SysFont('Comic Sans MS',75)
    screenSurf = font.render("Play Again?",1,(0,0,0))
    winObj.win.blit(screenSurf,(winObj.screenWidth//3.9, winObj.screenHeight//4))

    if score >=200:
        specFont = pygame.font.SysFont('Comic Sans MS',50,True)
        specRender = specFont.render("You're a snake god.",1,(0,0,0))
        winObj.win.blit(specRender,(winObj.screenWidth//5, winObj.screenHeight//1.75))

    #prompt
    font2 = pygame.font.SysFont('Comic Sans MS',25)
    prompt = font2.render("Press Spacebar to play",1,(0,0,0))
    winObj.win.blit(prompt,(winObj.screenWidth//3, winObj.screenHeight//1.1))

def displayScoreText(score,winObj):
    font = pygame.font.SysFont('Comic Sans MS',15)
    scoreRender = font.render("Score: " + str(score),1,(0,0,0))
    winObj.win.blit(scoreRender,(0,0))

def collision(snakeWinObj,snakeObj):
    collide = False
    xHead = snakeObj.X[0]
    yHead = snakeObj.Y[0]
    #Collision with itself
    for i in range(1, snakeObj.tailSize):
        if xHead == snakeObj.X[i] and yHead == snakeObj.Y[i]:
            collide = True
    return collide

def eatFoodCheck(foodObj,snakeObj):
    eatFood = False
    xHead = snakeObj.X[0]
    yHead = snakeObj.Y[0]
    
    if xHead == foodObj.xFood and yHead == foodObj.yFood:
        eatFood = True
    return eatFood


#Game Variables
crash = True
score = 0
scrWidth = 800
scrHeight = 600
delayStep = 10
blockSize = 20
snakeLenInc = 5
foodHitbox = False

scoreFont = pygame.font.SysFont('Comic Sans MS',30)
scoreFontSurf = scoreFont.render("Some Text", 1, (0,0,0))
#titleFont = pygame.font.SysFont()

snakeWin = windowObject(scrWidth,scrHeight)
snakeWin.drawWindow()
displayTitleText("Snaaaaaaaaaaake", snakeWin)
snake1 = snake(scrWidth/2,scrHeight/2,blockSize)
snake1.draw(snakeWin) 
pygame.display.update()
del snake1
while run:
    clock.tick(60)

    #On Startup
    delayTime = 150
    score = 0
    snake1 = snake(scrWidth/2,scrHeight/2,blockSize)
    snake1.updateSnakeSize(2)
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
            snake1.updateSnakeSize(snakeLenInc)
            food.newFoodPos(snake1,snakeWin)
            if delayTime > 50:
                delayTime -= delayStep
            elif delayTime > 0:
                delayTime -= delayStep//2

        #Draw
        snakeWin.drawWindow()
        snake1.draw(snakeWin)
        food.drawFood(snakeWin,foodHitbox)
        displayScoreText(score,snakeWin)
        pygame.display.update()
        
        if crash:
            displayPlayAgainText(snakeWin, score)
            pygame.display.update()
        #DelayTimer
        pygame.time.delay(delayTime)

    #displayTitleText("Play Again?", snakeWin)
    #pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        crash = False
        del snake1

pygame.quit()