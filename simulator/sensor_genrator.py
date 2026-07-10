import random
import json
import time
from datetime import datetime

from config import *

def genrate_sensor_data():
    Commodity= random.choice(list(Commodities.keys()))

    sensor={
        "Container_id": random.choice(Containers),

        "Commodity":Commodity,

        "Temperature": round(
            random.uniform(
                *Commodities[Commodity]["temp_range"]),2),

        "Humidity": round(
            random.uniform(
                *Commodities[Commodity]["humidity_range"]),2),

        "Vibartion": round(
            random.uniform(
                *Commodities[Commodity]["vibration_range"]),2),

        "Latitude": round(
            random.uniform(
                *Commodities[Commodity]["latitude_range"]),6),

        "Longitude":round(
            random.uniform(
                *Commodities[Commodity]["longitude_range"]),6),
            
        "timestamp": datetime.now().strftime("%d/%m%Y/,%H:%M:%S")
    }
    return sensor

def main():
    print("AtmoSync LoT Simulator Started...\n")

    while True:
        sensor= genrate_sensor_data()

        print(json.dumps(sensor,indent=4))
        print("-"*50)
        time.sleep(interval)

if __name__ == "__main__":
    main()
