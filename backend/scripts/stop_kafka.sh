# Stop Kafka
echo "Stopping Kafka..."
../kafka/bin/kafka-server-stop.sh

# Stop Zookeeper
echo "Stopping Zookeeper..."
../kafka/bin/zookeeper-server-stop.sh

echo "Kafka and Zookeeper have been stopped!"