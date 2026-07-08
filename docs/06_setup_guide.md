# Setup Guide

## 1. Purpose

This document describes the planned development environment and setup process for the AtmoSync project.

AtmoSync uses the following technology stack:

```text
Python IoT Simulator
        ↓
Apache Kafka
        ↓
Snowflake
        ↓
dbt + SQL
        ↓
Apache Superset
```

Git and GitHub are used for version control and team collaboration.

> Note: The project is currently under active development. Setup steps may evolve during implementation and integration.

---

## 2. Development Tools

The project may require the following tools:

| Tool | Purpose |
|---|---|
| Python | IoT sensor and journey simulation |
| VS Code | Code development |
| Git | Local version control |
| GitHub | Repository collaboration |
| Apache Kafka | Real-time event streaming |
| Snowflake | Cloud data warehouse |
| dbt | Data transformation and analytics modeling |
| SQL | Querying and business logic |
| Apache Superset | Dashboard and visualization layer |

---

## 3. Team Setup Responsibility

Not every team member needs to configure every technology immediately.

The tentative responsibility structure is:

| Role | Main Tools |
|---|---|
| Team Lead / Integration | GitHub, integration, Superset |
| Python Data Engineer | Python, simulator libraries |
| Streaming / Warehouse Engineer | Kafka, Snowflake |
| Analytics Engineer | dbt, SQL, documentation |

Team members may install additional tools when integration testing requires them.

---

## 4. Git and GitHub Setup

### Step 1: Install Git

Download and install Git from the official Git website.

Verify installation:

```bash
git --version
```

Expected output:

```text
git version x.x.x
```

---

### Step 2: Configure Git Identity

Set your Git username:

```bash
git config --global user.name "Your Name"
```

Set the email address associated with your GitHub account:

```bash
git config --global user.email "your-email@example.com"
```

Verify:

```bash
git config --global --list
```

---

### Step 3: Clone the Repository

Clone the AtmoSync repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Infotact-AtmoSync-Group6
```

---

### Step 4: Check Available Branches

```bash
git branch -a
```

---

### Step 5: Work on Your Assigned Branch

Switch to your assigned branch:

```bash
git checkout <your-branch-name>
```

Example:

```bash
git checkout purvaja510-create
```

Verify:

```bash
git branch
```

The active branch will be marked with `*`.

---

## 5. Python Environment Setup

### Step 1: Install Python

Install a stable Python 3 version.

Verify:

```bash
python --version
```

On some systems:

```bash
python3 --version
```

---

### Step 2: Create a Virtual Environment

From the project directory:

```bash
python -m venv .venv
```

---

### Step 3: Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

---

### Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

### Step 5: Install Project Dependencies

Once the project dependency file is finalized:

```bash
pip install -r requirements.txt
```

> The final `requirements.txt` should be updated as implementation progresses.

---

## 6. Planned Python Simulator Setup

The simulator is expected to generate:

- Timestamp
- Container ID
- Commodity
- Temperature
- Humidity
- Vibration
- Battery level
- Latitude
- Longitude
- Speed
- Event type

A possible simulator structure is:

```text
simulator/
├── main.py
├── container.py
├── sensor.py
├── journey.py
├── events.py
├── generator.py
├── risk_engine.py
└── config.py
```

The exact structure may evolve during development.

---

## 7. Apache Kafka Setup

Kafka is planned as the real-time streaming layer.

The intended flow is:

```text
Python Simulator
        ↓
Kafka Producer
        ↓
Kafka Topic
        ↓
Kafka Consumer
        ↓
Downstream Storage
```

### Planned Kafka Components

- Kafka broker
- Producer
- Topic
- Consumer

A possible topic name is:

```text
sensor-events
```

### Kafka Validation Goals

During implementation, verify that:

- Producer can connect to Kafka
- JSON messages are published successfully
- Topic receives messages
- Consumer can read messages
- Message structure is valid
- Events arrive continuously
- Downstream ingestion works correctly

> Exact Kafka installation commands depend on the selected local or containerized deployment approach. The team should finalize one common approach before implementation.

---

## 8. Snowflake Setup

Snowflake is planned as the cloud data warehouse.

A possible logical structure is:

```text
ATMOSYNC_DB
│
├── RAW
├── STAGING
└── ANALYTICS
```

### RAW Layer

Stores incoming source-level data.

Example:

```text
RAW.SENSOR_EVENTS
```

### STAGING Layer

Contains cleaned and standardized data.

Example:

```text
STAGING.STG_SENSOR_EVENTS
```

### ANALYTICS Layer

Contains business-ready models.

Examples:

```text
ANALYTICS.CONTAINER_RISK
ANALYTICS.TEMPERATURE_EXCURSIONS
ANALYTICS.ROUTE_PERFORMANCE
```

### Snowflake Setup Tasks

The Snowflake owner may need to:

- Create or configure the project account
- Create database
- Create schemas
- Create tables
- Configure roles and permissions
- Test SQL queries
- Validate incoming records
- Prepare connectivity for dbt
- Prepare connectivity for Superset

> Final database, schema, warehouse, and role names should be agreed by the team before implementation.

---

## 9. dbt Setup

dbt is planned as the transformation and analytics-modeling layer.

For a local dbt Core approach, the analytics engineer may create a Python environment and install the Snowflake adapter.

Example:

```bash
pip install dbt-core dbt-snowflake
```

Verify:

```bash
dbt --version
```

### Planned dbt Flow

```text
Snowflake Raw Data
        ↓
dbt Staging Models
        ↓
Intermediate Models
        ↓
Analytics / Mart Models
        ↓
Superset
```

### Possible dbt Project Structure

```text
dbt/
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
├── seeds/
├── tests/
└── dbt_project.yml
```

### Potential dbt Models

```text
stg_sensor_events
int_temperature_excursions
int_container_events
mart_container_risk
mart_route_performance
mart_commodity_analysis
```

### Planned dbt Commands

Check configuration:

```bash
dbt debug
```

Run models:

```bash
dbt run
```

Run tests:

```bash
dbt test
```

Build models and tests:

```bash
dbt build
```

> Credentials must not be committed to GitHub. Connection configuration should use secure local profiles or environment variables.

---

## 10. Apache Superset Setup

Apache Superset is planned as the dashboard and visualization layer.

The intended flow is:

```text
Snowflake Analytics Models
        ↓
Apache Superset
        ↓
Charts
        ↓
Dashboards
        ↓
Business Insights
```

Potential dashboards include:

- Operations Dashboard
- Risk and Alert Dashboard
- Advanced Analytics Dashboard
- Executive Dashboard

### Superset Setup Goals

- Configure Superset environment
- Connect to analytics-ready data
- Validate datasets
- Create charts
- Add filters
- Build dashboards
- Test dashboard behavior

> The final installation and deployment approach should be agreed by the team before implementation.

---

## 11. Environment Variables and Secrets

Sensitive credentials must not be stored directly in source code.

Examples include:

- Snowflake username
- Snowflake password
- Account identifier
- Database credentials
- API keys
- Other secrets

A local environment file may be used:

```text
.env
```

Example variable names:

```text
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_WAREHOUSE=
```

The `.env` file should be excluded from Git tracking.

Example `.gitignore` entries:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 12. Recommended Local Project Structure

```text
Infotact-AtmoSync-Group6/
│
├── simulator/
├── kafka/
│   ├── producer/
│   └── consumer/
├── snowflake/
│   ├── schema/
│   └── sql/
├── dbt/
│   ├── models/
│   └── seeds/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── docs/
├── presentation/
├── images/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 13. GitHub Collaboration Workflow

Each member should work on their assigned branch.

```text
Assigned Branch
        ↓
Make Changes
        ↓
Test Changes
        ↓
Commit
        ↓
Push
        ↓
Create Pull Request
        ↓
Review
        ↓
Merge into main
```

Avoid direct changes to `main`.

---

## 14. Recommended Commit Messages

Examples:

```text
docs: add project setup guide
```

```text
feat: add initial IoT sensor simulator
```

```text
feat: add Kafka producer
```

```text
feat: add Snowflake raw sensor schema
```

```text
feat: add dbt staging model
```

```text
fix: correct temperature excursion logic
```

---

## 15. Setup Validation Checklist

### GitHub

- [x] Repository cloned successfully
- [x] Correct branch selected
- [x] Git identity configured
- [x] Push access tested

### Python

- [ ] Python installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Simulator can run

### Kafka

- [ ] Kafka environment configured
- [ ] Producer connection tested
- [ ] Topic available
- [ ] Consumer receives messages

### Snowflake

- [ ] Account access available
- [ ] Database created
- [ ] Schemas created
- [ ] Raw table created
- [ ] SQL queries tested

### dbt

- [ ] dbt environment configured
- [ ] Snowflake connection tested
- [ ] `dbt debug` succeeds
- [ ] Models run successfully
- [ ] Tests run successfully

### Superset

- [ ] Superset environment configured
- [ ] Data source connection tested
- [ ] Dataset available
- [ ] Initial chart created

---

## 16. Current Status

This setup guide represents the planned development environment for AtmoSync.

As implementation progresses, the team should update this document with:

- Final installation method
- Confirmed software versions
- Exact configuration steps
- Final Kafka approach
- Final Snowflake objects
- Final dbt project structure
- Final Superset connection process
- Known issues and troubleshooting steps

The document should evolve with the actual implementation of the project.
