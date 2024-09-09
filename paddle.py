#Nicolas Tellez nrt56
#Purpose: This file has a child class dervied from drawable. It creates a moveable paddle to be used in the main file.
from drawable import Drawable
import pygame


'''
This class creates a paddle and it's size and color can be changed. The paddle is also moveable
and responds to the players cursor location.
'''
class Paddle(Drawable):
    
    '''Constructor method that sets attributes for x,y,width,height, and color'''
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height

    ''' draw method required for child classes, draws a rectangle'''
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())

    ''' get_rect method that gets the object as a rectangle'''
    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, screenHeight - 20 - (self.__height), self.__width, self.__height) 
