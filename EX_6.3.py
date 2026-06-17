def reverse(number):
    number = abs(number)
    reversed_num = 0
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return reversed_num

def isPalindrome(number):
    return abs(number) == reverse(number)

n = int(input("Enter an integer: "))
if isPalindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")