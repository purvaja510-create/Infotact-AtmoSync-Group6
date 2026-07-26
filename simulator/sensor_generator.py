import random
import json
import time
from datetime import datetime

from simulator.config import *


def maybe_missing(value, probability):
    if random.random() < probability:
        return None
    return value


def maybe_temperature_spike(temperature, probability):
    if random.random() < probability:
        return round(random.uniform(20, 40), 2)
    return temperature


def generate_sensor_data():

    commodity = random.choice(list(Commodities.keys()))
    
    
    temperature = round(
        random.uniform(*Commodities[commodity]["Temp_range"]), 2
    )

    humidity = random.randint(
        *Commodities[commodity]["Humidity_range"]
    )

    temperature = maybe_temperature_spike(
        temperature,
        temperature_spike_probability
    )

    temperature = maybe_missing(
        temperature,
        temperature_missing_probability
    )

    humidity = maybe_missing(
        humidity,
        humidity_missing_probability
    )

    # New fields
    battery_level = random.randint(*battery_range)

    speed = round(
        random.uniform(*speed_range),
        1
    )

    route = random.choice(Route)

    sensor = {

        "Container_id": random.choice(Containers),

        "Commodity": commodity,


        "Origin":  route["origin"],

        "Destination": route["destination"],

        "Route_id": route["route_id"],

        "Transport_mode": route["transport_mode"],

        "Container_status": random.choice(container_status),

        "Temperature": temperature,

        "Humidity": humidity,

        "Vibration": round(
            random.uniform(
                *Commodities[commodity]["Vibration_range"]
            ),
            2
        ),

        "Battery_Level": battery_level,

        "Speed": speed,

        "Latitude": round(
            random.uniform(
                *route["Latitude_range"]
            ),
            6
        ),

        "Longitude": round(
            random.uniform(
                *route["Longitude_range"]
            ),
            6
        ),

        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }

    return sensor


def main():
    print("AtmoSync IoT Simulator Started...\n")

    while True:
        sensor = generate_sensor_data()

        print(json.dumps(sensor, indent=4))
        print("=" * 50)

        time.sleep(interval)


if __name__ == "__main__":
    main()