num_students = int(input("Enter number of students: "))
highest = 0

for i in range(num_students):
    score = float(input("Enter score: "))
    if score > highest:
        highest = score

print(f"The highest score is {highest}")