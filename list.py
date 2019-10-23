myClasses = ["Algebra", "English", "World History"]
print(myClasses)

# add an item to the list
# append or insert
# append will add to the back of the list
myClasses.append("Physics")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print (myClasses)
# insert
myClasses.insert(3, "Art")
print (myClasses)
# overwrite
myClasses[4] = "Science"
print (myClasses)
# remove list items
# remove, pop
# remove will remove specific item
myClasses.remove("Science")
print(myClasses)
# pop will remove the item at a specific index
myClasses.pop()
print(myClasses)
myClasses.pop(1)
print(myClasses)
print("myClasses is " + str(len(myClasses)) + " items long.")
print(myClasses[len(myClasses) - 1])

# loop through a list
count = 1
for aClass in myClasses:
	print("Item " + str(count) + " is " + aClass)
	count += 1
numbers = [1,3,5,7,9]
# Challenge: loop through list, add all the numbers and print the sum
count2 = 1
total = 0
for number in numbers:
	print (number)
	total += number
	count2 += 1
print ("Your total number is " + str(total))
