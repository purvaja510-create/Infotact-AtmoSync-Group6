{{ config(materialized='table') }}

SELECT DISTINCT

    CONCAT(source, ' -> ', destination) AS route_key,

    source,
    destination

FROM {{ ref('stg_sensor_readings') }}

ORDER BY
    source,
    destination 