from datetime import datetime
now = datetime.now()
print("""Welcome to HR Pro 2019
""")
print("""
Options:
    1. Show Employees
    2. Show Managers
    3. Add an Employee
    4. Add a Manager
    5. Exit
""")
manager_list = []
employee_list = []
dictionary = {}
class Manager:
    working_years = 0
    bonus = 0
    def __init__(self, name, age, salary, employment_date, bonus_percentage, **kwargs):
        self.name = name
        dictionary["name"] = self.name
        self.age = age
        dictionary["age"] = self.age
        self.salary = salary
        dictionary["salary"] = self.salary
        self.employment_date = employment_date
        dictionary["employment date"] = self.employment_date
        self.bonus_percentage = bonus_percentage
        self.get_bonus()
        self.get_working_years()
    
    def get_working_years(self):
        working_years = now.year - self.employment_date
        dictionary["working years"] = working_years
        manager_list.append(dictionary.copy())
        print("The Manager has been added successfully") 
        
    def get_bonus(self):
        bonus = (self.bonus_percentage/100) * self.salary
        dictionary["bonus"] = bonus


class Employee:
    employee_working_years = 0
    
    def __init__(self, name, age, salary, employment_date, **kwargs):
        self.name = name
        dictionary["name"] = self.name
        self.age = age
        dictionary["age"] = self.age
        self.salary = salary
        dictionary["salary"] = self.salary
        self.employment_date = employment_date
        dictionary["employment date"] = self.employment_date
        self.get_working_years()  
        
    def get_working_years(self):
        employee_working_years = now.year - self.employment_date
        dictionary["working years"] = employee_working_years
        employee_list.append(dictionary.copy())
        print("The Employee has been added successfully")     
        
while True:
    to_do = int(input("Please enter the number corresponding to the action you want to execute: "))
    if to_do == 1:
        print("""
        THE LIST OF EMPLOYEES ARE AS FOLLOWS:
        """)
        for member in employee_list:
            print("Name = {}".format(member["name"]))
            print("Age = {}".format(member["age"]))
            print("Salary = KD {}".format(member["salary"]))
            print("Employment date = {}".format(member["employment date"]))
            print("Working years = {}".format(member["working years"]))
            print("------------------------")  
    
    elif to_do == 2:
        print("""
        THE LIST OF MANAGERS ARE AS FOLLOWS:
        """)
        for member in manager_list:
            print("Name = {}".format(member["name"]))
            print("Age = {}".format(member["age"]))
            print("Salary = KD {}".format(member["salary"]))
            print("Bonus = KD {}".format(member["bonus"]))
            print("Employment date = {}".format(member["employment date"]))
            print("Working years = {}".format(member["working years"]))
            print("------------------------")
    elif to_do == 3:
        self = Employee(input("Please write the name of the employee: ").title(), int(input("Please write the age of the employee: ")), int(input("Please write the salary of the employee: ")), int(input("Please write the employment date of the employee: ")))
        continue
    elif to_do == 4:     
        self = Manager(input("Please write the name of the manager: ").title(), int(input("Please write the age of the manager: ")), int(input("Please write the salary of the manager: ")), int(input("Please write the employment date of the manager: ")), float(input("Please enter the bonus percentage for the manager: "))) 
        continue 
    elif to_do == 5:
        break
