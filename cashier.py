import math
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
        userprice = float(input("Please enter the price of the item: "))
        userquantity = int(input("Please enter the quantity of the item: "))
        package(useritem, userprice, userquantity)
        continue
total_due = 0
for item in grocery_items:
    total_due += float((item["price"] * item["quantity"]))

print("""
-------------- RECEIPT ----------------
""")
for item in grocery_items:
    print(item["name"] + " = {}".format(item["quantity"]) + ", each for KD {}".format(item["price"]))
print("""
---------------------------------------""")    
print("The total amount due is: KD {}".format(round(total_due, 3)))
