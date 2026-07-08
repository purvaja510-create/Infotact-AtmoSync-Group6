
# Business Problem

## 1. Background

Cold-chain logistics is used to transport products that must remain within controlled environmental conditions throughout their journey.

Examples include:

- Fruits and vegetables
- Dairy products
- Frozen foods
- Medicines
- Vaccines
- Other temperature-sensitive goods

These products are often transported in refrigerated trucks or containers.

During transportation, environmental and operational conditions may change. If these changes are not detected and analyzed in time, they can affect product quality and increase the risk of spoilage or financial loss.

---

## 2. Core Business Problem

A shipment may begin its journey under safe conditions but experience problems during transportation.

Possible issues include:

- Cooling system failure
- Unexpected temperature increase
- High or unstable humidity
- Container door opening
- Traffic delays
- Rough-road conditions
- Excessive vibration
- Low monitoring-device battery
- Longer-than-expected journey duration

These events may affect the internal environment of the container.

For example, if a cooling system fails, the temperature may gradually rise above the safe range for the commodity being transported.

The business therefore needs better visibility into:

- What is happening inside the container?
- Which container is experiencing abnormal conditions?
- When did the problem begin?
- How long did the unsafe condition continue?
- Which event may have contributed to the problem?
- Which shipment may require immediate attention?

---

## 3. Example Business Scenario

Consider a refrigerated container carrying apples.

Assume the safe temperature range is:

```text
2°C to 6°C
```

At the beginning of the journey:

```text
Container ID: C001
Commodity: Apples
Temperature: 4.5°C
Status: Normal
```

The cooling system later begins to fail.

The temperature changes gradually:

```text
10:00 AM → 4.5°C
10:05 AM → 5.1°C
10:10 AM → 5.8°C
10:15 AM → 6.4°C
10:20 AM → 7.2°C
10:25 AM → 8.1°C
```

The temperature has now exceeded the safe maximum of 6°C.

This creates important business questions:

- When did the temperature first exceed the safe range?
- How long did the excursion continue?
- What was the maximum temperature?
- Was a cooling failure event recorded?
- Is the container repeatedly experiencing unsafe conditions?
- Should the shipment be prioritized for operational attention?

AtmoSync aims to generate and analyze the data required to answer such questions.

---

## 4. Limitations of Basic Shipment Tracking

Traditional shipment tracking often focuses on:

- Current location
- Source
- Destination
- Estimated arrival time
- Delivery status

However, location information alone does not explain the environmental condition inside a refrigerated container.

For example:

```text
Shipment Status: On Time
Location: Near Destination
```

This may appear normal.

But internally:

```text
Temperature: 9.2°C
Safe Maximum: 6°C
Cooling Status: Failure
```

The shipment may be moving correctly while the product environment is unsafe.

Therefore, logistics monitoring should consider both:

```text
Shipment Movement Data
        +
Environmental Sensor Data
        +
Operational Event Data
```

---

## 5. Data Visibility Challenge

Cold-chain monitoring can generate continuous time-series data.

For example:

```text
10:00:00 → Temperature 5.1°C
10:00:05 → Temperature 5.2°C
10:00:10 → Temperature 5.4°C
10:00:15 → Temperature 5.8°C
10:00:20 → Temperature 6.3°C
```

When multiple containers generate readings continuously, the volume of data increases quickly.

The business therefore needs a pipeline capable of:

- Generating or receiving continuous sensor data
- Streaming events
- Storing historical readings
- Transforming raw data
- Calculating analytical metrics
- Visualizing trends and risks

---

## 6. Business Need

A useful cold-chain analytics solution should support:

- Continuous monitoring of container conditions
- Historical sensor analysis
- Temperature trend analysis
- Humidity monitoring
- Vibration monitoring
- Operational event tracking
- Temperature excursion detection
- Time-outside-safe-range analysis
- Container-level risk indicators
- Route-level comparisons
- Commodity-level comparisons
- Interactive dashboards

The objective is not only to collect data but to transform it into information that supports decisions.

---

## 7. Proposed AtmoSync Solution

AtmoSync proposes an end-to-end Advanced Data Analytics and Data Engineering pipeline.

The planned workflow is:

```text
Python IoT Simulator
        ↓
JSON Sensor Events
        ↓
Apache Kafka
        ↓
Snowflake
        ↓
dbt + SQL
        ↓
Analytics-Ready Models
        ↓
Apache Superset
        ↓
Business Insights
```

Each component has a specific responsibility.

### Python IoT Simulator

Python will simulate realistic sensor and journey data because physical IoT sensors are not available for the project.

Planned readings include:

- Temperature
- Humidity
- Vibration
- Battery level
- Latitude
- Longitude
- Vehicle speed
- Event type

### Apache Kafka

Kafka will act as the real-time event-streaming layer.

It will support the continuous movement of sensor events from the Python simulator toward downstream processing and storage.

### Snowflake

Snowflake will act as the cloud data warehouse.

It will store:

- Raw sensor events
- Historical readings
- Structured shipment data
- Analytics-related datasets

### dbt and SQL

dbt and SQL will transform raw warehouse data into clean and analytics-ready models.

Potential transformations include:

- Temperature deviation
- Temperature excursion detection
- Time outside safe range
- Event counts
- Container risk indicators
- Route-level metrics
- Commodity-level metrics

### Apache Superset

Apache Superset will provide dashboards and visualizations.

Potential dashboard areas include:

- Operations monitoring
- Risk and alerts
- Advanced analytics
- Executive insights

---

## 8. Operational Events

AtmoSync may simulate business events such as:

- `NORMAL`
- `DOOR_OPEN`
- `COOLING_FAILURE`
- `TRAFFIC_DELAY`
- `ROUGH_ROAD`
- `BATTERY_LOW`

These events should influence sensor behavior.

### Example: Cooling Failure

```text
COOLING_FAILURE
        ↓
Temperature begins increasing
        ↓
Safe maximum may be exceeded
        ↓
Temperature excursion occurs
        ↓
Risk indicator increases
        ↓
Container may require attention
```

### Example: Rough Road

```text
ROUGH_ROAD
        ↓
Vibration increases
        ↓
Repeated high-vibration readings
        ↓
Potential handling concern
```

### Example: Traffic Delay

```text
TRAFFIC_DELAY
        ↓
Vehicle speed decreases
        ↓
Journey duration may increase
        ↓
Shipment exposure time increases
```

---

## 9. Key Business Questions

AtmoSync aims to support questions such as:

- Which containers are currently outside safe temperature conditions?
- Which containers experience repeated temperature excursions?
- How long does each container remain outside its safe range?
- Which container recorded the highest temperature deviation?
- Which routes experience more operational disruptions?
- Which commodities experience more environmental exceptions?
- How frequently do cooling failures occur?
- Which containers show repeated abnormal patterns?
- Which shipments may require operational attention?
- How do environmental conditions change over time?

---

## 10. Expected Business Value

AtmoSync aims to demonstrate how streaming and historical sensor data can support:

- Better shipment visibility
- Faster identification of abnormal conditions
- Historical trend analysis
- Temperature excursion analysis
- Container-level monitoring
- Route-level analysis
- Commodity-level analysis
- Better operational prioritization
- Data-driven decision support

---

## 11. Problem Statement

Cold-chain shipments are exposed to changing environmental and operational conditions during transportation. Basic shipment tracking alone may not provide sufficient visibility into temperature, humidity, vibration, cooling failures, delays, and other events that can affect product conditions.

AtmoSync aims to address this problem by simulating continuous IoT sensor data, streaming events through a real-time data pipeline, storing historical records in a cloud data warehouse, transforming raw observations into analytics-ready models, and presenting meaningful insights through interactive dashboards.

The overall objective is to identify abnormal shipment conditions, analyze environmental and operational patterns, and support better logistics decisions.
