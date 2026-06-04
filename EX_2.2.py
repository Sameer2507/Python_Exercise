import math
radius, length = eval(input("Enter radius and length: "))
area = radius * radius * math.pi
volume = area * length
print(f"The area is {round(area, 4)}")
print(f"The volume is {round(volume, 1)}")