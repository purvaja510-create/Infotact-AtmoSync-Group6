# Container Numbers
Containers = [
    "A101",
    "A102",
    "A103",
    "A104",
    "A105",
    "A106"
]

# Origin and Destination of the containers
Origin = ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Kashi", "Delhi", "Pune", "Lucknow", "Jaipur"]
Destination = ["Goa", "Vizag", "Srinagar", "Bhubaneswar", "Kolkata", "Amritsar", "Chandigarh", "Dehradun", "Shimla"]

# Commodities with their details
Commodities = {
    "Avocado": {
        "Temp_range": (4, 8),
        "Humidity_range": (65, 80),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    },

    "Banana": {
        "Temp_range": (13, 15),
        "Humidity_range": (85, 95),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    },

    "Mango": {
        "Temp_range": (10, 13),
        "Humidity_range": (80, 90),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    },

    "Medicine": {
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    },

    "Vaccine": {
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    },

    "Vegetables": {
        "Temp_range": (5, 10),
        "Humidity_range": (65, 90),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50),
        "Longitude_range": (78.30, 78.60)
    }
}

# Vehicle telemetry
speed_range = (30, 90)      # km/h
battery_range = (40, 100)   # %

# Additional sensor values
temperature_missing_probability = 0.5
humidity_missing_probability = 0.3
temperature_spike_probability = 0.2

# Time interval (seconds)
interval = 0.2