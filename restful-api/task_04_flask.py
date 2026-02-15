#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
# Per instructions: Do not include testing data for the checker.
users = {}

@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames."""
    # users.keys() gives us the usernames; list() converts it to a JSON-serializable list
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the status of the API."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the full object for a specific user."""
    # .get() returns None if the key isn't found
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user via POST request."""
    # get_json(silent=True) returns None if parsing fails instead of raising an error
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user to our dictionary
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
