
````markdown
# Project Workflow

## 1. Overview

AtmoSync follows an end-to-end data engineering and analytics workflow that converts simulated IoT sensor readings into analytics-ready datasets and interactive business dashboards.

The complete project workflow is:

```text
Python IoT Simulator
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

Each component performs a specific role in moving the data from generation to analysis.

---

## 2. Step 1 – IoT Sensor Data Simulation

The workflow begins with the Python-based IoT simulator.

The simulator generates continuous sensor readings for different containers, commodities, routes, and environmental conditions.

Each generated reading contains information such as:

* Reading ID
* Container ID
* Commodity
* Category
* Origin
* Destination
* Temperature
* Humidity
* Vibration
* Battery level
* Speed
* Latitude
* Longitude
* Timestamp

The simulator uses commodity-specific configuration to generate realistic environmental readings.

It also introduces controlled data-quality variations:

```text
Temperature Missing Probability : 5%
Humidity Missing Probability    : 3%
Temperature Spike Probability   : 1%
```

This allows the pipeline to process both normal and imperfect sensor data.

---

## 3. Step 2 – Kafka Producer

The generated sensor data is converted into JSON sensor events.

The Kafka Producer publishes these events to the configured Kafka topic.

The Producer is responsible for:

1. Generating or receiving sensor data from the simulator
2. Serializing the sensor reading as JSON
3. Publishing the event to Kafka
4. Continuing to send readings at the configured interval

Example sensor event:

```json
{
    "Reading_ID": "R001435",
    "Container_id": "A105",
    "Commodity": "Asparagus",
    "Category": "Exotic Fruits & Vegetables",
    "Origin": "Bengaluru",
    "Destination": "Kochi",
    "Temperature": 3.3,
    "Humidity": 98,
    "Vibration": 0.35,
    "Battery_Level": 67,
    "Speed": 58.7,
    "Latitude": 13.046059,
    "Longitude": 77.663551,
    "Timestamp": "2026-08-07 21:31:30"
}
```

The Producer terminal confirms successful transmission of sensor events.

---

## 4. Step 3 – Kafka Broker

Apache Kafka acts as the real-time messaging layer between the Producer and Consumer.

The Kafka Broker receives the sensor events published by the Producer and makes them available to the Consumer.

The project uses Kafka infrastructure running through Docker.

The Kafka environment includes:

* Kafka
* ZooKeeper

The Docker environment can be verified using:

```text
docker ps
```

The running containers provide the infrastructure required for the streaming pipeline.

The overall streaming flow is:

```text
IoT Simulator
      ↓
Kafka Producer
      ↓
Kafka Broker
      ↓
Kafka Consumer
```

---

## 5. Step 4 – Kafka Consumer

The Kafka Consumer subscribes to the sensor-data stream and receives the events published by the Producer.

The Consumer performs the downstream ingestion step by:

1. Receiving JSON sensor events from Kafka
2. Deserializing the events
3. Processing the sensor records
4. Inserting the records into Snowflake

The Consumer terminal provides confirmation when a reading is successfully inserted.

Example:

```text
Inserted R001441 into Snowflake
Inserted R001442 into Snowflake
Inserted R001443 into Snowflake
```

This demonstrates the movement of sensor data from the Kafka streaming layer into the cloud data warehouse.

---

## 6. Step 5 – Snowflake RAW Layer

Snowflake acts as the central cloud data warehouse for the project.

The incoming sensor records are first stored in the RAW layer.

The main raw table is:

```text
RAW.SENSOR_READINGS_RAW
```

The RAW layer preserves the incoming sensor information before analytical transformations are applied.

The Snowflake database structure includes:

```text
ATMOSYNC_DB
│
├── RAW
│   └── SENSOR_READINGS_RAW
│
├── STAGING
│   └── STG_SENSOR_READINGS
│
└── MARTS
    ├── DIM_CONTAINER
    ├── DIM_ROUTE
    └── FACT_SENSOR_READINGS
```

This layered approach separates raw ingestion, transformation, and analytical datasets.

---

## 7. Step 6 – dbt Staging

After the raw sensor data is stored in Snowflake, dbt is used to transform the data.

The first transformation layer is the staging model:

```text
STAGING.STG_SENSOR_READINGS
```

The staging layer provides a structured representation of the raw sensor data and acts as the foundation for the downstream analytical models.

The workflow is:

```text
RAW.SENSOR_READINGS_RAW
          ↓
STAGING.STG_SENSOR_READINGS
```

---

## 8. Step 7 – dbt Dimension and Fact Models

The staged sensor data is then transformed into analytical dimension and fact models.

The project includes:

```text
DIM_CONTAINER
DIM_ROUTE
FACT_SENSOR_READINGS
```

The model structure can be represented as:

```text
                    STG_SENSOR_READINGS
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
       DIM_CONTAINER     DIM_ROUTE    FACT_SENSOR_READINGS
```

### Dimension Models

The dimension models provide descriptive information used for analysis.

#### DIM_CONTAINER

The container dimension represents container-related information used to analyze sensor readings at the container level.

#### DIM_ROUTE

The route dimension represents route-related information, including the relationship between shipment origins and destinations.

### Fact Model

#### FACT_SENSOR_READINGS

The fact model contains the analytical sensor-reading records used for monitoring and reporting.

It brings together sensor measurements and relevant descriptive information required for analytics.

---

## 9. Step 8 – dbt Execution

The dbt project is executed from the project environment using:

```text
dbt run
```

The dbt execution builds the required models in Snowflake.

A successful execution confirms that the transformation pipeline completed without errors.

The project execution shown during development included:

```text
4 models
8 data tests
1 seed
2 sources
```

The dbt run completed successfully with:

```text
PASS=4
WARN=0
ERROR=0
SKIP=0
NO-OP=0
```

The generated models include:

```text
STAGING.STG_SENSOR_READINGS
MARTS.DIM_CONTAINER
MARTS.DIM_ROUTE
MARTS.FACT_SENSOR_READINGS
```

---

## 10. Step 9 – Snowflake MARTS Layer

After the dbt transformations are completed, the analytics-ready models are available in the Snowflake MARTS layer.

The MARTS layer contains:

```text
MARTS.DIM_CONTAINER
MARTS.DIM_ROUTE
MARTS.FACT_SENSOR_READINGS
```

These models are designed for analytical queries and dashboard consumption rather than raw ingestion.

The resulting analytical structure can be represented as:

```text
RAW
 ↓
STAGING
 ↓
MARTS
 ├── DIM_CONTAINER
 ├── DIM_ROUTE
 └── FACT_SENSOR_READINGS
```

The resulting fact and dimension data can be queried directly in Snowflake to validate the transformation results.

---

## 11. Step 10 – Data Validation in Snowflake

After the dbt models are built, the resulting data can be queried in Snowflake.

For example:

```sql
SELECT *
FROM FACT_SENSOR_READINGS
LIMIT 20;
```

This allows the transformed records to be inspected and validated before they are consumed by the dashboard.

The Snowflake results contain analytical fields such as:

* Container ID
* Commodity
* Category
* Price per KG
* Shelf life
* Optimal temperature range
* Risk level
* Route
* Source
* Destination
* Temperature

This provides a final validation point between the transformation layer and the visualization layer.

---

## 12. Step 11 – Apache Superset Dashboard

The analytics-ready Snowflake MARTS data is connected to Apache Superset.

Superset provides the final visualization and monitoring layer of AtmoSync.

The dashboard is titled:

```text
AtmoSync Cold Chain Monitoring Dashboard
```

The dashboard provides key performance indicators and visualizations based on the transformed data.

---

## 13. Dashboard KPIs

The dashboard provides high-level monitoring metrics such as:

### Total Sensor Readings

Shows the total number of sensor records available in the analytical dataset.

### Active Containers

Shows the number of containers represented in the sensor data.

### Temperature Alerts

Shows the number of readings identified as being outside the expected temperature conditions.

### Average Battery

Shows the average battery level across the monitored containers.

These KPIs provide a quick overview of the current analytical dataset.

---

## 14. Dashboard Visualizations

The dashboard includes multiple visualizations for analyzing the sensor and shipment data.

Key visualizations include:

* Temperature Trend by Category
* Temperature Alerts by Container
* Shipment Distribution by Risk Level
* Commodity Distribution
* Shipment Category Distribution
* Top 10 Commodities by Shipment Volume
* Container Activity
* Recent Sensor Readings

These visualizations allow users to examine the data from different analytical perspectives.

---

## 15. Dashboard Filters

The dashboard provides interactive filters that allow users to explore specific subsets of the data.

Available filters include:

* Risk Level
* Commodity
* Destination
* Container
* Category

Users can combine these filters to investigate specific commodities, containers, destinations, categories, or risk levels.

---

## 16. End-to-End Data Flow

The complete AtmoSync workflow can be summarized as:

```text
┌──────────────────────────────┐
│      Python IoT Simulator    │
│                              │
│ Sensor + Container + Route   │
│ Environmental Data           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Kafka Producer        │
│      JSON Sensor Events      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Kafka Broker         │
│       Real-Time Stream       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Kafka Consumer        │
│      Data Ingestion          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Snowflake RAW          │
│    SENSOR_READINGS_RAW       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       dbt STAGING            │
│    STG_SENSOR_READINGS       │
└──────────────┬───────────────┘
               │
               ▼
       ┌───────┴────────┐
       │                │
       ▼                ▼
┌──────────────┐  ┌──────────────────┐
│ DIMENSIONS   │  │ FACT MODEL       │
│              │  │                  │
│ DIM_CONTAINER│  │ FACT_SENSOR_     │
│ DIM_ROUTE    │  │ READINGS         │
└───────┬──────┘  └────────┬─────────┘
        │                  │
        └────────┬─────────┘
                 ▼
┌──────────────────────────────┐
│       Snowflake MARTS        │
│  Analytics-Ready Data        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Apache Superset         │
│                              │
│ KPIs + Charts + Filters      │
│ + Recent Sensor Readings     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Business Monitoring      │
│       & Analytics            │
└──────────────────────────────┘
```

---

## 17. Final Workflow Summary

AtmoSync follows a complete data pipeline from sensor-data generation to business visualization.

The workflow is:

```text
Generate
   ↓
Stream
   ↓
Ingest
   ↓
Store
   ↓
Transform
   ↓
Model
   ↓
Validate
   ↓
Visualize
   ↓
Analyze
```

The integration of Python, Apache Kafka, Snowflake, dbt, SQL, and Apache Superset provides an end-to-end platform for processing and analyzing cold-chain sensor data.

The architecture separates real-time ingestion from data transformation and analytical reporting, allowing raw sensor data to be converted into structured datasets and finally presented through an interactive monitoring dashboard.

````

### For your documentation

Your `docs` folder can now have:

```text
docs/
│
├── 01_project_overview.md
├── 02_business_problem.md
├── 03_project_workflow.md      ← paste the above here
├── 04_system_architecture.md
├── 05_data_dictionary.md
├── 06_setup_guide.md
├── 07_analytics_kpis.md
├── 08_team_responsibilities.md
└── 09_testing_plan.md
````
