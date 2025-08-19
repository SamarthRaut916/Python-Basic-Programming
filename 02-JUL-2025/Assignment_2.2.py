class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print(f"Rectangle: width = {self.width}, height = {self.height}")

# Create a rectangle 
rect = Rectangle(5, 3)

# Display the rectangle's properties
rect.display()

# Print area and perimeter
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
