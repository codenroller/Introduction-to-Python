"""
    Program: sketchbook.py

    Description: A simple sketch book. By using 'Up', 'Down', 'Right', and 'Left' keys 
        the user can draw a simple sketches
    Keys:
        'Up' key - move turtle forward
        'Down' key - undo the last turtle action
        'Right' key - turn turtle 90 degrees right
        'Left' key - turn turtle 90 degrees left
        'u' key - take pen up from the paper 
            (if you want to move turtle without drawih anything)
        'd' key - put the pen down on the paper
            (if you want to start drawing again)
        'c' key - clear the drawing
        'h' key - place turtle to the initial (0,0) position
    
"""

import turtle

def main():
    # create a turtle instance
    t = turtle.Turtle()
    
    # set turtle parameters
    t.width(2)
    t.speed(0)
    t.pencolor("blue")
    
    # capture program screen
    s = turtle.Screen()
    
    # Events
    s.onkey(t.up, "u") # pen up when 'u' button pressed
    s.onkey(t.down, "d") # pen down when 'd' button pressed
    s.onkey(t.clear, "c") # clear turtle drawing when "c" button pressed
    s.onkey(t.home, "h") # place turtle to home position (0,0)
    
    s.onkey(lambda: t.forward(5), "Up") # when 'Up' key pressed move turtle 5 steps forward 
    s.onkey(lambda: t.undo(), "Down") # when 'Down' key pressed undo last turtle action
    s.onkey(lambda: t.right(5), "Right") # when 'Right' key pressed move turtle 5 degrees to the right 
    s.onkey(lambda: t.left(5), "Left") # when 'Left' key pressed move turtle 5 degrees to the left
    
    s.listen() # start listening to events
    
    return "Done!"


if __name__=='__main__':
    msg = main()
    print(msg)
    turtle.Screen().mainloop()