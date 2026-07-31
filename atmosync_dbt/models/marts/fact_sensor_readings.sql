SELECT

    s.reading_id,

    s.timestamp,

    s.container_id,

    s.commodity,

    s.category,

    cp.price_per_kg,

    cp.shelf_life_days,

    cp.optimal_temp_min,

    cp.optimal_temp_max,

    cp.risk_level,

    CONCAT(s.source, ' -> ', s.destination) AS route_key,

    s.source,

    s.destination,

    s.temperature,

    s.humidity,

    s.vibration,

    s.battery_level,

    s.speed,

    s.latitude,

    s.longitude

FROM {{ ref('stg_sensor_readings') }} s

LEFT JOIN {{ source('raw', 'commodity_pricing') }} cp
    ON s.commodity = cp.commodity