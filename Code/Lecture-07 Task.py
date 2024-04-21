import datetime

months = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}

month = input("Enter a month: ")

if month not in months:
    print("Month entered is not valid")

day = int(input("Enter a day: "))

if month == "February" and day > 29:
    print("Invalid date")

if 0 >= day > 31:
    print("Day entered is not valid")
else:
    if month == 'March' and day >= 20 or month == 'April' or month == 'May' or month == 'June' and day <= 20:
        print('Spring')
    elif month == 'June' and day >= 21 or month == 'July' or month == 'August' or month == 'September' and day <= 21:
        print('Summer')
    elif month == 'September' and day >= 22 or month == 'October' or month == 'November' or month == 'December' and day <= 20:
        print('Autumn')
    elif month == 'December' and day >= 21 or month == 'January' or month == 'February' or month == 'March' and day <= 19:
        print('Winter')


