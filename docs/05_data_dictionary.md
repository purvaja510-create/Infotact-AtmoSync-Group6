
````markdown
# Data Dictionary

## Fact Sensor Readings

| Field | Description |
|---|---|
| READING_ID | Unique identifier for each sensor reading |
| TIMESTAMP | Date and time when the reading was generated |
| CONTAINER_ID | Identifier of the shipping container |
| COMMODITY | Commodity being transported |
| CATEGORY | Category of the transported commodity |
| TEMPERATURE | Temperature recorded by the sensor |
| HUMIDITY | Humidity recorded by the sensor |
| VIBRATION | Vibration level recorded by the sensor |
| BATTERY_LEVEL | Sensor/device battery level |
| SPEED | Vehicle speed at the time of reading |
| LATITUDE | Geographic latitude of the container |
| LONGITUDE | Geographic longitude of the container |
| SOURCE | Shipment origin |
| DESTINATION | Shipment destination |
| ROUTE_KEY | Route connecting source and destination |
| RISK_LEVEL | Risk classification of the shipment condition |
| PRICE_PER_KG | Commodity price per kilogram |
| SHELF_LIFE_DAYS | Expected shelf life of the commodity |
| OPTIMAL_TEMP_MIN | Minimum recommended temperature |
| OPTIMAL_TEMP_MAX | Maximum recommended temperature |

## Dimension Tables

### DIM_CONTAINER

Contains container-level information used to identify and analyze individual containers.

### DIM_ROUTE

Contains route-related information including source, destination, and route identification.

### COMMODITY_PRICING

Contains commodity-level information such as category, pricing, shelf life, and recommended temperature range.

## Data Layers

```text
RAW
 ↓
STAGING
 ↓
MARTS
````

* **RAW** – Incoming sensor data stored from the streaming pipeline.
* **STAGING** – Cleaned and standardized data created using dbt.
* **MARTS** – Analytics-ready dimension and fact models used by the dashboard.
