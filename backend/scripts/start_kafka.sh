# Start Zookeeper
echo "Starting Zookeeper..."
../kafka/bin/zookeeper-server-start.sh ../kafka/config/zookeeper.properties &

# Wait for a few seconds to ensure Zookeeper is fully up
sleep 5

# Start Kafka
echo "Starting Kafka..."
../kafka/bin/kafka-server-start.sh ../kafka/config/server.properties &

echo "Kafka and Zookeeper are now running!"