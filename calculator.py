import sys

number_1 = input("Enter the first number: ")
try:
	val = float(number_1)
except ValueError:
	print("The input was not a number! Try again")
	sys.exit()
number_2 = input("Enter the second number: ")
try:
	val = float(number_2)
except ValueError:
	print("The input was not a number! Try again")
	sys.exit()

operation = input("Enter the operation required: ")
if operation == "+":
	print(float(number_1) + float(number_2))
elif operation == "-":
	print(float(number_1) - float(number_2))
elif operation == "*":
	print(float(number_1) * float(number_2))
elif operation == "/":
	print(float(number_1) / float(number_2))
else:
	print("Operation is not valid!")


