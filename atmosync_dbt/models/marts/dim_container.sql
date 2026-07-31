{{ config(materialized='table') }}

SELECT DISTINCT

    container_id

FROM {{ ref('stg_sensor_readings') }}

ORDER BY container_id