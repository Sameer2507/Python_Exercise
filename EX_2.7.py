minutes = int(input("Enter the number of minutes: "))

total_days = minutes // 60 // 24
years = total_days // 365
days = total_days % 365

print(f"{minutes} minutes is approximately {years} years and {days} days")