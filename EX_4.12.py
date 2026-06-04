num = int(input("Enter an integer: "))
if num % 5 == 0 and num % 6 == 0 :
    print("true")
else :
    print("false")
if num % 5 == 0 or num % 6 == 0 :
    print("true")
else:
    print("false")
if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):
    print("true")
else:
    print("false")
