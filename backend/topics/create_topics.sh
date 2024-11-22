#!/bin/bash
# Kafka topics creation script

BOOTSTRAP_SERVER="localhost:9092"

# Create topics
../kafka/bin/kafka-topics.sh --create --topic stock-prices-topic --bootstrap-server $BOOTSTRAP_SERVER --partitions 3 --replication-factor 1
../kafka/bin/kafka-topics.sh --create --topic stock-alerts-topic --bootstrap-server $BOOTSTRAP_SERVER --partitions 1 --replication-factor 1

# List created topics
kafka-topics.sh --list --bootstrap-server $BOOTSTRAP_SERVER

chmod +x create_topics.sh