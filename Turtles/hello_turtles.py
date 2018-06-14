"""
    Program: hello_turtles.py
    
    Description: The program creates a turtle, 
    sets turtle properties, and paints three squares 
    using different color and line width
    
"""
import turtle

def main():
    # create a turtle object
    t = turtle.Turtle()
    
    # capture program screen instance
    s = turtle.Screen()
    # set screen size to be 400 x 300 pixels
    s.screensize(450, 350)
    
    # set turtle shape and size
    t.shape("turtle")
    t.shapesize(2,2,1)
    
    # tell turtle to put the pen down on the paper
    t.pd()
    
    # drawing the first square 100 x 100
    t.forward(100) # turtle moves 100 steps forward
    t.left(90) # turtle turns 90 degrees to the left
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    
    
    # tell turtle to put the pen off the paper
    t.pu()
    
    # drawing the second square 150 x 150; color -> limegreen; line width -> 2
    
    # modifying the turtle
    t.color("limegreen") # setting color
    t.width(2) # setting line width
    
    # tell turtle to put the pen down on the paper
    t.pd()
    
    # drawing the second square 150 x 150
    t.forward(150) # turtle moves 150 steps forward
    t.left(90) # turtle turns 90 degrees left
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    
    # tell turtle to put the pen off the paper
    t.pu()

    
    # drawing the third square 200 x 200; color -> orange; line width -> 5
    
    # modifying the turtle
    t.color("orange") # setting color
    t.width(5) # setting line width
    
    # tell turtle to put the pen down on the paper
    t.pd()
    
    # drawing the second square 150 x 150
    t.forward(200) # turtle moves 200 steps forward
    t.left(90) # turtle turns 90 degrees left
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    
    # tell turtle to put the pen off the paper
    t.pu()
    
    # hide turtle after it finished to draw
    t.ht()
    
    # prevent program window from closing automatically
    s.mainloop()

      
    
if __name__=='__main__':
    main()

