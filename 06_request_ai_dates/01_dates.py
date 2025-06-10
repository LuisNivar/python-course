from datetime import datetime, timedelta
import locale
import os

os.system("cls")
locale.setlocale(locale.LC_TIME, "es-ES.UTF-8") # 

# 1 Get current date
date = datetime.now()
print("Now: ",date)
print("-"*70)

# 2 Get specific date
date = datetime(2025,5,15)
print("Date: ",date)
print("-"*70)

# 3 Format Date

formated_date = date.strftime("%d/%m/%Y")
print(formated_date)

formated_date = date.strftime("%a %d/%b/%y")
print(formated_date)

formated_date = date.strftime("%A %d-%b-%y")
print(formated_date)
print("-"*70)

# 4- Operations with dates
yesterday = datetime.now()- timedelta(1)
print(yesterday)

past_week = datetime.now()- timedelta(weeks=1)
print(past_week)

past_5_hours = datetime.now()- timedelta(hours=5)
print(past_5_hours)
print("-"*70)

# 5- Get individual parts of a date
year = datetime.now().year
print(year)
month = datetime.now().month
print(month)
day = datetime.now().day
print(day)
print("-"*70)

# 6 - Difference between two dates
birthday = datetime(1991,2,20)
now = datetime.now()

difference = now - birthday
print(difference)
print("-"*70)
