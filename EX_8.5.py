def count(s1, s2):
    count = 0
    index = 0
    while index <= len(s1) - len(s2):
        pos = s1.find(s2, index)
        if pos != -1:
            count += 1
            index = pos + len(s2)
        else:
            break
    return count

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print(f"The number of occurrences of \"{s2}\" in \"{s1}\" is: {count(s1, s2)}")