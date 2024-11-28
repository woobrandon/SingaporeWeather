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

temperature_queue = queue.Queue()
weather_queue = queue.Queue()

def background_consumer():
    logging.info("Consumer thread started.")
    for message in consumer.consume_message():
        if 'temperature' in message.columns:
            temperature_queue.put(message)
            logging.info("Queued message into temperature queue")
        elif 'forecast_summary' in message.columns:
            weather_queue.put(message)
            logging.info("Queued message into weather forecast queue")
        else:
            logger.warning("Unknown message type received")

# Start the consumer thread
consumer_thread = threading.Thread(target=background_consumer, daemon=True)
consumer_thread.start()

@app.route('/temperature', methods=["GET"])
def get_temperature():
    try:
        # Check if there is any data in the queue
        if not temperature_queue.empty():
            if temperature_queue.qsize() == 1:
                processed_data = temperature_queue.queue[0]
            else:
                processed_data = temperature_queue.get()
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
        if not weather_queue.empty():
            if weather_queue.qsize() == 1:
                processed_data = weather_queue.queue[0]
            else:
                processed_data = weather_queue.get()
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
