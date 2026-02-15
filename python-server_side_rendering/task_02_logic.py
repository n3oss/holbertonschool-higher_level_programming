#!/usr/bin/python3
"""Basic HTML template in flask"""
from flask import Flask, render_template
import json
app = Flask(__name__)
@app.route('/')
def home():
    """" route for home page"""
    return render_template('index.html')
@app.route('/about')
def about():
    """"route for about page"""
    return render_template('about.html')
@app.route('/contact')
def contact():
    """ route for contact page """
    return render_template('contact.html')
@app.route('/items')
def items():
    """"route for items page"""
    try:
        with open('items.json', 'r') as json_file:
            items = json.load(json_file)
            items_list = items.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    #pass items to template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
