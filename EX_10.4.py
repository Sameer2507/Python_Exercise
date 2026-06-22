scores = list(map(float, input("Enter scores separated by spaces: ").split()))
average = sum(scores) / len(scores)

above = sum(1 for s in scores if s >= average)
below = sum(1 for s in scores if s < average)

print(f"Average is: {average:.2f}")
print(f"Number of scores above or equal to the average: {above}")
print(f"Number of scores below the average: {below}")