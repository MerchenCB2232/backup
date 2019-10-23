import random

mysteryNum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Guess a number between 1 and 100: "))
	score += 1 # the same as score = score + 1
	if guess == mysteryNum:
		print ("You guessed correctly. nice work BUD")
		break
	elif guess > mysteryNum:
		print ("Too high")
	else:
		print ("Too low")
print ("You took " + str(score) + " guesses.")