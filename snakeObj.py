import pygame
class snake(object):
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = 10
        self.vel = 1
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.tailSize = 0
        self.X = [x]
        self.Y = [y]
        
    
    
    def updateSnake(self):
        self.tailSize += 1
        self.X.append(self.x)
        self.Y.append(self.y)
        print(self.tailSize)
        print(self.X)
        print(self.Y)


    def updatePos(self,keyDict,winObj):
        #Remember last key pressed
        
        self.X[self.tailSize] = self.X[0]
        self.Y[self.tailSize] = self.Y[0]

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

        if self.left and self.X[0] > 0:
            self.X[0] -= self.vel
        if self.right and self.X[0] + self.width < winObj.screenWidth:
            self.X[0] += self.vel
        if self.up and self.Y[0] > 0:
            self.Y[0] -= self.vel
        if self.down and self.Y[0] + self.height < winObj.screenHeight:
            self.Y[0] += self.vel
        
        

    def draw(self,winObj):
        #For now, draw on screen center
        #print(self.prevX[self.tailSize], self.x)
        #print(self.prevY[self.tailSize], self.y)
        #pygame.draw.rect(winObj.win, (255,255,255), (self.x,self.y, self.width, self.height))
        pygame.draw.rect(winObj.win, (255,255,255), (self.X[0],self.Y[0], self.width, self.height))
        pygame.draw.rect(winObj.win, (255,255,255), (self.X[self.tailSize],self.Y[self.tailSize],self.width,self.height))
        pygame.draw.rect(winObj.win, (255,255,255), (0,0,self.width,self.height))