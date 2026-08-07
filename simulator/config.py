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


# Origin,Destination,Route Id and Transport Mode of the containers
City_coordinates = {

    "Mumbai": {
        "latitude_range": (18.90, 19.25),
        "longitude_range": (72.75, 72.95)
    },

    "Pune": {
        "latitude_range": (18.45, 18.65),
        "longitude_range": (73.75, 73.95)
    },

    "Nashik": {
        "latitude_range": (19.90, 20.05),
        "longitude_range": (73.70, 73.90)
    },

    "Hyderabad": {
        "latitude_range": (17.30, 17.55),
        "longitude_range": (78.30, 78.60)
    },

    "Bengaluru": {
        "latitude_range": (12.85, 13.10),
        "longitude_range": (77.45, 77.75)
    },

    "Kochi": {
        "latitude_range": (9.90, 10.10),
        "longitude_range": (76.15, 76.40)
    },

    "Ahmedabad": {
        "latitude_range": (23.00, 23.15),
        "longitude_range": (72.45, 72.70)
    },

    "Indore": {
        "latitude_range": (22.65, 22.80),
        "longitude_range": (75.75, 75.95)
    },

    "Nagpur": {
        "latitude_range": (21.05, 21.25),
        "longitude_range": (78.95, 79.15)
    },

    "Visakhapatnam": {
        "latitude_range": (17.60, 17.80),
        "longitude_range": (83.20, 83.40)
    },

    "Lucknow": {
        "latitude_range": (26.75, 27.00),
        "longitude_range": (80.80, 81.05)
    },

    "Kolkata": {
        "latitude_range": (22.45, 22.70),
        "longitude_range": (88.25, 88.45)
    },

    "Delhi": {
        "latitude_range": (28.45, 28.75),
        "longitude_range": (77.05, 77.30)
    },

    "Chennai": {
        "latitude_range": (12.90, 13.20),
        "longitude_range": (80.15, 80.35)
    },

    "Surat": {
        "latitude_range": (21.10, 21.25),
        "longitude_range": (72.75, 72.95)
    }

}


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
        "Vibration_range": (0.10, 0.80)
    },

    "Banana": {
        "Category": "Fruits",
        "Temp_range": (13, 15),
        "Humidity_range": (85, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Mango": {
        "Category": "Fruits",
        "Temp_range": (10, 13),
        "Humidity_range": (80, 90),
        "Vibration_range": (0.10, 1.00)
    },


    "Orange": {
        "Category": "Fruits",
        "Temp_range": (3, 8),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80)
    },

    "Grapes": {
        "Category": "Fruits",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Pineapple": {
        "Category": "Fruits",
        "Temp_range": (7, 10),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80)
    },

    "Strawberries": {
        "Category": "Fruits",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Papaya": {
        "Category": "Fruits",
        "Temp_range": (10, 13),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80)
    },

    # =====================================================
    # VEGETABLES
    # =====================================================

    "Tomato": {
        "Category": "Vegetables",
        "Temp_range": (8, 12),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80)
    },

    "Potato": {
        "Category": "Vegetables",
        "Temp_range": (4, 8),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Onion": {
        "Category": "Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (65, 75),
        "Vibration_range": (0.10, 0.80)
    },

    "Carrot": {
        "Category": "Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    "Cabbage": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    "Cauliflower": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    "Capsicum": {
        "Category": "Vegetables",
        "Temp_range": (7, 10),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Green Peas": {
        "Category": "Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },
    
    # =====================================================
    # EXOTIC FRUITS & VEGETABLES
    # =====================================================

    "Avocados": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (4, 8),
        "Humidity_range": (65, 80),
        "Vibration_range": (0.10, 0.80)
    },

    "Kiwi": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 1),
        "Humidity_range": (90, 95),
        "Vibration_range": (0.10, 0.80)
    },

    "Dragon Fruit": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (5, 10),
        "Humidity_range": (85, 90),
        "Vibration_range": (0.10, 0.80)
    },

    "Broccoli": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    "Asparagus": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (2, 4),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    "Lettuce": {
        "Category": "Exotic Fruits & Vegetables",
        "Temp_range": (0, 2),
        "Humidity_range": (95, 100),
        "Vibration_range": (0.10, 0.80)
    },

    # =====================================================
    # FROZEN FOODS
    # =====================================================

    "Frozen Fish": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen Prawns": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen Chicken": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen Meat": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen Peas": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen Corn": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Ice Cream": {
        "Category": "Frozen Foods",
        "Temp_range": (-25, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    "Frozen French Fries": {
        "Category": "Frozen Foods",
        "Temp_range": (-20, -18),
        "Humidity_range": (40, 60),
        "Vibration_range": (0.10, 1.00)
    },

    # =====================================================
    # PHARMACEUTICALS
    # =====================================================

    "Vaccines": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50)
    },

    "Medicines": {
        "Category": "Pharmaceuticals",
        "Temp_range": (15, 25),
        "Humidity_range": (35, 60),
        "Vibration_range": (0.10, 0.50)
    },

    "Insulin": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50)
    },

    "Blood Plasma": {
        "Category": "Pharmaceuticals",
        "Temp_range": (-30, -20),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50)
    },

    "Antibiotics": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50)
    },

    "Biologics": {
        "Category": "Pharmaceuticals",
        "Temp_range": (2, 8),
        "Humidity_range": (30, 50),
        "Vibration_range": (0.10, 0.50)
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
temperature_spike_probability = 0.10

# ---------------------------------------------------------
# Simulation Interval
# ---------------------------------------------------------

interval = 5