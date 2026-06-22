def reverse(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

s = input("Enter a string: ")
print(f"The reversed string is: {reverse(s)}")