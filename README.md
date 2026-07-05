#  AtmoSync – Micro-Climate Arbitrage Analytics

> An Advanced Data Analytics & Engineering project focused on real-time cold-chain monitoring, spoilage-risk analysis, and data-driven logistics decision support.

##  Project Overview

AtmoSync is an end-to-end real-time data analytics platform designed to monitor environmental conditions inside cold-chain shipping containers.

The project simulates IoT sensor data such as temperature, humidity, vibration, GPS location, speed, and battery level. The planned pipeline streams this data through Apache Kafka, stores it in Snowflake, transforms it using dbt and SQL, and visualizes actionable insights through Apache Superset dashboards.

The objective is to help logistics teams identify abnormal environmental conditions, detect potential spoilage risks, monitor shipment health, and support better operational decisions.

---

##  Business Problem

Perishable goods such as fruits, vegetables, dairy products, pharmaceuticals, and vaccines require controlled environmental conditions during transportation.

Unexpected events such as:

- Cooling system failure
- Door opening
- High humidity
- Temperature excursions
- Traffic delays
- Rough-road conditions
- Excessive vibration
- Low sensor battery

can increase the risk of product degradation and financial loss.

AtmoSync aims to transform continuous sensor readings into meaningful analytics that help answer questions such as:

- Which containers are currently at risk?
- Which shipments exceeded their safe temperature range?
- How long did a container remain outside safe conditions?
- Which routes experience more environmental disruptions?
- Which commodities are most vulnerable to spoilage?
- What operational action should be prioritized?

---

##  Planned System Architecture

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
        (Raw Data Layer)
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
