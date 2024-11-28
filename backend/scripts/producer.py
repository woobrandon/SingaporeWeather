from kafka import KafkaProducer
import requests
import json
import time
import logging
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
         
SINGAPORE_TEMPERATURE_API_URL = "https://api-open.data.gov.sg/v2/real-time/api/air-temperature"
SINGAPORE_WEATHER_FORECAST_API_URL = "https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook"


TOPIC_TEMPERATURE = "singapore_temperature"
TOPIC_WEATHER_FORECAST = "singapore_weather_forecast"
KAFKA_BROKER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_data(api_url, data_key):
    """Fetch data from the specified API and return the relevant key."""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get(data_key)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from {api_url}: {e}")
    return None

def send_data(topic, data):
    """Send data to the specified Kafka topic."""
    try:
        producer.send(topic, value=data)
        producer.flush()  # Ensure the message is sent
        logger.info(f"Data sent to topic '{topic}'")
    except Exception as e:
        logger.error(f"Error sending data to Kafka topic '{topic}': {e}")

def fetch_temperature():
    """Fetch and send temperature data every minute in a separate thread."""
    while True:
        # Fetch and send temperature data every 1 minute
        temperature_data = fetch_data(SINGAPORE_TEMPERATURE_API_URL, "data")
        if temperature_data:
            send_data(TOPIC_TEMPERATURE, temperature_data)
        else:
            logger.warning("No temperature data to send.")
        
        time.sleep(60)  # Sleep for 60 seconds (1 minute) before fetching again

def fetch_weather_forecast():
    """Fetch and send weather forecast data twice a day in a separate thread."""
    while True:
        # Fetch and send weather forecast data every 12 hours (43200 seconds)
        forecast_data = fetch_data(SINGAPORE_WEATHER_FORECAST_API_URL, "data")
        if forecast_data:
            send_data(TOPIC_WEATHER_FORECAST, forecast_data)
        else:
            logger.warning("No weather forecast data to send.")
        
        time.sleep(43200)  # Sleep for 12 hours (43200 seconds) before fetching again

def main():
    # Start two separate threads for fetching temperature and weather forecast data
    temperature_thread = threading.Thread(target=fetch_temperature, daemon=True)
    weather_forecast_thread = threading.Thread(target=fetch_weather_forecast, daemon=True)

    # Start the threads
    temperature_thread.start()
    weather_forecast_thread.start()

    # Keep the main thread running to allow background threads to execute
    temperature_thread.join()
    weather_forecast_thread.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Producer stopped by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        producer.close()