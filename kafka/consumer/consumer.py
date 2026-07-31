import os
import sys
import json

from kafka import KafkaConsumer

# ---------------------------------------------------------
# Project Path
# ---------------------------------------------------------

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.insert(0, project_root)

# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------

from snowflake_db.connection import get_connection

TOPIC = "container_sensor"
BOOTSTRAP_SERVER = "localhost:9092"

# ---------------------------------------------------------
# Kafka Consumer
# ---------------------------------------------------------

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVER,
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("=" * 55)
print("      AtmoSync Kafka Consumer Started")
print("=" * 55)

# ---------------------------------------------------------
# Snowflake Connection
# ---------------------------------------------------------

conn = get_connection()
cursor = conn.cursor()

insert_query = """
INSERT INTO RAW.SENSOR_READINGS_RAW
(
    READING_ID,
    TIMESTAMP,
    CONTAINER_ID,
    COMMODITY,
    CATEGORY,
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
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# ---------------------------------------------------------
# Consume Messages
# ---------------------------------------------------------

try:

    for message in consumer:

        data = message.value

        print(json.dumps(data, indent=4))
        print("=" * 60)

        cursor.execute(
            insert_query,
            (
                data["Reading_ID"],
                data["Timestamp"],
                data["Container_id"],
                data["Commodity"],
                data["Category"],
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

        print(f"✅ Inserted {data['Reading_ID']} into Snowflake")

except KeyboardInterrupt:

    print("\nStopping Consumer...")

finally:

    cursor.close()
    conn.close()