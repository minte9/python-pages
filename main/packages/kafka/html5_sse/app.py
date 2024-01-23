from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/events')
def events():
    def generate():
        while True:

            """
                Yeld is often used for streaming data to the client, like in Server-Sent Events (SSE).
                When you use yield in a route, Flask keeps the connection open.
                It sends each value yielded by the function to the client as it becomes available.
                
                This is different from a regular Flask route that returns a complete response at once. 
                With yield, the response is sent in chunks over time.
            """
            yield f"data: Server time is {time.ctime()}\n\n"

            time.sleep(2)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
