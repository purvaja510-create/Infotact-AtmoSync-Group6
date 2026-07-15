{{ config(materialized='table') }}

SELECT DISTINCT
    source,
    destination

FROM {{ ref('stg_sensor_readings') }}

ORDER BY
    source,
    destination