#Nicolas Tellez nrt56
#Purpose: This file has a child class dervied from drawable. It creates blocks used in the main file.
from drawable import Drawable
import pygame


'''
This class creates a block object by using given paramteres of x and y locations, width and height, and color
to determine where the block is placed, it's size, and it's color
'''
class Block(Drawable):
    
    '''Constructor method that sets attributes for x,y,width,height, and color'''
    def __init__(self,x, y, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(x,y)
        self.__color = color
        self.__width = width
        self.__height = height
    
    ''' draw method required for child classes, draws a rectangle'''
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())

    ''' get_rect method that gets the object as a rectangle'''
    def get_rect(self):
        return pygame.Rect((self.getLoc()[0],self.getLoc()[1],self.__width,self.__height))
        
        