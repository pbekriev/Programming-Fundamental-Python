class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumfewrence(self):
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        return