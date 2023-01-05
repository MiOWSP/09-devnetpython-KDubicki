from math import pi

class circleClass:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.circumferenceValue = self.circumference(radius)

    def  circumference(self, radius):
        return 2 * pi * radius

    def printCircumference(self):
        print(f'Circle {self.name} have radius: {self.radius} and circumference: {self.circumferenceValue}')


# circle_1 = circleClass('first', 3)
# circle_2 = circleClass('second', 7)
# circle_3 = circleClass('third', 7.5)
# circle_1.printCircumference()
# circle_2.printCircumference()
# circle_3.printCircumference()