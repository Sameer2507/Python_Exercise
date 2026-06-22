import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, other):
        return math.sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)

    def isNearBy(self, p1):
        return self.distance(p1) < 5

    def __str__(self):
        return f"({self.__x}, {self.__y})"

x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print(f"The distance between {p1} and {p2} is: {p1.distance(p2):.2f}")
if p1.isNearBy(p2):
    print(f"{p1} and {p2} are near each other.")
else:
    print(f"{p1} and {p2} are not near each other.")