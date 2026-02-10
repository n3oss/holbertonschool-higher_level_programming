#!/usr/bin/python3
"""this is document"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is document"""

    def __init__(self, width, height):
        """this is document"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """This is document"""
        return "[{}] {}/{}".format(
             __class__.__name__,
             self.__width,
             self.__height
             )

    def area(self):
        """This is Document"""
        return self.__width * self.__height
