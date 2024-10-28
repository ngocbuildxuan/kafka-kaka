from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer(
    'second_topic',  # Topic name
    bootstrap_servers=['localhost:9092'],  # Replace with your broker's address
    auto_offset_reset='earliest',  # Start from the earliest available message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='my-group',  # Consumer group ID
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    key_deserializer=lambda k: json.loads(k.decode('utf-8')) if k else None
)

# Consume messages from the topic
print("Listening for messages...")
for message in consumer:
    key = message.key
    value = message.value
    print(f"Received message with key: {key}, value: {value}")

# Close the consumer
consumer.close()
