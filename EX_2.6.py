number = int(input("Enter a number between 0 and 1000: "))

digit1 = number % 10
remaining = number // 10

digit2 = remaining % 10
remaining = remaining // 10

digit3 = remaining % 10

total = digit1 + digit2 + digit3
print(f"The sum of the digits is {total}")