#John Liu, jl4582
#5/14/24
#The drawable abstract base class that paddle, ball, and text will derive from

from abc import ABC, abstractmethod

class Drawable(ABC):
    
    def __init__(self, x=0, y=0):
        '''
        Purpose: when instantiating the drawable class, create the attributes for x and y and an additional one for visibility (visible)
        Parameters: self, x, y
        Return value: None
        '''
        self.__visible = True
        self.__x = x
        self.__y = y
  
    @abstractmethod
    def draw(self, surface):
        '''
        Purpose: create an abstract method draw so that other classes that derive from Drawable are required to have this method
        Parameters: self, surface
        Return value: None
        '''
        pass
        
    @abstractmethod
    def get_rect(self):
        '''
        Purpose: create an abstract method get_rect so that other classes that derive from Drawable are required to have this method
        Parameters: self
        Return value: None
        '''
        pass
    
    def getLoc(self):
        '''
        Purpose: gets the location of the object and returns a tuple (x, y)
        Parameters: self
        Return value: (self.__x, self.__y)
        Sample call: self.getLoc()
        '''
        return (self.__x, self.__y)
    
    def getX(self):
        '''
        Purpose: gets the x coordinate of the object
        Parameters: self
        Return value: self.__x
        Sample call: myBall.getX()
        '''
        return self.__x
    def getY(self):
        '''
        Purpose: gets the y coordinate of the object
        Parameters: self
        Return value: self.__y
        Sample call: myBall.getY()
        '''
        return self.__y
    
    def setX(self, x):
        '''
        Purpose: changes the x coordinate of the object
        Parameters: self, x
        Return value: None
        Sample call: myBall.setX(3)
        '''
        self.__x = x
        
    def setY(self, y):
        '''
        Purpose: changes the y coordinate of the object
        Parameters: self, y
        Return value: None
        Sample call: myBall.setY(3)
        '''
        self.__y = y
        
    def isVisible(self):
        '''
        Purpose: checks whether the object is visible
        Parameters: self
        Return value: self.__visible (boolean)
        Sample call: myBall.isVisible()
        '''
        return self.__visible
    
    def setVisible(self, visible):
        '''
        Purpose: user can set the visibility of the object
        Parameters: self, visible
        Return value: None
        Sample call: myBall.setVisible(True)
        '''
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False
        
    def intersects(self, other):
        '''
        Purpose: checks whether two rectangles intersect
        Parameters: self, other
        Return value: True or False
        Sample call: myBall.intersects(myPaddle)
        '''
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
            return True
        return False
        
    