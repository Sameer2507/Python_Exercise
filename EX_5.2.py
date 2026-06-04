import random
correct_count = 0
for i in range(10):
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    answer = int(input(f"What is {num1} + {num2}? "))
    if answer == num1 + num2:
        print("Correct!")
        correct_count += 1
    else:
        print(f"Wrong. The correct answer is {num1 + num2}")

print(f"You got {correct_count} correct out of 10")