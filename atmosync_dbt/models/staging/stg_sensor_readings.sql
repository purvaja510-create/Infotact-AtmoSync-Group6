SELECT
    TIMESTAMP,
    CONTAINER_ID,
    COMMODITY,
    SOURCE,
    DESTINATION,
    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    BATTERY_LEVEL,
    SPEED,
    INGESTED_AT

FROM {{ source('raw', 'sensor_readings_raw') }}