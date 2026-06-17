def sumDigits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input("Enter an integer: "))
print(f"The sum of digits in {n} is {sumDigits(n)}")