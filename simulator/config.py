# Container Numbers
Containers = [
    "A101",
    "A102",
    "A103",
    "A104",
    "A105",
    "A106"
]

# Origin,Destination,Route Id and Transport Mode of the containers
Route =[
    {
        "origin": "Hyderabad",
        "destination": "Bengaluru",
        "route_id": "HYD-BLR-001",
        "transport_mode": "Air Cargo",
        "Latitude_range": (17.30, 17.55),
        "Longitude_range": (78.30, 78.60)
    },
    {
        "origin": "Chennai",
        "destination": "Kolkata",
        "route_id": "CHE-KOL-002",
        "transport_mode": "Cargo Train",
        "Latitude_range": (12.90, 13.20),
        "Longitude_range": (80.15, 80.35)
    },
    {
        "origin": "Hyderabad",
        "destination": "Mumbai",
        "route_id": "HYD-MUM-003",
        "transport_mode": "Cargo Train",
        "Latitude_range": (17.30, 17.55),
        "Longitude_range": (78.30, 78.60)
    },
    {
        "origin": "Kashi",
        "destination": "Jaipur",
        "route_id": "KAS-JAI-004",
        "transport_mode": "Refrigerated Truck",
        "Latitude_range": (25.20, 25.40),
        "Longitude_range": (82.90, 83.10)
    },
    {
        "origin": "Delhi",
        "destination": "Chandigarh",
        "route_id": "DEL-CHD-005",
        "transport_mode": "Cargo Train",
        "Latitude_range": (28.45, 28.75),
        "Longitude_range": (77.05, 77.30)
    },
    {
        "origin": "Goa",
        "destination": "Srinagar",
        "route_id": "GOA-SXR-006",
        "transport_mode": "Air Cargo",
        "Latitude_range": (15.35, 15.65),
        "Longitude_range": (73.75, 74.05)
    },
    {
        "origin": "Bhubaneswar",
        "destination": "Shimla",
        "route_id": "BBS-SML-007",
        "transport_mode": "Cargo Train",
        "Latitude_range": (20.20, 20.40),
        "Longitude_range": (85.75, 85.95)
    },
    {
        "origin": "India",
        "destination": "Sri Lanka",
        "route_id": "IND-LKA-IL010",
        "transport_mode": "Ocean Freight",
        "Latitude_range": (8.00, 13.00),
        "Longitude_range": (76.00, 80.50)
    },
    {
        "origin": "India",
        "destination": "Australia",
        "route_id": "IND-AUS-IA020",
        "transport_mode": "Ocean Freight",
        "Latitude_range": (8.00, 13.00),
        "Longitude_range": (76.00, 80.50)
    },
    {
        "origin": "Korea",
        "destination": "America",
        "route_id": "KOR-USA-KA030",
        "transport_mode": "Air Cargo",
        "Latitude_range": (37.40, 37.70),
        "Longitude_range": (126.80, 127.20)
    },
    {
        "origin": "Korea",
        "destination": "India",
        "route_id": "KOR-IND-KI040",
        "transport_mode": "Ocean Freight",
        "Latitude_range": (35.00, 37.80),
        "Longitude_range": (126.00, 129.50)
    }

]

# Statues of the conatainers
container_status = [
    "In Transit",
    "Delivered", 
    "Delayed", 
    "At warehouse", 
    "In Customs", 
    "Out for Delivery", 
    "Awaiting Pickup"
    ]


# Commodities with their details
Commodities = {
    "Avocado": {
        "Temp_range": (4, 8),
        "Humidity_range": (65, 80),
        "Vibration_range": (0.10, 1.00)
    },

    "Banana": {
        "Temp_range": (13, 15),
        "Humidity_range": (85, 95),
        "Vibration_range": (0.10, 1.00)
    },

    "Mango": {
        "Temp_range": (10, 13),
        "Humidity_range": (80, 90),
        "Vibration_range": (0.10, 1.00)
    },

    "Medicine": {
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 1.00)
    },

    "Vaccine": {
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (17.30, 17.50)
    },

    "Vegetables": {
        "Temp_range": (5, 10),
        "Humidity_range": (65, 90),
        "Vibration_range": (0.10, 1.00)
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