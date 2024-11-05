from flask import Flask, Response
from kafka import KafkaConsumer
from flask_cors import CORS
import threading
import json
import queue
import time

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Queue to store messages
message_queue = queue.Queue()

def kafka_listener():
    consumer = KafkaConsumer(
        'AccessLogTopic',
        bootstrap_servers=['localhost:9092']
    )
    for message in consumer:
        json_data = message.value.decode()
        dict_data = json.loads(json_data)
        msg = f"AccessLog: {dict_data['ip_address']} {dict_data['datetime']} {dict_data['request']}"
        message_queue.put(msg) # Add message to the queue

@app.route('/events')
def events():
    def generate():
        while True:
            # Fetch message from the queue
            if not message_queue.empty():
                msg = message_queue.get()
                yield f"data: {msg}\n\n"
            time.sleep(2)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    # Kafka listener runs in its own thread
    kafka_thread = threading.Thread(target=kafka_listener)
    kafka_thread.start()
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
        # app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'), debug=True, host='0.0.0.0', port=5000)