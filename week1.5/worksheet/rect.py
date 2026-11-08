# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int):
            raise TypeError("Width must be an integer.")
        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        else:
            self.width = width
            self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """This is the is_square method,
        this check if the values given for the rectangle class actually form a square"""
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """This is the area method, this calculates the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """This is the perimeter method, it calculates the perimeter"""
        return 2 * (self.width + self.height)