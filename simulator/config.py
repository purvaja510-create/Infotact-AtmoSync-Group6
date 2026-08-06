# AtmoSync IoT Simulator Configuration

# ---------------------------------------------------------
# Simulation Settings
# ---------------------------------------------------------

SIMULATION_INTERVAL_SECONDS = 5

# ---------------------------------------------------------
# Container IDs
# ---------------------------------------------------------

Containers = [
    "A101",
    "A102",
    "A103",
    "A104",
    "A105",
    "A106",
    "A107",
    "A108",
    "A109",
    "A110",
    "A111",
    "A112",
    "A113",
    "A114",
    "A115"
]

# ---------------------------------------------------------
# Valid Transportation Routes
# ---------------------------------------------------------

Routes = [

    ("Mumbai", "Delhi"),
    ("Mumbai", "Jaipur"),
    ("Mumbai", "Ahmedabad"),
    ("Mumbai", "Goa"),

    ("Pune", "Hyderabad"),
    ("Pune", "Nagpur"),
    ("Pune", "Lucknow"),

    ("Nashik", "Delhi"),
    ("Nashik", "Jaipur"),

    ("Hyderabad", "Chennai"),
    ("Hyderabad", "Bengaluru"),
    ("Hyderabad", "Kolkata"),

    ("Bengaluru", "Chennai"),
    ("Bengaluru", "Kochi"),

    ("Kochi", "Mumbai"),
    ("Kochi", "Bengaluru"),

    ("Ahmedabad", "Chandigarh"),
    ("Ahmedabad", "Delhi"),

    ("Indore", "Bhopal"),
    ("Indore", "Delhi"),

    ("Nagpur", "Raipur"),
    ("Nagpur", "Hyderabad"),

    ("Visakhapatnam", "Bhubaneswar"),

    ("Lucknow", "Patna"),

    ("Kolkata", "Guwahati"),

    ("Delhi", "Amritsar"),

    ("Chennai", "Coimbatore"),

    ("Surat", "Pune")
]

# ---------------------------------------------------------
# Commodity Master
# ---------------------------------------------------------

Commodities = {

    # =====================================================
    # FRUITS
    # =====================================================

    "Apple": {
        "Category": "Fruits",
        "Temp_range": (0, 4),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (34.0, 34.8),
        "Longitude_range": (74.0, 75.2)
    },

    "Banana": {
        "Category": "Fruits",
        "Temp_range": (13, 15),
        "Humidity_range": (85, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (16.5, 18.0),
        "Longitude_range": (80.0, 81.5)
    },

    "Mango": {
        "Category": "Fruits",
        "Temp_range": (10, 13),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (17.0, 19.5),
        "Longitude_range": (73.0, 75.5)
    },

    "Orange": {
        "Category": "Fruits",
        "Temp_range": (3, 8),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (20.0, 22.0),
        "Longitude_range": (78.0, 80.0)
    },

    "Grapes": {
        "Category": "Fruits",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (19.0, 20.5),
        "Longitude_range": (73.0, 74.5)
    },

    "Pineapple": {
        "Category": "Fruits",
        "Temp_range": (7, 10),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (10.0, 11.5),
        "Longitude_range": (76.0, 77.5)
    },

    "Strawberries": {
        "Category": "Fruits",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (18.5, 19.5),
        "Longitude_range": (73.0, 74.0)
    },

    "Papaya": {
        "Category": "Fruits",
        "Temp_range": (10, 13),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (16.0, 18.0),
        "Longitude_range": (78.0, 79.5)
    },

    # =====================================================
    # VEGETABLES
    # =====================================================

    "Tomato": {
        "Category": "Vegetables",
        "Temp_range": (8, 12),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (22.0, 23.5),
        "Longitude_range": (75.0, 76.5)
    },

    "Potato": {
        "Category": "Vegetables",
        "Temp_range": (4, 8),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (22.0, 23.5),
        "Longitude_range": (75.0, 76.5)
    },

    "Onion": {
        "Category": "Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (65, 75),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (20.0, 21.0),
        "Longitude_range": (74.0, 75.0)
    },

    "Carrot": {
        "Category": "Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (30.0, 31.0),
        "Longitude_range": (76.0, 77.0)
    },

    "Cabbage": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (30.0, 31.0),
        "Longitude_range": (76.0, 77.0)
    },

    "Cauliflower": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (30.0, 31.0),
        "Longitude_range": (76.0, 77.0)
    },

    "Capsicum": {
        "Category": "Vegetables",
        "Temp_range": (7, 10),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Green Peas": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (30.0, 31.0),
        "Longitude_range": (76.0, 77.0)
    },
    
    # =====================================================
    # EXOTIC FRUITS & VEGETABLES
    # =====================================================

    "Avocados": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (4, 8),
        "Humidity_range": (65, 80),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Kiwi": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 1),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Dragon Fruit": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (5, 10),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Broccoli": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Asparagus": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (2, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Lettuce": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    # =====================================================
    # FROZEN FOODS
    # =====================================================

    "Frozen Fish": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (9.5, 10.5),
        "Longitude_range": (76.0, 77.0)
    },

    "Frozen Prawns": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (9.5, 10.5),
        "Longitude_range": (76.0, 77.0)
    },

    "Frozen Chicken": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (12.5, 13.5),
        "Longitude_range": (77.0, 78.0)
    },

    "Frozen Meat": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (19.0, 20.0),
        "Longitude_range": (72.5, 73.5)
    },

    "Frozen Peas": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (30.0, 31.0),
        "Longitude_range": (76.0, 77.0)
    },

    "Frozen Corn": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (22.0, 23.5),
        "Longitude_range": (75.0, 76.5)
    },

    "Ice Cream": {
        "Category": "Frozen Foods",
        "Temp_range": (-25, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (19.0, 20.0),
        "Longitude_range": (72.5, 73.5)
    },

    "Frozen French Fries": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00),
        "Latitude_range": (19.0, 20.0),
        "Longitude_range": (72.5, 73.5)
    },

    # =====================================================
    # PHARMACEUTICALS
    # =====================================================

    "Vaccines": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Medicines": {
        "Category": "Pharmaceuticals",
        "Temp_range": (15, 25),
        "Humidity_range": (35, 60),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Insulin": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Blood Plasma": {
        "Category": "Pharmaceuticals",
        "Temp_range": (-30, -20),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Antibiotics": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    },

    "Biologics": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50),
        "Latitude_range": (17.0, 18.0),
        "Longitude_range": (78.0, 79.0)
    }

}

# ---------------------------------------------------------
# Vehicle Telemetry
# ---------------------------------------------------------

speed_range = (30, 90)      # km/h
battery_range = (40, 100)   # %

# ---------------------------------------------------------
# Data Quality Simulation
# ---------------------------------------------------------

temperature_missing_probability = 0.05
humidity_missing_probability = 0.03
temperature_spike_probability = 0.01

# ---------------------------------------------------------
# Simulation Interval
# ---------------------------------------------------------

interval = 5