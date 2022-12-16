# Check whether a given date is valid. If yes, find the next date, consider leap year as well.

from datetime import datetime, timedelta

date_string = input("Enter date in DD-MM-YYYY format: ")

try:
    given_date = datetime.strptime(date_string, "%d-%m-%Y")
except ValueError as err:
    print("Invalid date. Please provide date in format DD-MM-YYYY")
    print("Error message:", err)
    exit(1)

next_date = given_date + timedelta(days=1)
print(next_date.strftime("%d-%m-%Y"))
