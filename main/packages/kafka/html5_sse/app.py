from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/events')
def events():
    def generate():
        while True:
            yield f"data: Server time is {time.ctime()}\n\n"
            time.sleep(2)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
