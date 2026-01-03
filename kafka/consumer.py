import sys
import os
import json
from kafka import KafkaConsumer

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from run_agent import run_agent_flow

consumer = KafkaConsumer(
    "agentflow-input",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="agentflow-consumer-group"
)

print("Kafka Consumer started...")

for message in consumer:
    data = message.value
    print("Received:", data)

    query = data.get("query")
    if query:
        run_agent_flow(query)
    else:
        print("Message missing 'query'")