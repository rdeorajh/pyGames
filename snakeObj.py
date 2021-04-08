import pygame
class snake(object):
    def __init__(self,x,y,width):
        self.width = width
        self.height = width
        self.vel = 20
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.tailSize = 0
        self.X = [x]
        self.Y = [y]
        
    
    
    def updateSnakeSize(self,updInc):
        self.tailSize += updInc
        for i in range(0,updInc):
            self.X.append(self.X[0])
            self.Y.append(self.Y[0])


    def updateTailPos(self):
        for i in range(self.tailSize, 0, -1):
            self.X[i] = self.X[i-1]
            self.Y[i] = self.Y[i-1]


    def updateHeadPos(self,keyDict,winObj):
        #Remember last key pressed
        #Save Previous Tail sizes

        #Update Tail Pieces
        self.updateTailPos()

        #Direction Check
        if keyDict[pygame.K_LEFT] and self.right == False:
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if keyDict[pygame.K_RIGHT] and self.left == False:
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        if keyDict[pygame.K_UP] and self.down == False:
            self.left = False
            self.right = False
            self.up = True
            self.down = False
        if keyDict[pygame.K_DOWN] and self.up == False:
            self.left = False
            self.right = False
            self.up = False
            self.down = True

        #Increment Head
        if self.left and self.X[0] > 0:
            self.X[0] -= self.vel
        if self.right and self.X[0] + self.width < winObj.screenWidth:
            self.X[0] += self.vel
        if self.up and self.Y[0] > 0:
            self.Y[0] -= self.vel
        if self.down and self.Y[0] + self.height < winObj.screenHeight:
            self.Y[0] += self.vel
        

    def draw(self,winObj):
        #Draw Full snake
        for i in range(0, self.tailSize):
            pygame.draw.rect(winObj.win, (128,128,128), ((self.X[i]-self.width/10),(self.Y[i]-self.height/10), self.width, self.height)) 
            pygame.draw.rect(winObj.win, (255,255,255), (self.X[i], self.Y[i], self.width*0.8, self.height*0.8))
        pygame.draw.rect(winObj.win,(0,128,255),(self.X[0], self.Y[0], self.width*0.8, self.height*0.8))
                       
            