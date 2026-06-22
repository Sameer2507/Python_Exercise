def binaryToDecimal(binaryString):
    decimal = 0
    for char in binaryString:
        decimal = decimal * 2 + int(char)
    return decimal

binaryString = input("Enter a binary string: ")
print(f"The decimal value of \"{binaryString}\" is: {binaryToDecimal(binaryString)}")