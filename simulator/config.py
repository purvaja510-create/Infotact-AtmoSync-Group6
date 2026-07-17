# Containers Numbers
Containers=[
"A101",
"A102",
"A103",
"A104",
"A105",
"A106"
]

# Commodities with there details
Commodities= {
    "Avocado": {
        "temp_range": (4,8),
        "humidity_range": (65,80),
        "vibration_range":(0.10, 1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    },
    "Banana":{
        "temp_range":(13,15),
        "humidity_range":(85,95),
        "vibration_range":(0.10,1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    },
    "Mango":{
        "temp_range":(10,13),
        "humidity_range":(80,90),
        "vibration_range":(0.10,1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    },
    "Medicine":{
        "temp_range":(2,8),
        "humidity_range":(30,50),
        "vibration_range":(0.10,1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    },
    "Vaccine":{
        "temp_range":(2,8),
        "humidity_range":(30,50),
        "vibration_range":(0.10,1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    },
    "Vegetables":{
        "temp_range":(10,16),   
        "humidity_range":(50,60),
        "vibration_range":(0.10,1.00),
        "latitude_range":(17.30,17.50),
        "longitude_range":(78.30, 78.60)
    }
}    

# Adding some missing values
temperature_missing_probability=0.5
humidity_missing_probability=0.3
temperature_spike_probability=0.2

interval=0.5