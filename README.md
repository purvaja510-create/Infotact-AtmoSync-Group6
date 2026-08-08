
````markdown
# AtmoSync – Micro-Climate Arbitrage Analytics

> An Advanced Data Analytics & Engineering project focused on real-time cold-chain monitoring, spoilage-risk analysis, and data-driven logistics decision support.

## Project Overview

AtmoSync is an end-to-end real-time data analytics platform designed to monitor environmental conditions inside cold-chain shipping containers.

The project simulates IoT sensor data including temperature, humidity, vibration, GPS location, speed, battery level, commodity, and route information. The data is streamed through Apache Kafka, stored in Snowflake, transformed using dbt and SQL, and analyzed through Apache Superset dashboards.

The objective is to identify abnormal environmental conditions, assess shipment risk, monitor container health, and support data-driven logistics decisions.

---

## Business Problem

Perishable goods such as fruits, vegetables, frozen foods, pharmaceuticals, and vaccines require controlled environmental conditions during transportation.

Unexpected conditions such as:

- Temperature excursions
- Cooling-system failures
- High humidity
- Excessive vibration
- Traffic delays
- Low sensor battery
- Route-related disruptions

can increase the risk of product degradation and financial loss.

AtmoSync transforms continuous sensor readings into actionable analytics to help answer questions such as:

- Which containers are currently at risk?
- Which shipments experienced temperature alerts?
- Which commodities show higher environmental risk?
- Which containers generate the most alerts?
- How do environmental conditions vary across routes and shipments?
- Which shipments require operational attention?

---

## System Architecture

```text
Container & Route Configuration
              │
              ▼
      Python IoT Simulator
              │
              ▼
        JSON Sensor Events
              │
              ▼
      Apache Kafka Producer
              │
              ▼
          Kafka Topic
              │
              ▼
      Apache Kafka Consumer
              │
              ▼
   Snowflake Data Warehouse
      (RAW Data Layer)
              │
              ▼
          dbt + SQL
   (Transformation & Modeling)
              │
              ▼
    Analytics-Ready Data Models
              │
              ▼
      Apache Superset
              │
              ▼
 Dashboards, Insights & Decisions
````

---

## Technology Stack

* **Python** – IoT sensor simulation and data generation
* **Apache Kafka** – Real-time event streaming
* **Snowflake** – Cloud data warehouse
* **dbt & SQL** – Data transformation and analytical modeling
* **Apache Superset** – Analytics dashboards and visualization
* **Docker** – Containerized infrastructure
* **Git & GitHub** – Version control and collaboration
