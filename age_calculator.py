from datetime import datetime
now = datetime.now()
def check_birthdate(month, day, year):
  if (year) > now.year:
    return False
  elif (year) == now.year and (month) > now.month:
    return False
  elif (year) == now.year and (month) == now.month and (day) > now.day:
    return False
  else:
    return True
  
def calculate_age(month, day, year):
  age = int(now.year - (year))
  if month < now.month:
    print("Your are " + str(age) + " years old")
  elif month == now.month and day < now.day:
    print("Your are " + str(age) + " years old")
  elif month == now.month and day == now.day:
    print("Your are " + str(age) + " years old")
  elif month == now.month and day > now.day:
    print("Your are " + str(age - 1) + " years old")
  elif month > now.month:
    print("Your are " + str(age - 1) + " years old")
  else:
    print("Invalid birthdate")
  
birthyear = int(input("Enter your year of birth in the format YYYY: "))
birthmonth = int(input("Enter your month of birth in the format MM: "))
birthday = int(input("Enter your day of birth in the format DD: "))

if check_birthdate(birthmonth, birthday, birthyear) == True:
  calculate_age(birthmonth, birthday, birthyear)
else:
  print("Invalid birthdate")
