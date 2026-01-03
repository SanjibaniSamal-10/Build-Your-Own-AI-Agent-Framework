import sys
import os
import json
from kafka import KafkaProducer

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Kafka Producer started. Type 'exit' to stop.")

while True:
    query = input("Enter your query: ").strip()

    if query.lower() == "exit":
        print("Stopping producer...")
        break

    message = {
        "query": query
    }

    producer.send("agentflow-input", message)
    producer.flush()

    print("Sent:", message)

producer.close()