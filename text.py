#Nicolas Tellez nrt56
#Purpose: This file has a child class derived from drawable. It creates a text that can be drawn to the screen

from drawable import Drawable
import pygame

'''
This class creates a Text object by using given paramteres of x and y locations and color
to determine where the block is placed and it's color
'''
class Text(Drawable):

    '''Constructor method that sets attributes for x,y, and color'''
    def __init__(self, message="Pygame", x=0, y=0,color=(255,255,255), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)

    ''' draw method required for child classes, draws a rectangle'''
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLoc())
    ''' get_rect method that gets the object as a rectangle'''
    def get_rect(self):
        return self.__surface.get_rect()
    ''' method that sets a message to be displayed'''
    def setMessage(self, message):
        self.__message = message 
