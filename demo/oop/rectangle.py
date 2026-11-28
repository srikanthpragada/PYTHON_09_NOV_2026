class Rectangle():
    def __init__(self, length : int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def circumference(self):
        return 2 * (self.width + self.length)

r = Rectangle(10,20)
print(r.area())

