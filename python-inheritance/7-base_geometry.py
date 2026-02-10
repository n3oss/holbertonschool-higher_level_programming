#!/usr/bin/python3
"""python class"""


class BaseGeometry:
    """python """
    def area(self):
        raise Exception('area() is not implemented')
    """Doxument"""

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.name = value
