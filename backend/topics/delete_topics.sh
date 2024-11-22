#!/bin/bash
# Kafka topics deletion script

BOOTSTRAP_SERVER="localhost:9092"

# Delete topics
../kafka/bin/kafka-topics.sh --delete --topic stock-prices --bootstrap-server $BOOTSTRAP_SERVER
../kafka/bin/kafka-topics.sh --delete --topic my-topic --bootstrap-server $BOOTSTRAP_SERVER

# List remaining topics
../kafka/bin/kafka-topics.sh --list --bootstrap-server $BOOTSTRAP_SERVER
