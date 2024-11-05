""" Simple Flask app that accepts JSON requests and returns a JSON response

This app listens for POST requests on /json-endpoint.
Expects the request body to be a valid JSON object.

curl -X POST -H "Content-Type: application/json" -d '{"name": "Fabien"}' \
http://127.0.0.1:5000/json-endpoint
    Output: {"message":"Hello, Fabien"}
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/json-endpoint', methods=['POST'])
def json_endpoint():
    
    if request.is_json:
        data = request.get_json()

        # Perform some operations with data
        name = data.get('name', 'Unknown')

        # Prepare JSON response
        return jsonify({'message': f'Hello, {name}'})
    else:
        # Handle non-JSON requests
        return jsonify({'error': 'Invalid request format'}), 400

if __name__ == '__main__':
    app.run(debug=True)