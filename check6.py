# Cameron Merchen
# Period 6

# Variable Declaration and Assignment
myVariable = "Cameron" # String variable
myNumber = 11 # int variable
myDecimal = 11.7 # float variable

# Make a variable of type String
myStrVar = "Thank you Kanye, very cool!"

# While Loops 
x = 1
while x <= 10:
	print (x)
	x += 1
# challenge: Make a while loop to count down from 100 to 1
y = 100
while y >= 1:
	print(y)
	y -= 1

# String concatenation
# example
string1 = "Joe"
string2 = " Swanson"
print (string1 + string2 + "!")

# Challenge: Make a variable with your favorite movie
# Print "my favorite movie is "
myMov = "John Wick 3"
print ("My favorite movie is " + myMov)
# input
# example
yourName = input("What is your name? ")
print("Hello " + yourName)
# Challenge
# Prompt for favorite song
favSong = input("What is your favorite song? ")
# print "Your favorite song is "
print ("Your favorite song is " + favSong)
# casting changing one type into another
myNum = input("Enter a number: ") #myNum is a string type
myNum = int(myNum) + 10 # myNum is now an int
print("The answer is " + str(myNum))

#Challenge: Ask for 2 numbers, then add them, and print the sum
addedNum = 0
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
addedNum = num1 + num2
print("The sum of your numbers is " + str(addedNum))
# if and if/else
# example
num = int(input("What is your number: "))
if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is 100")
else:
	print("Your number is less than 100")
# Challenge: ask if today is your birthday
# if it is, print "Happy Birthday"
birthday = input("Is today your Birthday?(yes/no) ")
if birthday == "yes":
	print("Happy Birthday!")
else:
	print("Have a good day anyways.")


