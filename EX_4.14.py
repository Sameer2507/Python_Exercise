import random
coin = random.randint(0, 1)
guess = int(input(f"enter ur guess:"))
if guess == coin:
    print("Correct guess!")
else:
    print("Wrong guess!")
