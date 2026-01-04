# Setup Guide – AgentFlow

## Requirements
- **Python 3.10** (Windows) or 3.10+ on WSL/Linux
- **Apache Kafka** (for messaging)
- Optional: **Apache Airflow** (for DAG orchestration; Linux/WSL recommended)
- Intel OpenVINO (if using ML model optimization)
- Git (for cloning repository)

---

## Install Dependencies

```bash
# Create and activate virtual environment (Linux / WSL)
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
# Or manually
pip install kafka-python openvino
```
---
## Kafka Setup
 ### Start Zookeeper:
```
Bash
# Inside Kafka folder
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```
### Start Kafka Broker:
```
Bash
cd C:\kafka\kafka_2.13-3.6.1
bin\windows\kafka-server-start.bat config\server.properties
```
### Create topic agentflow-input if not already created:
```
Bash
bin\windows\kafka-topics.bat --create ^
 --topic agentflow-input ^
 --bootstrap-server localhost:9092 ^
 --partitions 1 ^
 --replication-factor 1
```
---
## Running AgentFlow
### Start the Kafka Consumer
```
Bash
python kafka/consumer.py
```
### Send input queries using Producer
```
Bash
python kafka/producer.py
```
## Observe logs and output in the console.
---

## Airflow Integration
### Set AIRFLOW_HOME:

```
Bash
export AIRFLOW_HOME=$(pwd)/airflow_home   # Linux / WSL
setx AIRFLOW_HOME "C:\path\to\project\airflow_home" # Windows
```
### Initialize database:
```
Bash
airflow db init
```
### Create admin user:
```
Bash
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```
### Start Airflow Webserver:
```
Bash
airflow webserver -p 8080
```
### Trigger DAG manually:
```
Bash
airflow dags trigger agentflow_dag
```
## Notes
Airflow on Windows: Recommended to use WSL2 or Docker

Memory / storage: In-memory for demo purposes

Agents: Reference Agent, Research Agent, Collab Agent
