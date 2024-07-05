#John Liu, jl4582
#5/14/24
#main pygame file with the ball, paddle, and a score counter 

#import pygame, derived classes, and random
import pygame
from ball import Ball
from paddle import Paddle
from text import Text
import random

#initalize pygame, surface, colors, ball, paddle and scoreboard objects, fps clock, the random circles that will pop up, and the numHit counter
pygame.init()
surface = pygame.display.set_mode((800, 600))
DREXEL_BLUE = (7, 41, 77)
myBall = Ball(400, 300, 25, DREXEL_BLUE)
myPaddle = Paddle(200, 25, DREXEL_BLUE)
myScoreBoard = Text("Score: 0", 10, 10)
running = True
fpsClock = pygame.time.Clock()
randomCircles = [(random.randint(50, 700), random.randint(50, 500), random.randint(10, 50)) for i in range(7)]
new_background_color = (255, 0, 0)
numHits = 0

#main game loop
while running:
    surface.fill((255, 255, 255))
    #iterate through the list and draw each circle 
    for circle in randomCircles:
        pygame.draw.circle(surface, (255, 0, 0), (circle[0], circle[1]), circle[2])
    #draw the ball, paddle, and score 
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreBoard.draw(surface)
    #if the ball hits the paddle, +1 point
    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed()*-1)
        numHits += 1
        myScoreBoard.setMessage("Score: " + str(numHits))
    #lose one point for colliding with the circles. Circle disappears afterwards
    for circle in randomCircles:
        circleX, circleY, circleRadius = circle
        if myBall.intersects(Ball(circleX, circleY, circleRadius, (255, 0, 0))):
            numHits -= 1
            myScoreBoard.setMessage("Score: " + str(numHits))
            new_color = new_background_color
            surface.fill(new_color)
            randomCircles.remove(circle)

    # ends when the balls hit the ground, and you win if you get 5 points from hitting the ball off the paddle 
    if myBall.getY() + myBall.getRadius() >= surface.get_height():
        print("You Lose!")
        running = False
    if numHits == 5:
        print("You Win!")
        running = False
    myBall.move()
    
    #quits if the user closes the program and changes the visibility of the ball if the user clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            myBall.setVisible(not myBall.isVisible())
        
    pygame.display.update()
    fpsClock.tick(120)
exit()

