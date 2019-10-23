from turtle import *
turtledood=Turtle()
screen=turtledood.getscreen()

def forward():
  turtledood.forward(10)
def left():
  turtledood.left(90)
def right():
  turtledood.right(90)
def back():
  turtledood.back(10)
def penup():
  turtledood.penup()
def pendown():
  turtledood.pendown()
def green():
  turtledood.pencolor("green")
def violet():
  turtledood.pencolor("violet")
def red():
  turtledood.pencolor("red")
def reset():
  turtledood.reset()
def home():
  turtledood.home()
def dot():
  turtledood.dot(15)
def sizeup():
  turtledood.pensize(10)
def sizedown():
  turtledood.pensize(1)

screen.onkey(forward, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(back, "Down")
screen.onkey(green, "1")
screen.onkey(violet, "2")
screen.onkey(red, "3")
screen.onkey(reset, "r")
screen.onkey(home, "h")
screen.onkey(dot, "d")
screen.onkey(sizeup, "U")
screen.onkey(sizedown, "O")
screen.listen()

