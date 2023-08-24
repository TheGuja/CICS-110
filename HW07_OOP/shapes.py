# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

class Shape:
    pass

class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def get_sides(self):
        return (self.side_a, self.side_b, self.side_c)
    
class IsoscelesTriangle(Triangle):

    def __init__(self, doubled_side, side_c):
        super().__init__(doubled_side, doubled_side, side_c)

class EquilateralTriangle(IsoscelesTriangle):
    
    def __init__(self, side):
        super().__init__(side, side)

class Quadrilateral(Shape):

    def __init__(self, side_a, side_b, side_c, side_d):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c + self.side_d
    
    def get_sides(self):
        return (self.side_a, self.side_b, self.side_c, self.side_d)
    
class Rectangle(Quadrilateral):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__(length, length, width, width)

    def area(self):
        return self.length * self.width
    
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)