import math
import sys
grocery_items = []
dictionary = {}
print("Welcome to the Simple Receipt calculator")
print("""Enter 'done', when prompted to enter item name, to print receipt!
""")

def package(item, price, quantity):
    dictionary["name"] = item
    dictionary["price"] = price
    dictionary["quantity"] = quantity
    grocery_items.append(dictionary.copy())
    
while True:
    useritem = input("Please enter the name of the item: ").lower()
    if useritem == "done":
        break
    elif useritem != "done":
        userprice = input("Please enter the price of the item: ")
        try:
            val = float(userprice)
        except ValueError:
            print("Input was not a number! Please try again")
            sys.exit()
        userquantity = input("Please enter the quantity of the item: ")
        try:
            val = int(userquantity)
        except ValueError:
            print("Input was not a whole number! Please try again")
            sys.exit()
        package(useritem, float(userprice), int(userquantity))
        continue
total_due = 0

print("""
-------------- RECEIPT ----------------
""")
for item in grocery_items:
    print(item["name"] + " = {}".format(item["quantity"]) + ", each for KD {}".format(item["price"]))
    total_due += (item["price"] * item["quantity"])
print("""
---------------------------------------""")    
print("The total amount due is: KD {}".format(round(total_due, 3)))
