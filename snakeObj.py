import pygame
class snake(object):
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = 10
        self.vel = 0.025
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    
    def updatePos(self,keyDict,winObj):
        #Remember last key pressed
        if keyDict[pygame.K_LEFT]:
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if keyDict[pygame.K_RIGHT]:
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        if keyDict[pygame.K_UP]:
            self.left = False
            self.right = False
            self.up = True
            self.down = False
        if keyDict[pygame.K_DOWN]:
            self.left = False
            self.right = False
            self.up = False
            self.down = True
        
        if self.left and self.x > 0:
            self.x -= self.vel
        if self.right and self.x + self.width < winObj.screenWidth:
            self.x += self.vel
        if self.up and self.y > 0:
            self.y -= self.vel
        if self.down and self.y + self.height < winObj.screenHeight:
            self.y += self.vel

    def draw(self,winObj):
        #For now, draw on screen center
        pygame.draw.rect(winObj.win, (255,255,255), (self.x,self.y, self.width, self.height))
