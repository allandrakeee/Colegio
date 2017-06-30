import turtle

def drawSpiral(turtle1, turtle2, maxSide):
    for sideLength in range(1,maxSide+1,5):
        turtle1.forward(sideLength)
        turtle2.forward(sideLength)
        turtle1.right(140)
        turtle2.left(140)


t1 = turtle.Turtle()
t2 = turtle.Turtle()
drawSpiral(t1, t2, 500)
