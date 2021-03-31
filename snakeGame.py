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
        





snakeWin = windowObject(640,480)
snakeWin.drawWindow()
snake1 = snake(640/2,480/2,10)
snake1.updateSnake()
snake1.draw(snakeWin)
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    snake1.updatePos(keys,snakeWin)



    #Draw
    snakeWin.drawWindow()
    snake1.draw(snakeWin)
    pygame.display.update()


pygame.quit()