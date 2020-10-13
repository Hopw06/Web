class Circle():
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.PI

    def circumference(self):
        return 2 * self.radius * self.PI


mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumference())
