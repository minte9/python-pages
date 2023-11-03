""" Flask 'Hello World' APP v2.1   
Start the app with 'flask run'
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker & Jenkins!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')