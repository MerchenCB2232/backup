# Conditional
print ("Welcome to Ticket Bot")
print ("You must be at least 18 to see R rated movies")
age = int(input("How old are you?"))

if age > 17:
	print ("You can see R rated movies")
else:
	print ("You are not old enough to see R rated movies")

print ("Thank you")

mysteryNum = 6
guess = int(input("Guess a number between 1 and 10: "))
if guess == mysteryNum:
	print ("Good job!")
elif guess < mysteryNum:
	print("Too low!")
elif guess > 10:
		print("Please read directions")
else:
	print ("Too high!")

#conditional operators: >, <, >=, <=, ==, !=

birthday = input("Is today your birthday?(yes/no): ")
if birthday == "yes":
	print("Happy birthday!")
elif birthday == "no":
	print ("Have a good day anyway")
else:
	print("Please read directions")

