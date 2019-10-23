import random
import time
myWord = "egghead"
count = 0
secretList = list(myWord)
secret = []
missedLetters = []
numMiss = int(input("How many misses till you game over? "))
for a in secretList:
	secret.append("_")
print("Welcome to Hangman! Once you've guessed all the letters, guess the word!")
print (secret)
while True:
	if count == numMiss:
		print("Game Over!")
		break
	else:
		pass
	if secret == myWord:
		print("Congratulations!")
		break
	else:
		pass
	choice2 = input("Enter l to guess a letter, w to guess a word, and q to quit: ")
	if choice2 == "l":
		letter = input("Type a letter (You have 10 seconds!) ")
		time.sleep(10)
		print("You took too long")
		if letter in myWord:
			if letter == "e":
				secret[0] = "e"
				secret[4] = "e"
				print(secret)
				print("You've missed these letters: " + str(missedLetters))
				print("Misses: " + str(count))
			elif letter == "g":
				secret[1] = "g"
				secret[2] = "g"
				print(secret)
				print("Misses: " + str(count))
			elif letter == "h":
				secret[3] = "h"
				print(secret)
				print("Misses: " + str(count))
			elif letter == "a":
				secret[5] = "a"
				print(secret)
				print("Misses: " + str(count))
			else:
				secret[6] = "d"
				print(secret)
				print("Misses: " + str(count))

		else:
			print("Letter is not in word")
			missedLetters.append(letter)
			count += 1
			print("Misses: " + str(count))
			print(missedLetters)
	elif choice2 == "w":
		choice = input("Type a word: ")
		if choice == myWord:
			print("You're correct! Great job!")
			break
		else:
			print("haha that's wrong")
			count += 1
			print("Misses: " + str(count))
	elif choice2 == "q":
		break
	else:
		print("That is not an option")





