import pygame
import numpy as np

pygame.init()
clock = pygame.time.Clock()
run = True #for main game loop

class windowObject(object):
    def __init__(self,screenWidth,screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.win = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption("Conway's Game of Life")
    def drawWindow(self):
        self.win.fill((255,255,255))


#Global Variables
scrWidth = 1280
scrHeight = 720


lifeWin = windowObject(scrWidth, scrHeight)
lifeWin.drawWindow()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    lifeWin.drawWindow()
    pygame.display.update()

