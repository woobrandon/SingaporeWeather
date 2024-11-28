# Start Kafka producer
echo "Starting Kafka producer..."
python producer.py &  # Run the producer in the background
sleep 2  # Wait for the producer to start

# Start Flask app
echo "Starting Flask app..."
python ../app.py &  # Run Flask app in the background
sleep 8  # Wait for Flask app to initialize

# Start npm frontend in src directory
echo "Starting npm..."
cd ../../frontend/src && npm start &  # Change to the src directory and start npm

# Wait for all processes to finish (this script won't exit until all processes are terminated)
wait