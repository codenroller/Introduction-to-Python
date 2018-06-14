"""
Program Name: simplespiro.py

Description: Draws spiro by given parameters: rSmall, rBig, and l
The parameters can be changed in 

Author: Vitalija Alisauskaite
Date: 14.06.2018

"""

import math
import turtle

def xcoord(rSmall, rBig, l, theta):
    """
        Returns x coordinate of spirograph
        rSmall - small circle radius
        rBig - big circle radius
        l - PC/rBig ratio
        theta - angle between PC and X-axis in radians
    """
    k = rSmall / rBig
    v1 = (1-k) * math.cos(theta)
    v2 = l * k * math.cos( theta * (1/k - 1) )
    return rBig * (v1 + v2) 

def ycoord(rSmall, rBig, l, theta):
    """
        Returns x coordinate of spirograph
        rSmall - small circle radius
        rBig - big circle radius
        l - PC/rBig ratio
        theta - angle between PC and X-axis in radians
    """
    k = rSmall / rBig
    v1 = (1-k) * math.sin(theta)
    v2 = l * k * math.sin( theta * (1/k - 1) )
    return rBig * (v1 - v2)

def drawSpiro(rSmall, rBig, l, xc=0, yc=0):
    """
        Draws a spiro using parameters:
            rSmall - small radius
            rBig - big radius
            l - PC / r
    """
    # environment settings
    painter = turtle.Turtle() # turtle instance
    
    # turtle-painter settings
    painter.shape("turtle")
    painter.color("limegreen")
    painter.width(2)
    
    # number of revolutions required
    n = rSmall // math.gcd(rSmall, rBig) 
    
    # move turtle to spiro starting position
    painter.pu()
    x0 = xc + xcoord(rSmall, rBig, l, 0)
    y0 = yc + ycoord(rSmall, rBig, l, 0)
    painter.setposition(x0, y0)
    painter.pd()
    
    # draw a spiro
    for alpha in range(0, 360 * n + 1):
        theta = alpha * math.pi / 180
        x = xc + xcoord(rSmall, rBig, l, theta)
        y = yc + ycoord(rSmall, rBig, l, theta)
        painter.goto(x,y)

    painter.pu()
    painter.ht()
    

def main():
    # spiro parameters
    rSmall = 65
    rBig = 220
    l = 0.8
    xc = 0
    yc = 0
    
    # draw spiro
    drawSpiro(rSmall, rBig, l, xc, yc)
    
    # preventing program window from closing automatically
    screen = turtle.Screen() # screen instance
    screen.mainloop()
    
if __name__=='__main__':
    main()

    