"""
Program Name: circle.py

Description: Draws circle of a given radius using Python turtles

Author: Vitalija Alisauskaite
Date: 14.06.2018

"""

import math
import turtle

def coordX(r, theta, useradians = True):
    """
        (float, float, boolean) -> (float)
        r - radius, positive number
        theta - angle in degrees or in radians
        useradians - boolean, if useradians is equal to True
            the function will assume that you are providing angle theta in radians,
            if useradians is False, then the angle has to be provided in degrees

        Function returns the coordinate x = f1(r, theta) = r * cos(theta)
    """
    if not useradians :
        #convert theta to radians
        theta = theta / 180 * math.pi
    x = r * math.cos(theta)
    return x


def coordY(r, theta, useradians = True):
    """
        (float, float, boolean) -> (float)
        r - radius, positive number
        theta - angle in degrees or in radians
        useradians - boolean, if useradians is equal to True
            the function will assume that you are providing angle theta in radians,
            if useradians is False, then the angle has to be provided in degrees

        Function returns the coordinate y = f2(r, theta) = r * sin(theta)
    """
    if not useradians :
        #convert theta to radians
        theta = theta / 180 * math.pi
    y = r * math.sin(theta)
    return y


def drawCircle(r):
    """
        (float) -> ()
        Draws a circle of a given radius r
    """
    # create a turtle-painter instance using turtle library
    painter = turtle.Turtle()

    # turtle properties (we want the turtle to look nicer)
    painter.shape("turtle") # setting painter shape to turtle
    painter.shapesize(3,3,1) # making turtle-painter 3 times bigger
    painter.color("limegreen") # setting painting color to limegreen

    # move the turtle-painter to ready position
    painter.pu() # we just move without drawing anything
    x0 = coordX(r, 0) # compute initial coordinate x0
    y0 = coordY(r, 0) # compute initial coordinate y0

    painter.goto(x0,y0) # move the turtle to the ready position
    
    # tell the turtle to put pencil down on the paper
    painter.pd()

    # draw a circle
    for theta in range(0, 361, 1):
        x = coordX(r, theta, useradians = False)
        y = coordY(r, theta, useradians = False)

        painter.goto(x,y)

    # tell the turtle to put pencil up from the paper
    painter.pu()
    # hide the painter after he finished to draw
    painter.ht()
    print("Draw a circle of r = ", r )


def main():
    drawCircle(100)


if __name__ == '__main__':
    main()

        
        

    






    


