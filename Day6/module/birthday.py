# Write a Python program that utilizes the built-in datetime module to perform the following tasks:
# Get the current date and time and display it on the console.
# Create a datetime object representing your birthday.
# Calculate the difference between the current date and your birthday, and display the result in years, months, and days.


import datetime as d
s =d.datetime.now()
b =d.date(2023,12,24) 
present = d.date.today()
diff = b-present
years = diff.days // 365
remaining_days = diff.days % 365
months = remaining_days // 30
days = remaining_days % 30
print("Difference between current date and your birthday:")
print("Years:", years)
print("Months:", months)
print("Days:", days)