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
class Employee:
    
    def __init__(self, name, age, salary, employment_date, **kwargs):
        self.name = name        
        self.age = age
        self.salary = salary
        self.employment_date = employment_date
        self.get_working_years()  
        
    def get_working_years(self):
        working_years = now.year - self.employment_date
        return working_years

class Manager(Employee):

    def __init__(self, name, age, salary, employment_date, bonus_percentage, **kwargs):
        super().__init__(name, age, salary, employment_date)
        self.bonus_percentage = bonus_percentage
            
        
    def get_bonus(self):
        bonus = (self.bonus_percentage/100) * self.salary
        return bonus
    
      
        
while True:
    to_do = int(input("Please enter the number corresponding to the action you want to execute: "))
    if to_do == 1:
        print("""
        THE LIST OF EMPLOYEES ARE AS FOLLOWS:
        """)
        for member in employee_list:
            print("Name = {}".format(member.name))
            print("Age = {}".format(member.age))
            print("Salary = KD {}".format(member.salary))
            print("Employment date = {}".format(member.employment_date))
            print("Working years = {}".format(member.get_working_years()))
            print("------------------------")  
    
    elif to_do == 2:
        print("""
        THE LIST OF MANAGERS ARE AS FOLLOWS:
        """)
        for member in manager_list:
            print("Name = {}".format(member.name))
            print("Age = {}".format(member.age))
            print("Salary = KD {}".format(member.salary))
            print("Bonus = KD {}".format(member.get_bonus()))
            print("Employment date = {}".format(member.employment_date))
            print("Working years = {}".format(member.get_working_years()))
            print("------------------------")
    elif to_do == 3:
        empl = Employee(input("Please write the name of the employee: ").title(), int(input("Please write the age of the employee: ")), int(input("Please write the salary of the employee: ")), int(input("Please write the employment date of the employee: ")))
        employee_list.append(empl) 
        print("The Employee has been added successfully")
        continue
    elif to_do == 4:     
        mngr = Manager(input("Please write the name of the manager: ").title(), int(input("Please write the age of the manager: ")), int(input("Please write the salary of the manager: ")), int(input("Please write the employment date of the manager: ")), float(input("Please enter the bonus percentage for the manager: ")))
        manager_list.append(mngr)
        print("The Manager has been added successfully") 
        continue 
    elif to_do == 5:
        break