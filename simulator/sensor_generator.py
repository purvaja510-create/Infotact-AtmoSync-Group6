import random
import json
import time
from datetime import datetime

from simulator.config import *

def maybe_missing(value,probability):
    if random.random()<probability:
        return None
    return value

def maybe_temperature_spike(temperature,probabitiy):
    if random.random()<probabitiy:
        return round(random.uniform(20,40),2)
    return temperature

def generate_sensor_data():
    commodity= random.choice(list(Commodities.keys()))

    temperature=round(random.uniform(*Commodities[commodity]["temp_range"]),2)

    humidity=random.randint(*Commodities[commodity]["humidity_range"])

    temperature=maybe_temperature_spike(temperature,temperature_spike_probability)

    temperature=maybe_missing(temperature,temperature_missing_probability)

    humidity=maybe_missing(humidity,humidity_missing_probability)

    sensor={
        "Container_id": random.choice(Containers),

        "commodity":commodity,

        "Temperature": temperature,

        "Humidity": humidity,

        "Vibration": round(
            random.uniform(
                *Commodities[commodity]["vibration_range"]),2),

        "Latitude": round(
            random.uniform(
                *Commodities[commodity]["latitude_range"]),6),

        "Longitude":round(
            random.uniform(
                *Commodities[commodity]["longitude_range"]),6),
        
            
        "timestamp": datetime.now().strftime("%d/%m%Y/,%H:%M:%S")
    }
    return sensor

def main():
    print("AtmoSync IoT Simulator Started...\n")

    while True:
        sensor= generate_sensor_data()

        print(json.dumps(sensor,indent=4))
        print("-"*50)
        time.sleep(interval)

if __name__ == "__main__":
    main()
