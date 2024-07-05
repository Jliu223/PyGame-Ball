#John Liu, jl4582
#5/14/24
#The ball class, which creates a ball that can change direction when it hits the surface window 

from drawable import Drawable
import pygame
import math

class Ball(Drawable):

    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        '''
        Purpose: when Ball is instantiated, create attributes for x, y, radius, and color
        Also include the speed in x and y 
        Parameters: self, x, y, radius, color
        Return value: None
        '''
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 1
        self.__ySpeed = 1

    def draw(self, surface):
        '''
        Purpose: if the ball is visible, draw the circle on the surface with the specified color, location, and radius
        Parameters: self, surface
        Return value: None
        Sample call: myBall.draw(surface)
        '''
        if self.isVisible(): 
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
    
    def move(self):
        '''
        Purpose: updates the ball's position which has a certain speed. If the ball hits
        the surface window, the speed is negated and goes in the other direction 
        Parameters: self
        Return value: None
        Sample Call: myBall.move()
        '''
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)
        
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1
        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1
    
    def get_rect(self):
        '''
        Purpose: creates a rectangle around the ball
        Parameters: self
        Return value: pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)
        Sample call: myBall.get_rect()
        '''
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)
    
    def getColor(self):
        '''
        Purpose: gets the ball's color
        Parameters: self
        Return value: self.__color
        Sample Call: myBall.getColor()
        '''
        return self.__color
    def setColor(self, color):
        '''
        Purpose: changes the ball's color
        Parameters: self, color
        Return value: None
        Sample Call: myBall.setColor((255,0,0))
        '''
        self.__color = color
    def getRadius(self):
        '''
        Purpose: gets the ball's radius
        Parameters: self
        Return value: self.__radius
        Sample Call: myBall.getRadius()
        '''
        return self.__radius
    def setRadius(self, radius):
        '''
        Purpose: changes the ball's radius
        Parameters: self, radius
        Return value: None
        Sample call: myBall.setRadius(20)
        '''
        self.__radius = radius
    def setXSpeed(self, speed):
        '''
        Purpose: changes the ball's speed in x
        Parameters: self, speed
        Return value: None
        Sample Call: myBall.setXSpeed(20)
        '''
        self.__xSpeed = speed
    def getXSpeed(self):
        '''
        Purpose: gets the ball's speed in x
        Parameters: self
        Return value: self.__xSpeed
        Sample call: myBall.getXSpeed()
        '''
        return self.__xSpeed
    def setYSpeed(self, speed):
        '''
        Purpose: changes the ball's speed in y
        Parameters: self, speed
        Return value: None
        Sample call: myBall.setYSpeed(20)
        '''
        self.__ySpeed = speed
    def getYSpeed(self):
        '''
        Purpose: gets the ball's speed in y 
        Parameters: self
        Return value: self.__ySpeed
        Sample call: myBall.getYSpeed()
        '''
        return self.__ySpeed