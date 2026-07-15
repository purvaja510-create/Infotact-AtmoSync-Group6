import json
from kafka import KafkaConsumer

TOPIC = "container_sensor"
BOOTSTRAP_SERVER = "localhost:9092"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVER,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("📥 Kafka Consumer Started...\n")

for message in consumer:
    print("=" * 50)
    print("Received Sensor Data:")
    print(json.dumps(message.value, indent=4))