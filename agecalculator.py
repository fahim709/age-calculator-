import datetime
import sys  # To exit the program if input is invalid

year = int(input('Enter your birth year: '))
month = int(input('Enter your birth month (1-12): '))
day = int(input('Enter your birth date (1-31): '))

# Input validation
if not (1 <= month <= 12):
    print('❌ Invalid month. Please enter a value from 1 to 12.')
    sys.exit()

if not (1 <= day <= 31):
    print('❌ Invalid day. Please enter a value from 1 to 31.')
    sys.exit()

try:
    birth_date = datetime.date(year, month, day)
except ValueError:
    print("❌ Invalid date. Please make sure the day exists in that month (e.g., Feb 30 is invalid).")
    sys.exit()

today = datetime.date.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f'🎉 You are {age} years old.')

