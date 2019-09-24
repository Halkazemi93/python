skills = [
    'Python', 
    'Django', 
    'JavaScript', 
    'Painting', 
    'Critical Thinking', 
    'Running',
]
cv = {'name':' ' , 'age':' ' , 'experience':' ' , 'skills':[]}

print("""Welcome to the Recruitment Program! Please follow the instructions below
""")
cv['name'] = input("Please write your name: ").title()
cv['age'] = int(input("Please write your age: "))
cv['experience'] = int(input("Please write your years of experience: "))

print("Please choose two skills from the following skills set below by typing the number corresponding to that skill:")

print("skills:")
for skill in skills:
    number_seq = 1
    print("{}- ".format(skills.index(skill) + 1) + skill)
    number_seq += 1
option1 = int(input("Please choose your first skill: "))
option2 = int(input("Please choose your second skill. It cannot be the same as the first skill: "))

if option1 >= 1 and option1 <= len(skills):
    cv["skills"].append(skills[int(option1) - 1])
else:
    print("Not part of the list!")

if option2 >= 1 and option2 <= len(skills):
    cv['skills'].append(skills[int(option2) - 1])
else:
    print("Not part of the list!")


if cv['age'] >= 21 and cv['age'] <= 50 and cv['experience'] >= 4 and ((option1 == 1) or (option2 == 1)):
    print("Congratulations {}, you have been accepted to the program!!!!".format(cv['name']))
else:
    print("Unfortunately your credentials do not meet the requirements. Sorry you have been rejected")
