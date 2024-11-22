from kafka import KafkaConsumer
import json
import station_stream_processing

TOPIC_NAME = "singapore_temperature"
BOOTSTRAP_SERVERS = ["localhost:9092"]

def consume_message():
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers = BOOTSTRAP_SERVERS,
            auto_offset_reset = "earliest",
            group_id = 'temperature-consumer-group',
            enable_auto_commit = True,
            value_deserializer = lambda x:json.loads(x.decode('utf-8'))
        )

        print(f"Connected to Kafka topic '{TOPIC_NAME}'. Waiting for messages...\n")

        for message in consumer:
            data = message.value
            print(f"Recevied message: {data["readings"][0]["timestamp"]}")
        return consumer
    
    except Exception as e:
        print(f"Error in consuming messages: {e}")

if __name__ == "__main__":
    while True:
        fetched_temperature = consume_message()