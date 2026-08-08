
````markdown
# Setup Guide

## 1. Project Environment

AtmoSync uses the following technology stack:

```text
Python IoT Simulator
        ↓
Apache Kafka
        ↓
Snowflake RAW
        ↓
dbt
        ↓
Snowflake MARTS
        ↓
Apache Superset
````

Development and version control are managed using VS Code, Git, and GitHub.

---

## 2. Technology Stack

| Tool            | Purpose                                   |
| --------------- | ----------------------------------------- |
| Python          | IoT sensor data simulation                |
| Apache Kafka    | Real-time event streaming                 |
| Docker          | Kafka and Zookeeper container environment |
| Snowflake       | Cloud data warehouse                      |
| dbt             | Data transformation and modeling          |
| SQL             | Data querying and transformation          |
| Apache Superset | Dashboard and visualization               |
| Git & GitHub    | Version control and collaboration         |
| VS Code         | Development environment                   |

---

## 3. Repository Structure

The project repository is organized into the following major folders:

```text
Infotact-AtmoSync-Group6/
│
├── atmosync_dbt/
├── dashboard/
├── data/
├── dbt/
├── docs/
├── images/
├── kafka/
├── presentation/
├── simulator/
├── snowflake/
├── snowflake_db/
├── superset/
└── README.md
```

---

## 4. Python Environment

The project uses a Python virtual environment.

### Activate Environment – Windows

```text
.venv\Scripts\activate
```

### Check Python Version

```text
python --version
```

### Install Dependencies

```text
pip install -r requirements.txt
```

---

## 5. Kafka Environment

Kafka and Zookeeper are run using Docker.

The Kafka environment consists of:

```text
Kafka
Zookeeper
```

The data flow is:

```text
IoT Simulator
      ↓
Kafka Producer
      ↓
Kafka Broker
      ↓
Kafka Consumer
      ↓
Snowflake
```

The Producer publishes sensor events to Kafka, while the Consumer receives the events and inserts the sensor data into Snowflake.

---

## 6. Snowflake

Snowflake is used as the central cloud data warehouse.

The project uses the following database layers:

```text
ATMOSYNC_DB
│
├── RAW
├── STAGING
└── MARTS
```

### RAW

Stores incoming sensor readings.

```text
RAW.SENSOR_READINGS_RAW
```

### STAGING

Contains the cleaned staging model.

```text
STAGING.STG_SENSOR_READINGS
```

### MARTS

Contains analytics-ready models.

```text
MARTS.DIM_CONTAINER
MARTS.DIM_ROUTE
MARTS.FACT_SENSOR_READINGS
```

Commodity pricing data is also used during the transformation process.

---

## 7. dbt

dbt is used to transform the Snowflake RAW data into analytics-ready models.

The dbt transformation flow is:

```text
RAW.SENSOR_READINGS_RAW
          ↓
STAGING.STG_SENSOR_READINGS
          ↓
     ┌────┼────┐
     ↓    ↓    ↓
DIM_CONTAINER
DIM_ROUTE
FACT_SENSOR_READINGS
```

The dbt project is located in:

```text
atmosync_dbt/
```

Run the dbt transformations from the `atmosync_dbt` directory:

```text
dbt run
```

The completed dbt pipeline creates the required staging, dimension, and fact models in Snowflake.

---

## 8. Apache Superset

Apache Superset is used as the visualization layer.

The dashboard connects to the analytics-ready data in Snowflake MARTS.

The dashboard provides monitoring and analytical views including:

* Total Sensor Readings
* Active Containers
* Temperature Alerts
* Average Battery
* Temperature Trends
* Shipment Risk Distribution
* Commodity Distribution
* Container Activity
* Recent Sensor Readings

---

## 9. Git and GitHub

Git and GitHub are used for version control and team collaboration.

The project repository is:

```text
Infotact-AtmoSync-Group6
```

The general development workflow is:

```text
Create / Update Branch
        ↓
Make Changes
        ↓
Test Changes
        ↓
Commit
        ↓
Push
        ↓
Pull Request
        ↓
Review
        ↓
Merge
```

Team members work through separate branches and merge completed changes into the main project branch.

---

## 10. Project Pipeline

The complete implemented pipeline is:

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
dbt Staging Model
      ↓
dbt Dimension & Fact Models
      ↓
Snowflake MARTS
      ↓
Apache Superset
```

This setup enables AtmoSync to move sensor data from simulation through real-time streaming, cloud storage, transformation, analytical modeling, and dashboard visualization.
