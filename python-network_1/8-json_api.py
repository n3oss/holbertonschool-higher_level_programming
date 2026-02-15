#!/usr/bin/python3
"""
Sends a POST request to a local API with a letter as a parameter.
Handles JSON formatting and empty response scenarios.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the letter from arguments, or default to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    try:
        # Send POST request
        r = requests.post(url, data=payload)
        # Try to parse the response as JSON
        json_data = r.json()
        # Check if the dictionary is empty
        if not json_data:
            print("No result")
        else:
            # Access values safely and format the output
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print("[{}] {}".format(user_id, user_name))
    except ValueError:
        # This triggers if r.json() fails because the body isn't valid JSON
        print("Not a valid JSON")
