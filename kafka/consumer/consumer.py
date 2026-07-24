import os
import sys

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.insert(0, project_root)

from snowflake_db.connection import get_connection
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

# Snowflake Connection
conn = get_connection()
cursor = conn.cursor()

insert_query = """
INSERT INTO RAW.SENSOR_READINGS_RAW
(
    TIMESTAMP,
    CONTAINER_ID,
    COMMODITY,
    SOURCE,
    DESTINATION,
    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    BATTERY_LEVEL,
    SPEED,
    LATITUDE,
    LONGITUDE
)
VALUES
(
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""

try:

    for message in consumer:

        data = message.value

        print("=" * 60)
        print(json.dumps(data, indent=4))

        cursor.execute(
            insert_query,
            (
                data["Timestamp"],
                data["Container_id"],
                data["Commodity"],
                data["Origin"],
                data["Destination"],
                data["Temperature"],
                data["Humidity"],
                data["Vibration"],
                data["Battery_Level"],
                data["Speed"],
                data["Latitude"],
                data["Longitude"]
            )
        )

        conn.commit()

        print("✅ Inserted into Snowflake")

except KeyboardInterrupt:
    print("Stopping Consumer...")

finally:
    cursor.close()
    conn.close()