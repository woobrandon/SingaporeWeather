import threading
import queue
import sqlite3
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from scripts import consumer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Queue to store consumed messages
message_queue = queue.Queue()

def background_consumer():
    logging.info("Consumer thread started.")
    for message in consumer.consume_message():
        logging.info("Received message in consumer thread.")
        message_queue.put(message)

# Start the consumer thread
consumer_thread = threading.Thread(target=background_consumer, daemon=True)
consumer_thread.start()

@app.route('/temperature', methods=["GET"])
def get_temperature():
    try:
        # Check if there is any data in the queue
        if not message_queue.empty():
            processed_data = message_queue.get()
            if hasattr(processed_data, "toPandas"):
                result = processed_data.toPandas()
                data = result.to_dict(orient='records')
            else:
                data = processed_data
            return data
        else:
            return jsonify({"message": "No new temperature data available"}), 204

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/weather-forecast', methods=["GET"])
def get_weather_forecast():
    try:
        # Check if there is any data in the queue
        if not message_queue.empty():
            processed_data = message_queue.get()
            if hasattr(processed_data, "toPandas"):
                result = processed_data.toPandas()
                data = result.to_dict(orient='records')
            else:
                data = processed_data
            return data
        else:
            return jsonify({"message": "No new temperature data available"}), 204

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
