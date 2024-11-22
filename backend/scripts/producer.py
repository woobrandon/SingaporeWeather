from kafka import KafkaProducer
import requests
import json
import time
import pandas as pd

COLLECTION_ID = 1459          
API_URL = "https://api-open.data.gov.sg/v2/real-time/api/air-temperature"

TOPIC = "singapore_temperature"
KAFKA_BROKER = "localhost:9092"

# Initialize Kafka Producer with JSON serialization
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),  # Serialize data to JSON
    api_version=(0, 11, 5)
)

def fetch_temperature_data():
    try:
        # Fetch data from the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        temperature = {}
        # Extract relevant information (modify based on API response format)
        if "data" in data:
            return data["data"]
        else:
            print("Unexpected data format:", data)
            return None
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

while True:
    # Fetch temperature data
    temperature_data = fetch_temperature_data()
    if temperature_data:
        try:
            # Send temperature data to Kafka
            producer.send(TOPIC, value=temperature_data)
            print(f"Sent :{temperature_data["readings"][0]["timestamp"]}")
        except Exception as e:
            print(f"Error sending data to Kafka: {e}")
    else:
        print("No data to send.")
    time.sleep(30)
