from kafka import KafkaProducer
import json
import time
import random

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Replace with your broker's address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: json.dumps(k).encode('utf-8')
)

# Define the topic name
topic_name = 'second_topic'

# Function to generate random messages
def generate_random_message():
    uid= random.randint(1, 100)
    return {
        'key': f'user-{uid}',
        'value': {
            'message': f'Hello from user {uid}',
            'timestamp': time.time()
        }
    }

# Send multiple messages
for _ in range(111150):  # Number of messages to send
    msg = generate_random_message()
    producer.send(topic_name, key=msg['key'], value=msg['value'])
    time.sleep(2)  # Adding delay to simulate real-time messaging
    print(f"Sent message with key: {msg['key']}, value: {msg['value']}")

# Flush and close the producer
producer.flush()
producer.close()

print("All messages sent.")
