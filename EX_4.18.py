rate = float(input("Enter the exchange rate from dollars to RMB: "))
direction = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))
amount = float(input("Enter the amount: "))
if direction == 0:
    result = amount * rate
    print(f"${amount} is {result} yuan")
elif direction == 1:
    result = amount / rate
    print(f"{amount} yuan is ${result}")
else:
    print("Incorrect input")