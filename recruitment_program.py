skills = [
    'Python', 
    'Django', 
    'JavaScript', 
    'Painting', 
    'Critical Thinking', 
    'Running',
]
cv = {'Name':' ' , 'Age':' ' , 'Experience':' ' , 'Skills':[]}

print("""Welcome to the Recruitment Program! Please follow the instructions below
""")
cv['Name'] = input("Please write your name: ").title()
cv['Age'] = int(input("Please write your age: "))
cv['Experience'] = int(input("Please write your years of experience: "))

print("Please choose two skills from the following skills set below by typing the number corresponding to that skill:")

print("skills:")
for skill in skills:
    number_seq = 1
    print("{}- ".format(skills.index(skill) + 1) + skill)
    number_seq += 1
option1 = int(input("Please choose your first skill: "))
option2 = int(input("Please choose your second skill. It cannot be the same as the first skill: "))

if option1 == 1:
    cv['Skills'].append('Python')
elif option1 == 2:
    cv['Skills'].append('Django')
elif option1 == 3:
    cv['Skills'].append('JavaScript')
elif option1 == 4:
    cv['Skills'].append('Painting')
elif option1 == 5:
    cv['Skills'].append('Critical Thinking')
elif option1 == 6:
    cv['Skills'].append('Running')
else:
    print("Not part of the list!")

if option2 == 1:
    cv['Skills'].append('Python')
elif option2 == 2:
    cv['Skills'].append('Django')
elif option2 == 3:
    cv['Skills'].append('JavaScript')
elif option2 == 4:
    cv['Skills'].append('Painting')
elif option2 == 5:
    cv['Skills'].append('Critical Thinking')
elif option2 == 6:
    cv['Skills'].append('Running')
else:
    print("Not part of the list!")

if cv['Age'] >= 21 and cv['Age'] <= 50 and cv['Experience'] >= 4 and ((option1 == 1) or (option2 == 1)):
    print("Congratulations {}, you have been accepted to the program!!!!".format(cv['Name']))
else:
    print("Unfortunately your credentials do not meet the requirements. Sorry you have been rejected")
