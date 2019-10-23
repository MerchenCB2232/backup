from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()

myTurtle.forward(100)

def writename():
	name = screen.textinput("name box", "What is your name?")
	myTurtle.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()

screen.onkey(writename, "w") 

screen.listen()

screen.mainloop()