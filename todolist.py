import pickle
print ("Welcome to the To Do List :))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter l to load list")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		pickle.dump(todoList,open("save.p", "wb"))
		break
	elif choice == "a":
		addition = input("What would you like to add to the list? ")
		todoList.append(addition)
	elif choice == "r":
		subtraction = input("What would you like to remove? ")
		todoList.remove(subtraction)
	elif choice == "p":
		print(todoList)
	elif choice == "l":
		todoList = pickle.load(open("save.p", "rb"))
	else:
		print("That is not an option. :(")	