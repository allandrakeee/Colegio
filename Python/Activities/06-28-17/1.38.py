def drawSquare(t, sideLength):
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(90)

def drawNestedSquare(t):
    for i in range(200, 200-5*10, -5):
        drawSquare(t, i)

import turtle
tt = turtle.Turtle()
drawNestedSquare(tt)
