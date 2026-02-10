#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle with private width and height."""


class Rectangle:

    """Class that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle.
        Note: We use the setters by calling self.width and self.height
        to ensure the validation logic is applied.
        """
        self.width = width
        self.height = height

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
