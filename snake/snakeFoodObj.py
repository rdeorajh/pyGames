import pygame
from random import *

class snakeFood(object):
    def __init__(self, foodWidth, winObj):
        #Creates coordinates
        self.xFood = randint(0, winObj.screenWidth)
        self.yFood = randint(0, winObj.screenHeight)
        self.foodWidth = foodWidth
        self.foodHeight = foodWidth

    def newFoodPos(self,snakeObj,winObj):
        validFood = False
        while not validFood:
            self.xFood = (randint(0,winObj.screenWidth) // snakeObj.vel) * snakeObj.vel
            self.yFood = (randint(0,winObj.screenHeight) // snakeObj.vel) * snakeObj.vel
            validFood = True

            #Check if food spawned on Snake Body
            for i in range(1,snakeObj.tailSize):
                if self.xFood == snakeObj.X[i] and self.yFood == snakeObj.Y[i]:
                    validFood = False
        


    def drawFood(self,winObj,rectBool):
        #Set Boolean to draw boundary

        xFoodPos = (self.xFood + (self.foodWidth * 0.8)/2) 
        yFoodPos = (self.yFood + (self.foodHeight * 0.8)/2)
        rad = (self.foodWidth * 0.8)/2

        if rectBool:
            pygame.draw.rect(winObj.win, (200,200,200), (self.xFood, self.yFood, self.foodWidth * 0.8, self.foodHeight * 0.8))
        pygame.draw.circle(winObj.win, (255,0,0), (xFoodPos,yFoodPos),rad)

