#!/usr/bin/env python3
"""
Module demonstrating custom object serialization using pickle.
"""
import pickle


class CustomObject:
    """
    A class representing a person with serialization capabilities.
    """
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of CustomObject from a file.
        Returns:
            CustomObject: The loaded instance or None if an
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
            return None
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
