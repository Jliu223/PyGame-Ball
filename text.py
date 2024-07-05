#John Liu, jl4582
#5/14/24
#A text class which draws a message (like the score) onto the surface 

from drawable import Drawable
import pygame

class Text(Drawable):
    def __init__(self, message = "Pygame", x=0, y=0, color = (0,0,0), size = 24):
        '''
        Purpose: when Text is instantiated, create attributes for message, x, y, color and size
        Also include an attribute for the font 
        Parameters: self, message, x, y, color, size
        Return value: None
        '''
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)
        
    def draw(self, surface):
        '''
        Purpose: draws or "blits" the text onto the surface at the specified location  
        Parameters: self, surface
        Return value: None
        Sample call: text.draw(surface)
        '''
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLoc())
    
    def get_rect(self):
        '''
        Purpose: Have a rectangle around the text (like a text box)
        Parameters: self
        Return value: None
        Sample call: text.get_rect()
        '''
        return self.__surface.get_rect()
    
    def setMessage(self, message):
        '''
        Purpose: sets/changes the message that is displayed on the surface 
        Parameters: self, message
        Return value: None
        Sample call: myScoreBoard.setMessage("Score:")
        '''
        self.__message = message 
    