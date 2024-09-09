#Nicolas Tellez nrt56
#Purpose: This files class serves as a Parent class for other objects to be derived from



#Drawable Class
from abc import ABC, abstractmethod
'''
This class is a parent class that has x,y,visibility, and collision methods
'''
class Drawable(ABC):
    
    '''Constructor method that sets attributes for x,y, and visible '''
    def __init__(self,x=0,y=0,visible = True):
        self.__x = x
        self.__y = y
        self.__visible = visible
        
    ''' method that gets the x and y location'''
    def getLoc(self):
        return (self.__x, self.__y)
    ''' method that sets the x and y location'''   
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    ''' method that checks if the object is visible, returns boolean'''   
    def isVisible(self):
        return self.__visible
    
    ''' method that sets the objects to a boolean value'''  
    def setVisible(self,visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False
    ''' draw method required for child classes, draws object'''          
    @abstractmethod
    def draw(self,surface):
        pass
    ''' method required for child classes, gets the object as a rectangle'''
    @abstractmethod
    def get_rect(self):
        pass
    ''' method that sets the X location'''
    def setX(self,x):
        self.__x = x
    ''' method that sets the Y location'''    
    def setY(self,y):
        self.__y = y
        
    ''' method detects if one object collides with another, returns True or False'''
    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and \
            (rect1.x + rect1.width > rect2.x) and \
            (rect1.y < rect2.y + rect2.height) and \
            (rect1.height + rect1.y > rect2.y):
            return True
        return False 

    
