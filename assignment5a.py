class Shape:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name of the shape {self.name}")

class Rectangle(Shape):
    def __init__(self, name, width, length):
        super().__init__(name)
        self.width = width
        self.length = length

    def area(self):
        area = self.width * self.length
        return area
    
    def perimeter(self):
        perimeter = (self.width + self.length) * 2
        return perimeter

    def display_info(self):
        print(f"Rectangle: {self.name}")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
    
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        area = self.side ** 2
        return area
    
    def perimeter(self):
        perimeter = self.side * 4
        return perimeter
    
    def display_info(self):
        print(f"Square: {self.name}")
        print(f"side: {self.side}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


rect1 = Rectangle("MyRectangle", 10, 14)
square1 = Square("MySquare", 4)

rect1.display_info()

print("================================")

square1.display_info()