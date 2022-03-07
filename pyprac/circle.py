
class Circle:
    # diameter (2r), circumference (2πr) and area (πr²)
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * self.PI * self.radius

    def area(self):
        return self.PI * (self.radius ** 2)

    def __str__(self):
        return f'I am a Circle with Radius: {self.radius}, ' + \
               f'Diameter: {self.diameter()}, Circumference: {self.circumference()}, ' + \
               f'Area: {self.area()}'
