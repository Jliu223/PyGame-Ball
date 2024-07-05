#John Liu, jl4582
#5/14/24
#The paddle class which creates a paddle where the ball can bounce off of

from drawable import Drawable
import pygame

class Paddle(Drawable):
    
    def __init__(self, width, height, color):
        '''
        Purpose: when Paddle is instantiated, create width, height, and color attributes
        and create the surface window 
        Parameters: self, width, height, color
        Return value: None
        '''
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height
        
    def getWidth(self):
        '''
        Purpose: gets the width of the paddle
        Parameters: self
        Return value: self.__width
        Sample call: myPaddle.getWidth()
        '''
        return self.__width
    
    def draw(self, surface):
        '''
        Purpose: draws the paddle on the surface
        Parameters: self, surface
        Return value: None
        Sample call: myPaddle.draw(surface)
        '''
        pygame.draw.rect(surface, self.__color, self.get_rect())
        
    def get_rect(self):
        '''
        Purpose: makes the paddle follow the mouse 
        Parameters: self
        Return value: pygame.Rect(mouseX - self.__width/2, screenHeight - 20 - (self.__height), self.__width, self.__height) (the rectangle (paddle) object)
        Sample call: myPaddle.get_rect()
        '''
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, screenHeight - 20 - (self.__height), self.__width, self.__height)