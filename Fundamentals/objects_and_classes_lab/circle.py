class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = (Circle.__pi * self.diameter ** 2) / 4
        return area

    def calculate_area_of_sector(self, circle_angle):
        radius = self.diameter / 2
        area_of_sector = (circle_angle / 360) * Circle.__pi * radius * radius
        return area_of_sector
