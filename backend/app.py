import threading
import queue
import sqlite3
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from scripts import consumer
import logging
import schedule
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

temperature_queue = queue.Queue()
weather_queue = queue.Queue()

def consume_message_periodically():
    try:
        # Run consume_message once every minute
        schedule.every(1).minute.do(background_consumer)

        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
    except Exception as e:
        logging.error(f"Error in scheduled message consumption: {e}")

def background_consumer():
    logging.info("Consumer thread started.")
    try:
        messages = consumer.consume_message()
        for message in messages:
            if 'temperature' in message.columns:
                temperature_queue.put(message)
                logging.info("Queued message into temperature queue")
            elif 'forecast' in message.columns:
                weather_queue.put(message)
                logging.info("Queued message into weather forecast queue")
            else:
                logger.warning("Unknown message type received")
    except Exception as e:
        logging.error(f"Error consuming message: {e}")

# Start the consumer thread
consumer_thread = threading.Thread(target=consume_message_periodically, daemon=True)
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
