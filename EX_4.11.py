month, year = eval(input("Enter month and year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(f"Month {month} year {year} has 31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"Month {month} year {year} has 30 days")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Month {month} year {year} has 29 days")
    else:
        print(f"Month {month} year {year} has 28 days")