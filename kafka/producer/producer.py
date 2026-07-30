import sys
import os
import json
import time

from kafka import KafkaProducer

# ---------------------------------------------------------
# Add project root to Python path
# ---------------------------------------------------------

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.insert(0, project_root)

# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------

from simulator.sensor_generator import generate_sensor_data
from simulator.config import interval
from kafka_config import BOOTSTRAP_SERVER, TOPIC

# ---------------------------------------------------------
# Kafka Producer
# ---------------------------------------------------------

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

print("=" * 55)
print("      AtmoSync Kafka Producer Started")
print("=" * 55)

# ---------------------------------------------------------
# Produce Sensor Data
# ---------------------------------------------------------

while True:

    sensor = generate_sensor_data()

    try:
        future = producer.send(TOPIC, value=sensor)

        # Wait until Kafka acknowledges the message
        future.get(timeout=10)

        print("✓ Sent Sensor Data")
        print(json.dumps(sensor, indent=4))
        print("=" * 60)

    except Exception as e:
        print(f"❌ Failed to send message: {e}")

    time.sleep(interval)    