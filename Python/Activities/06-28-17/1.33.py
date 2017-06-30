def drawSpiral(t, maxSide):
    for sideLength in range(1, maxSide+1, 5):
        t.forward(sideLength)
        t.right(140)
        
import turtle
t = turtle.Turtle()
drawSpiral(t, 500)
