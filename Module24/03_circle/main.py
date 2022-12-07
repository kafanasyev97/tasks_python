import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return math.pi * self.r ** 2

    def length(self):
        return 2 * self.r * math.pi

    def increase(self, k):
        return self.length() * k

    def intersection(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) <= self.r + other.r


