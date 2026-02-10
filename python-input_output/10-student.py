#!/usr/bin/python3
"""
Module that defines a Student class with selective JSON serialization
"""


class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in that list are fetch
        """
        # If attrs is a list of strings
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for key in attrs:
                # Check if the attribute exists in the object's dictionary
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        # Otherwise, return the full dictionary as before
        return self.__dict__
