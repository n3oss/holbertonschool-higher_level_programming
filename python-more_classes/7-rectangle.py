#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle with private width and height."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle.
        Note: We use the setters by calling self.width and self.height
        to ensure the validation logic is applied.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the private instance attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width with type and value validation."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height with type and value validation."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area for rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter for rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """Returns a string of '#' representing the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Delete the class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """Returns a string representation  using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""

        # Build the rectangle string using the shared print_symbol
        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])
