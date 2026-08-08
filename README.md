# AtmoSync – Micro-Climate Arbitrage Analytics

> **An Advanced Data Analytics & Engineering platform for real-time cold-chain monitoring, environmental risk analysis, shipment intelligence, and data-driven logistics decision support.**

## Project Overview

**AtmoSync** is an end-to-end **real-time data analytics and engineering platform** designed to monitor and analyze environmental conditions across temperature-sensitive cold-chain shipments.

The platform simulates IoT sensor events containing operational and environmental attributes such as **temperature, humidity, vibration, GPS location, speed, battery level, commodity, route, and timestamp**. These events are continuously streamed through **Apache Kafka**, ingested into **Snowflake**, transformed and modeled using **dbt and SQL**, and exposed through **Apache Superset** for interactive analytics and operational monitoring.

The solution combines **real-time data ingestion, cloud data warehousing, analytical data modeling, data quality management, KPI development, risk classification, and interactive visualization** into a single analytics workflow.

The primary objective is to transform continuously generated sensor data into **actionable business intelligence** that enables logistics teams to monitor shipment health, identify environmental anomalies, assess spoilage risk, and prioritize operational interventions.

### Key Analytical Objectives

* Monitor environmental conditions across active shipments and containers.
* Detect **temperature excursions and other abnormal sensor conditions**.
* Identify containers and shipments with elevated operational risk.
* Analyze environmental trends across commodities, routes, and containers.
* Compare shipment activity and distribution across locations and categories.
* Monitor sensor health indicators such as battery levels.
* Provide near-real-time visibility into recent sensor readings.
* Support data-driven decisions around **shipment monitoring, risk prioritization, and cold-chain operations**.

---

## Business Problem

Cold-chain logistics requires maintaining controlled environmental conditions throughout transportation. Products such as **fruits, vegetables, frozen foods, pharmaceuticals, and vaccines** can experience quality degradation when exposed to unsuitable temperature or environmental conditions.

Traditional shipment tracking primarily provides information about **where a shipment is located**, but does not necessarily provide sufficient visibility into the environmental conditions affecting the cargo.

During transportation, factors such as:

* Cooling-system failures
* Temperature excursions
* High or low humidity
* Door-opening events
* Traffic delays
* Rough-road conditions
* Excessive vibration
* Low sensor battery
* Route-specific environmental disruptions

can increase the probability of **product degradation, spoilage, shipment loss, and operational inefficiency**.

AtmoSync addresses this problem by converting continuous IoT-style sensor events into a structured analytical data model and providing an interactive monitoring layer for operational analysis.

### Key Business Questions

The platform is designed to help answer questions such as:

* **Which containers are currently at elevated risk?**
* **Which shipments have experienced temperature excursions?**
* **Which commodities are most exposed to environmental risk?**
* **Which containers generate the highest number of temperature alerts?**
* **How do temperature and humidity conditions change over time?**
* **Which routes and locations show higher shipment activity or disruption patterns?**
* **What is the current health of active containers and their sensors?**
* **Which shipments or conditions should receive operational attention first?**

This transforms raw sensor telemetry into **business-oriented operational intelligence** rather than simply displaying sensor readings.

---

## End-to-End System Architecture

```text
┌──────────────────────────────────────┐
│ Container & Route Configuration      │
│ Commodity & Storage Parameters       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Python IoT Simulator          │
│                                      │
│ Temperature • Humidity • Vibration   │
│ GPS • Speed • Battery • Commodity    │
│ Route • Timestamp • Risk Attributes  │
└──────────────────┬───────────────────┘
                   │
                   ▼
          JSON Sensor Events
                   │
                   ▼
┌──────────────────────────────────────┐
│        Apache Kafka Producer         │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│            Kafka Topic               │
│       Real-Time Event Streaming      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Apache Kafka Consumer         │
│     Validation & Data Ingestion      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       Snowflake RAW Layer            │
│                                      │
│ SENSOR_READINGS_RAW                  │
│ COMMODITY_PRICING                    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│             dbt + SQL                │
│     Transformation & Data Modeling   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       Snowflake STAGING              │
│                                      │
│ STG_SENSOR_READINGS                  │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│         Snowflake MARTS              │
│                                      │
│ DIM_CONTAINER                        │
│ DIM_ROUTE                            │
│ FACT_SENSOR_READINGS                 │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       Apache Superset                │
│     Analytics & Visualization        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Operational Dashboards & Insights    │
│                                      │
│ KPIs • Temperature Trends            │
│ Alerts • Risk Analysis               │
│ Commodity Analysis • Route Analysis │
│ Container Monitoring • Live Readings │
└──────────────────────────────────────┘
```

### Pipeline Flow

**Generate → Stream → Ingest → Store → Transform → Model → Analyze → Decide**

The architecture separates **real-time ingestion** from **analytical transformation**, allowing raw sensor events to be preserved while providing a structured, analytics-ready data layer for downstream reporting and decision support.

---

## Data & Analytics Architecture

The Snowflake environment is organized into three logical analytical layers:

### 1. RAW Layer

The RAW layer preserves source-level data received from the streaming pipeline.

**Primary datasets:**

* `SENSOR_READINGS_RAW`
* `COMMODITY_PRICING`

This layer provides a persistent representation of the incoming data before analytical transformations are applied.

### 2. STAGING Layer

The STAGING layer provides a cleaned and standardized analytical representation of the raw sensor data.

**Model:**

* `STG_SENSOR_READINGS`

This layer acts as the transformation boundary between source data and business-facing analytical models.

### 3. MARTS Layer

The MARTS layer contains the final analytics-ready dimensional and fact models.

**Models:**

* `DIM_CONTAINER` – container-level analytical information.
* `DIM_ROUTE` – origin, destination, and route information.
* `FACT_SENSOR_READINGS` – sensor measurements and analytical attributes at the sensor-event grain.

This structure enables downstream dashboards and analysis to work with **reusable, structured analytical models rather than raw streaming data**.

---

## Advanced Analytics & Business Intelligence

The analytical layer is designed to provide visibility across multiple dimensions of cold-chain operations.

### Operational KPIs

The dashboard provides high-level indicators including:

* Total sensor readings
* Active containers
* Temperature alerts
* Average battery level

### Environmental Monitoring

Environmental conditions can be analyzed through:

* Temperature trends
* Temperature trends by commodity category
* Humidity trends
* Temperature alerts by container
* Recent sensor readings
* Abnormal environmental conditions

### Shipment & Risk Analysis

The platform supports analysis of:

* Shipment distribution by risk level
* Commodity distribution
* Shipment category distribution
* Container activity
* Source and destination patterns
* Route-level shipment activity

### Sensor-Level Monitoring

Recent sensor records provide visibility into:

* Timestamp
* Container ID
* Commodity
* Category
* Temperature
* Humidity
* Battery level
* Source
* Destination
* Risk level

This allows users to move from **high-level KPIs → analytical trends → individual sensor events** within the same monitoring workflow.

---

## Data Quality & Realistic Simulation

The IoT simulator was designed to generate realistic shipment-level events rather than simple random values.

Sensor behavior incorporates **commodity-specific storage requirements and operational characteristics**, allowing different categories of cargo to exhibit different environmental ranges.

The simulation also incorporates controlled data-quality conditions to make the analytical pipeline representative of real-world data engineering scenarios, including:

* Missing temperature values
* Missing humidity values
* Controlled temperature anomalies
* Commodity-specific temperature ranges
* Battery-level variation
* Route and location variation
* Shipment and container-level risk classification

This provides an environment for demonstrating not only dashboard development but also **data validation, transformation, anomaly analysis, and analytical modeling**.

---

## Technology Stack

| Technology          | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| **Python**          | IoT sensor simulation and data generation              |
| **Apache Kafka**    | Real-time event streaming                              |
| **Docker**          | Containerized Kafka and ZooKeeper runtime              |
| **Snowflake**       | Cloud data warehouse and analytical storage            |
| **dbt**             | SQL-based transformation and data modeling             |
| **SQL**             | Data transformation, modeling, and analytical logic    |
| **Apache Superset** | Interactive analytics and dashboarding                 |
| **Git & GitHub**    | Version control, collaboration, and project management |

---

## Analytical Outcome

AtmoSync demonstrates how raw, continuously generated IoT telemetry can be transformed into an **analytics-ready decision-support system**.

The completed pipeline enables:

**IoT Simulation**
→ **Real-Time Streaming**
→ **Cloud Data Ingestion**
→ **Data Transformation**
→ **Dimensional & Fact Modeling**
→ **Operational Analytics**
→ **Risk Monitoring**
→ **Business Decision Support**

The result is an integrated analytics platform that combines **data engineering, real-time processing, cloud warehousing, analytical modeling, and business intelligence** to address a practical cold-chain logistics problem.

---

### Project Status

**Status: Completed**

The implemented solution includes the Python IoT simulator, Kafka streaming pipeline, Snowflake RAW/STAGING/MARTS layers, dbt transformations, analytical models, and Apache Superset monitoring dashboards. The project also includes exported analytical datasets and supporting evidence for implementation in the repository. 
