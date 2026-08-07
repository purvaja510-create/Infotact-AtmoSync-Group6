import random
import json
import time
from datetime import datetime

from simulator.config import *

# ---------------------------------------------------------
# Reading ID Counter
# ---------------------------------------------------------

reading_counter = 1


def get_reading_id():
    global reading_counter
    reading_id = f"R{reading_counter:06d}"
    reading_counter += 1
    return reading_id


# ---------------------------------------------------------
# Missing Value Simulation
# ---------------------------------------------------------

def maybe_missing(value, probability):
    if random.random() < probability:
        return None
    return value


# ---------------------------------------------------------
# Temperature Spike Simulation
# ---------------------------------------------------------

def maybe_temperature_spike(temperature, probability):

    if random.random() > probability:
        return temperature

    chance = random.random()

    if chance < 0.70:
        spike = random.uniform(0.5, 1.5)   # Minor deviation
    elif chance < 0.95:
        spike = random.uniform(1.5, 3)     # Moderate deviation
    else:
        spike = random.uniform(4, 7)       # Rare critical deviation

    return round(temperature + spike, 2)

# ---------------------------------------------------------
# Generate Sensor Data
# ---------------------------------------------------------

def generate_sensor_data():

    commodity = random.choice(list(Commodities.keys()))

    commodity_details = Commodities.get(commodity, {})

    category = commodity_details.get("Category", "Unknown")

    origin, destination = random.choice(Routes)

    latitude = round(
        random.uniform(
            *City_coordinates[origin]["latitude_range"]
        ),
        6
    )

    longitude = round(
        random.uniform(
            *City_coordinates[origin]["longitude_range"]
        ),
        6
    )

    temperature = round(
        random.uniform(*commodity_details["Temp_range"]),
        2
    )

    humidity = random.randint(
        *commodity_details["Humidity_range"]
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

    battery_level = random.randint(*battery_range)

    speed = round(
        random.uniform(*speed_range),
        1
    )

    vibration = round(
        random.uniform(
            *commodity_details["Vibration_range"]
        ),
        2
    )


    sensor = {

        "Reading_ID": get_reading_id(),

        "Container_id": random.choice(Containers),

        "Commodity": commodity,

        "Category": category,

        "Origin": origin,

        "Destination": destination,

        "Temperature": temperature,

        "Humidity": humidity,

        "Vibration": vibration,

        "Battery_Level": battery_level,

        "Speed": speed,

        "Latitude": latitude,

        "Longitude": longitude,

        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return sensor


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 50)
    print("      AtmoSync IoT Simulator Started")
    print("=" * 50)

    while True:

        sensor = generate_sensor_data()

        print(json.dumps(sensor, indent=4))

        print("=" * 60)

        time.sleep(interval)


if __name__ == "__main__":
    main()