import sys
import os
import json
import time
from kafka import KafkaProducer

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.insert(0, project_root)

from simulator.sensor_generator import generate_sensor_data
from kafka_config import BOOTSTRAP_SERVER, TOPIC

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

while True:
    sensor = generate_sensor_data()

    producer.send(TOPIC, value=sensor)
    producer.flush()

    print("Sent:", sensor)

    time.sleep(5)