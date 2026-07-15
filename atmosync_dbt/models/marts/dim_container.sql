{{ config(materialized='table') }}

SELECT DISTINCT
    container_id,
    commodity,
    source,
    destination

FROM {{ ref('stg_sensor_readings') }}

ORDER BY container_id