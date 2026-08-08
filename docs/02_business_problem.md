
````markdown
# Business Problem

## 1. Background

Cold-chain logistics involves the transportation of products that require controlled environmental conditions throughout their journey.

Examples include:

- Fruits and vegetables
- Frozen foods
- Pharmaceuticals
- Vaccines
- Other temperature-sensitive commodities

During transportation, environmental conditions inside a container can change continuously. Variations in temperature, humidity, vibration, vehicle speed, or other sensor conditions may affect the quality and safety of temperature-sensitive goods.

Monitoring these conditions continuously can help identify abnormal readings and provide better visibility into the condition of shipments.

---

## 2. Core Business Problem

Traditional shipment tracking mainly provides information such as:

- Origin
- Destination
- Container
- Shipment movement
- Delivery status

However, shipment location alone does not provide sufficient visibility into the environmental conditions experienced by the goods during transportation.

For example, a shipment may be moving normally between its origin and destination while the temperature inside the container moves outside the recommended range for the transported commodity.

This creates a need to monitor sensor data such as:

- Temperature
- Humidity
- Vibration
- Battery level
- Vehicle speed
- Latitude
- Longitude
- Timestamp

The business problem is therefore to build a system that can continuously collect, process, store, transform, and analyze this sensor information.

---

## 3. Example Business Scenario

Consider a refrigerated container transporting a temperature-sensitive commodity.

The commodity has a defined recommended temperature range.

For example:

```text
Commodity: Temperature-Sensitive Product
Recommended Temperature Range: 2°C – 6°C
````

During transportation, the simulator may generate readings such as:

```text
10:00:00 → 4.5°C
10:00:05 → 5.1°C
10:00:10 → 5.8°C
10:00:15 → 6.4°C
10:00:20 → 7.2°C
```

The later readings indicate that the temperature has moved outside the recommended range.

A monitoring system should therefore make it possible to identify:

* Which container generated the reading?
* Which commodity was being transported?
* What was the recorded temperature?
* What was the recommended temperature range?
* Was the reading within or outside the expected range?
* What was the humidity at the same time?
* What was the container's battery level?
* What was the vehicle speed and location?
* What risk level was associated with the shipment?

AtmoSync addresses these requirements by generating and analyzing continuous sensor readings.

---

## 4. Environmental Monitoring Challenge

Sensor readings can change continuously during transportation.

For example:

```text
10:00:00 → Temperature: 5.1°C
10:00:05 → Temperature: 5.2°C
10:00:10 → Temperature: 5.4°C
10:00:15 → Temperature: 5.8°C
10:00:20 → Temperature: 6.3°C
```

When multiple containers generate readings at regular intervals, the volume of data can increase rapidly.

A data platform is therefore required to:

* Capture continuous sensor readings
* Stream the readings through a real-time messaging system
* Store the incoming data
* Transform raw data into structured models
* Combine sensor information with reference data
* Generate analytical metrics
* Present the results through dashboards

---

## 5. Data Quality Challenge

Real-world sensor systems may occasionally produce missing or abnormal readings.

To make the simulation more representative of real-world IoT data, AtmoSync introduces controlled data-quality variations.

The simulator currently uses:

```text
Temperature Missing Probability : 5%
Humidity Missing Probability    : 3%
Temperature Spike Probability   : 1%
```

Temperature spikes are simulated by temporarily increasing the generated temperature value.

Missing values are represented as `NULL` in the generated sensor data.

This allows the downstream pipeline to process data that is not always perfectly complete or consistent.

---

## 6. Commodity-Specific Monitoring

Different commodities require different environmental conditions.

AtmoSync therefore generates sensor readings based on commodity-specific configuration.

The simulator uses commodity-level information such as:

* Commodity
* Category
* Temperature range
* Humidity range
* Vibration range
* Latitude range
* Longitude range

This allows the system to generate more realistic sensor readings for different categories of transported goods.

The process can be represented as:

```text
Commodity
    ↓
Commodity Category
    ↓
Expected Environmental Conditions
    ↓
Simulated Sensor Reading
```

The resulting data can then be compared and analyzed across commodities and categories.

---

## 7. Business Need

A cold-chain monitoring solution should provide visibility into:

* Current sensor readings
* Historical sensor readings
* Temperature trends
* Temperature alerts
* Humidity conditions
* Vibration levels
* Battery levels
* Container activity
* Shipment volume
* Commodity distribution
* Shipment category distribution
* Risk-level distribution
* Route information

The objective is not simply to collect sensor data but to transform the data into useful information for monitoring and analysis.

---

## 8. Proposed AtmoSync Solution

AtmoSync implements an end-to-end data engineering and analytics pipeline.

The implemented workflow is:

```text
Python IoT Simulator
        ↓
JSON Sensor Events
        ↓
Apache Kafka
        ↓
Snowflake RAW
        ↓
dbt Staging
        ↓
dbt Dimension & Fact Models
        ↓
Snowflake MARTS
        ↓
Apache Superset
        ↓
Monitoring & Analytics
```

Each component performs a specific role in the pipeline.

### Python IoT Simulator

The Python simulator generates continuous sensor readings for different commodities and containers.

The generated data includes:

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

The simulator also introduces controlled missing values and temperature spikes to represent potential sensor-data quality issues.

### Apache Kafka

Apache Kafka provides the real-time streaming layer.

The Kafka Producer publishes the generated sensor events, while the Kafka Consumer receives the events and inserts them into Snowflake.

This creates a continuous flow of sensor data from the simulator to the data warehouse.

### Snowflake

Snowflake acts as the central cloud data warehouse.

The raw sensor readings are initially stored in:

```text
RAW.SENSOR_READINGS_RAW
```

The transformed analytical datasets are stored in the MARTS layer.

The project includes analytical models such as:

```text
MARTS.DIM_CONTAINER
MARTS.DIM_ROUTE
MARTS.FACT_SENSOR_READINGS
```

### dbt

dbt is used to transform the raw Snowflake data into structured and analytics-ready models.

The transformation flow includes:

```text
RAW.SENSOR_READINGS_RAW
            ↓
STAGING.STG_SENSOR_READINGS
            ↓
     ┌──────┼──────────────┐
     ↓      ↓              ↓
DIM_CONTAINER  DIM_ROUTE  FACT_SENSOR_READINGS
```

The dbt models separate raw ingestion from analytical structures and make the resulting data easier to query and analyze.

### Apache Superset

Apache Superset provides the analytical dashboard layer.

The AtmoSync dashboard provides visual monitoring of the processed sensor data.

The dashboard includes metrics and visualizations such as:

* Total sensor readings
* Active containers
* Temperature alerts
* Average battery level
* Temperature trends by category
* Temperature alerts by container
* Shipment distribution by risk level
* Commodity distribution
* Shipment category distribution
* Top commodities by shipment volume
* Container activity
* Recent sensor readings

Interactive filters allow users to explore the data by dimensions such as:

* Risk level
* Commodity
* Destination
* Container
* Category

---

## 9. Key Business Questions

The AtmoSync analytics solution is designed to support questions such as:

* How many sensor readings have been recorded?
* How many containers are represented in the dataset?
* Which containers have the highest number of temperature alerts?
* Which commodities are being transported most frequently?
* How are shipments distributed across risk levels?
* How do temperature readings vary across commodity categories?
* What is the average battery level across containers?
* Which containers show abnormal temperature readings?
* How are shipments distributed across different categories?
* Which routes and destinations are represented in the shipment data?
* What are the most recent sensor readings?
* Are missing or abnormal sensor readings present in the dataset?

---

## 10. Expected Business Value

AtmoSync demonstrates how IoT sensor data can be converted into structured analytical information through a modern data engineering pipeline.

The solution provides:

* Continuous sensor-data visibility
* Centralized historical data storage
* Structured analytical data models
* Temperature monitoring
* Environmental-condition analysis
* Container-level analysis
* Commodity-level analysis
* Route-level analysis
* Risk-level analysis
* Interactive dashboard-based monitoring
* A foundation for further cold-chain analytics

The project demonstrates the integration of real-time data streaming, cloud data warehousing, data transformation, and business intelligence.

---

## 11. Problem Statement

Cold-chain transportation involves continuously changing environmental conditions that can affect temperature-sensitive goods. Basic shipment tracking does not provide sufficient visibility into the sensor conditions experienced by individual containers.

AtmoSync addresses this challenge by implementing an end-to-end pipeline that simulates IoT sensor readings, streams the data through Apache Kafka, stores the raw readings in Snowflake, transforms the data using dbt, creates analytical dimension and fact models, and presents the resulting information through an interactive Apache Superset dashboard.

The objective is to provide a centralized analytical view of sensor conditions, container activity, commodity distribution, temperature alerts, shipment risk, and other operational metrics that can support cold-chain monitoring and data-driven analysis.

```

