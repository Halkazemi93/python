from datetime import datetime
from dateutil import relativedelta
import sys
now = datetime.now()
try:
    iyears = int(input("Please write the year in which you were born: "))
    imonths = int(input("Please write the month in which you were born: "))
    idays = int(input("Please write the day in which you were born: "))
except ValueError:
    print("Sorry! That is not a valid input")
    sys.exit()

def check_brithdate(year, month, day):
    birthdate = datetime(year, month, day, 00, 00)
    difference = relativedelta.relativedelta(now, birthdate)
    
    return not((difference.years < 0) or (difference.months < 0) or (difference.days < 0))
def calculate_age(year, month, day):
    birthdate = datetime(year, month, day, 00, 00)
    difference = relativedelta.relativedelta(now, birthdate)
    print("You are %s years, %s months and %s days old" % (difference.years, difference.months, difference.days))

if check_brithdate(iyears, imonths, idays) == True:
    calculate_age(iyears, imonths, idays)
else:
    print("Invalid birthdate. Seems to be in the future!!!")
    sys.exit()
