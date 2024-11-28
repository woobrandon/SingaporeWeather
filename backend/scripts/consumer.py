from kafka import KafkaConsumer
import json
from scripts import stream_processing
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOPIC_TEMPERATURE = "singapore_temperature"
TOPIC_WEATHER_FORECAST = "singapore_weather_forecast"
BOOTSTRAP_SERVERS = ["localhost:9092"]

def consume_message():
    try:
        consumer = KafkaConsumer(
            TOPIC_TEMPERATURE,
            TOPIC_WEATHER_FORECAST,
            bootstrap_servers = BOOTSTRAP_SERVERS,
            auto_offset_reset = "earliest",
            group_id = 'weathe-consumer-group',
            enable_auto_commit = True,
            value_deserializer = lambda x:json.loads(x.decode('utf-8'))
        )

        logging.info(f"Connected to Kafka topic '{TOPIC_TEMPERATURE}' and '{TOPIC_WEATHER_FORECAST}'. Waiting for messages...\n")
        for message in consumer:
            data = message.value
            topic = message.topic
            if topic == TOPIC_TEMPERATURE:
                if "readings" in data and data["readings"]:
                    processed_data = stream_processing.process_temperature_stream(data)
                    logging.info(f"Processed weather forecast data: {processed_data}")
                    yield processed_data
                else:
                    logging.error(f"Invalid temperature data: {data}")
            elif topic == TOPIC_WEATHER_FORECAST:
                # Process weather forecast stream
                if "records" in data and data["records"]:
                    processed_data = stream_processing.process_weather_forecast_stream(data)
                    logging.info(f"Processed weather forecast data: {processed_data}")
                    yield processed_data
                    
                else:
                    logging.error(f"Invalid weather forecast data: {data}")
    
    except Exception as e:
        logging.error(f"Error in consuming messages: {e}")
    finally:
        consumer.close()