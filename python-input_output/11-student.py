#!/usr/bin/python3
"""Define a Student class with JSON seriald deserialization."""


class Student:
    """Student class with first_name, laste attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """f instance attributes filter by attrs if given"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """ of the instance using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
