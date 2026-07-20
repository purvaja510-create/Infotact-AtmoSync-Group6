SELECT


    s.timestamp,

    s.container_id,

    dc.commodity,

    cp.category,

    cp.price_per_kg,

    dr.route_key,

    dr.source,

    dr.destination,

    s.temperature,

    s.humidity,

    s.vibration,

    s.battery_level,

    s.speed

FROM {{ ref('stg_sensor_readings') }} s

LEFT JOIN {{ ref('dim_container') }} dc
    ON s.container_id = dc.container_id

LEFT JOIN {{ ref('dim_route') }} dr
    ON dc.source = dr.source
   AND dc.destination = dr.destination

LEFT JOIN {{ source('raw', 'commodity_pricing') }} cp
    ON dc.commodity = cp.commodity