# Cameron Merchen
# Period 6
# Dice Rolling Simulator
import random 
x = 1
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
def printRolls():
	percRolls1 = (one / rolls)*100
	percRolls2 = (two / rolls)*100  
	percRolls3 = (three / rolls)*100
	percRolls4 = (four / rolls)*100
	percRolls5 = (five / rolls)*100
	percRolls6 = (six / rolls)*100
	print ("You have rolled the dice " + str(rolls) + " times.")
	print ("You have rolled a one " + str(one) + " times")
	print ("You have rolled a two " + str(two) + " times")
	print ("You have rolled a three " + str(three) + " times")
	print ("You have rolled a four " + str(four) + " times")
	print ("You have rolled a five " + str(five) + " times")
	print ("You have rolled a six " + str(six) + " times")
	print ("A one has been rolled " + str(percRolls1) + " percent of the time")
	print ("A two has been rolled " + str(percRolls2) + " percent of the time")
	print ("A three has been rolled " + str(percRolls3) + " percent of the time")
	print ("A four has been rolled " + str(percRolls4) + " percent of the time")
	print ("A five has been rolled " + str(percRolls5) + " percent of the time")
	print ("A six has been rolled " + str(percRolls6) + " percent of the time")
rolls = int(input("Enter the number of times the dice will roll: "))
while x <= rolls:
	randomNum = random.randint(1,6)
	if randomNum == 1:
		one += 1
		print ("Roll number " + str(x) + " result: 1")
	elif randomNum == 2:
		two += 1 
		print ("Roll number " + str(x) + " result: 2")
	elif randomNum == 3:
		three += 1 
		print ("Roll number " + str(x) + " result: 3")
	elif randomNum == 4:
		four += 1 
		print ("Roll number " + str(x) + " result: 4")
	elif randomNum == 5:
		five += 1 
		print ("Roll number " + str(x) + " result: 5")
	else:
		six += 1 
		print ("Roll number " + str(x) + " result: 6")
	

	x=x+1

printRolls()

