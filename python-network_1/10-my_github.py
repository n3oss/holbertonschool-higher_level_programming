#!/usr/bin/python3
"""
Uses Basic Authentication with a GitHub Personal Access Token
to access GitHub API and display the user's ID.
"""
import sys
import requests


if __name__ == "__main__":
    # Credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    # requests.get supports 'auth' parameter for Basic Authentication
    # It takes a tuple: (username, password/token)
    r = requests.get(url, auth=(username, password))
    try:
        # Convert the response body from JSON into a Python dictionary
        json_data = r.json()
        # Display the 'id' field if it exists, otherwise print None
        print(json_data.get('id'))
    except ValueError:
        # Handle cases where the response is not valid JSON
        print("None")
