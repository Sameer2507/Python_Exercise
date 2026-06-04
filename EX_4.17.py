import random
computer = random.randint(0, 2)
user = int(input("scissor(0), rock(1), paper(2): "))
choices = {0: "scissor", 1: "rock", 2: "paper"}
if user == computer:
    print(f"The computer is {choices[computer]}. You are {choices[user]}. It's a draw!")
elif (user == 1 and computer == 0) or (user == 0 and computer == 2) or (user == 2 and computer == 1):
    print(f"The computer is {choices[computer]}. You are {choices[user]}. You won!")
else:
    print(f"The computer is {choices[computer]}. You are {choices[user]}. Computer won!")