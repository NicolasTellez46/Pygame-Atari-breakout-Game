#Nicolas Tellez nrt56
#Purpose: This files class is used as a ball in the main code, it has the ability to bounce and change speeds 
from drawable import *
import pygame

''' This child class inherits from the Drawable class and draws and takes all the required information for a ball
    It can move around, change speeds, and be detected in collisions.
'''
class Ball(Drawable):

    '''Constructor method that sets attributes for x,y,color,radius,xSpeed,and ySpeed'''
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 0.1
        self.__ySpeed = 0.1

    ''' draw method required for child classes, draws circle'''
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
    ''' move method which moves the object based on its x and y speeds'''
    def move(self):
        currentX = self.getLoc()[0]
        currentY = self.getLoc()[1]
        newX = currentX+self.__xSpeed
        newY = currentY+self.__ySpeed
        self.setX(newX)
        self.setY(newY)
    
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed*=-1
            
        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1
            
    ''' get_rect method which gets the balls rectangle'''       
    def get_rect(self):
        loc = self.getLoc()
        radius = self.__radius
        return pygame.Rect(loc[0]-radius,loc[1]-radius, 2*radius,2*radius)
    ''' method which sets the balls X Speed to a value'''
    def setXSpeed(self,speed):
        self.__xSpeed = speed
    ''' method which gets the balls X Speed'''
    def getXSpeed(self):
        return self.__xSpeed
    ''' method which sets the balls Y Speed to a value'''
    def setYSpeed(self,speed):
        self.__ySpeed = speed
    ''' method which gets the balls Y Speed'''
    def getYSpeed(self):
        return self.__ySpeed
        
      