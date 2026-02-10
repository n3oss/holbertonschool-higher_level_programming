#!/usr/bin/python3
"""
Serialize and deserialize Python dictionaries to and from XML.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
