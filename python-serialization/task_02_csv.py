#!/usr/bin/python3
"""
Convert CSV data to JSON and save it to data.json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format."""
    try:
        with open(csv_filename, "r", newline="") as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception:
        return False
