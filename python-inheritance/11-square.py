#!/usr/bin/python3
"""this is python code document"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is Documentation"""

    def __init__(self, size):
        """This is Documentation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Python document"""
        return "[{}] {}/{}".format(
                __class__.__name__,
                self.__size,
                self.__size
                )
