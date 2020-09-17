from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

if __name__ == '__main__':
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()