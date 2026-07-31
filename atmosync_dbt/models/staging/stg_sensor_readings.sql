SELECT


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

    LONGITUDE,

    INGESTED_AT

FROM {{ source('raw', 'sensor_readings_raw') }}