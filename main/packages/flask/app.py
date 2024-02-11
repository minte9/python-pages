""" Flask 'Hello World' APP v2.1  

This is a simple Flask app that returns a 'Hello, Docker!' message
The app runs on port 5000

Start the app with 'flask run' command
Running on http://127.0.0.1:5000
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker v5!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')