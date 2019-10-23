# Cameron Merchen 
# Rock Paper Scissors
# rps.py
# added comment for github
import random
#Variables
pScore = 0
cScore = 0
tie = 0
cMoves = ["rock", "paper", "scissors"]
# Welcome message (Done)
# Print a welcome message
print("Welcome to Rock, Paper and Scissors!")
# Prompt for name
pName = input("What is your name?: ")

# Score Tracker (done)
# Make a function
def printScore():

# Prints score:
	print("Score: ") 
# Shows player score
	print (pName + ": " + str(pScore))
# Shows cpu score
	print ("Computer Score: " + str(cScore))
# Shows number of ties
	print ("Ties: " + str(tie))

# Game loop
# Loop until q is entered
while True:
# prompt player move (r, p, s, q)
	pMove = input("Enter 'r' for rock, 'p' for paper, 's' for scissors and 'q' for quit: ")
# check if q is entered if so end game
	if pMove == "q":
		break
# get a computer move (random)
	cMove = random.choice(cMoves)
# compare player move with computer move
# player picks rock
	if pMove == "r":
		print (pName + " picked Rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print ("Tie")
			tie += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print ("Paper covers Rock")
			cScore += 1
		else:
			print ("Computer picks Scissors")
			print ("Rock breaks Scissors")
			pScore += 1
# prints score
		printScore()
# player picks paper
	elif pMove == "p":
		print (pName + " picked Paper")
		if cMove == "rock":
			print("Computer picks Rock")
			print ("Paper covers Rock")
			pScore += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print ("Tie")
			tie += 1
		else:
			print ("Computer picks Scissors")
			print ("Scissors cuts Paper")
			cScore += 1
# prints score
		printScore()
# player picks scissors
	elif pMove == "s":
		print (pName + " picked Scissors")
		if cMove == "rock":
			print("Computer picks Rock")
			print ("Rock breaks Scissors")
			cScore += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print ("Scissors cuts Paper")
			pScore += 1
		else:
			print ("Computer picks Scissors")
			print ("Tie")
			tie += 1
# prints score		
		printScore()
# check is pMove is valid
	else:
		print("That is not an option.")