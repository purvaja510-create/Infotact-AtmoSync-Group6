````markdown
# System Architecture

## 1. Architecture Overview

AtmoSync follows an end-to-end data pipeline that moves sensor data from simulation through real-time streaming, storage, transformation, and visualization.

```text
IoT Simulator
      ↓
Kafka Producer
      ↓
Kafka Broker
      ↓
Kafka Consumer
      ↓
Snowflake RAW
      ↓
dbt Staging
      ↓
dbt Dimension & Fact Models
      ↓
Snowflake MARTS
      ↓
Apache Superset Dashboard
````

## 2. Architecture Components

### IoT Simulator

The Python-based simulator generates sensor readings for containers transporting different commodities.

The generated data includes parameters such as:

* Temperature
* Humidity
* Vibration
* Battery Level
* Speed
* Location
* Timestamp
* Container and commodity information

### Apache Kafka

Kafka provides the real-time streaming layer.

```text
IoT Simulator → Kafka Producer → Kafka Broker → Kafka Consumer
```

The Producer publishes sensor events, while the Consumer receives the events for storage.

### Snowflake

Snowflake is used as the central data warehouse.

The incoming sensor data is stored in the RAW layer:

```text
RAW.SENSOR_READINGS_RAW
```

### dbt

dbt performs the transformation and modeling of the Snowflake data.

The transformation flow is:

```text
RAW.SENSOR_READINGS_RAW
          ↓
STAGING.STG_SENSOR_READINGS
          ↓
   ┌──────┼──────────────┐
   ↓      ↓              ↓
DIM_CONTAINER
DIM_ROUTE
FACT_SENSOR_READINGS
```

The resulting models are stored in the Snowflake `MARTS` schema.

### Apache Superset

Apache Superset connects to the analytics-ready data in Snowflake MARTS and provides interactive dashboards for monitoring sensor readings and shipment conditions.

## 3. Data Flow Summary

```text
Generate → Stream → Ingest → Store → Transform → Model → Visualize
```

The architecture separates raw data, transformation logic, analytical models, and visualization, providing a structured pipeline for AtmoSync.
