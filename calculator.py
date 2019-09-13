number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if ((number_1) >= 0 or (number_1) <= 0) and ((number_2) >= 0 or (number_2) <= 0):
	operation = input("Enter the operation required: ")
	if operation == "+":
		print(number_1 + number_2)
	elif operation == "-":
		print(number_1 - number_2)
	elif operation == "*":
		print(number_1 * number_2)
	elif operation == "/":
		print(number_1 / number_2)
	else:
		print("Operation is not valid!")
else:
	print("Sorry invalid input! Try again")

