def prefix(s1, s2):
    result = ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            break
    return result

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
common = prefix(s1, s2)
if common:
    print(f"The common prefix is: {common}")
else:
    print("The two strings have no common prefix.")