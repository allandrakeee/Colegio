def drawRectangle(myTurtle, width, height):
    for i in range(2):
        myTurtle.forward(width) #side 1 
        myTurtle.right(90)
        myTurtle.forward(height) #side 2
        myTurtle.right(90)

import turtle
t = turtle.Turtle()
drawRectangle(t, 180, 80)
