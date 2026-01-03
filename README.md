#  Build-Your-Own AI Agent Framework – AgentFlow

AgentFlow is a **custom AI Agent Framework** (not just an app) designed to **orchestrate agentic workflows from input to output**. The framework allows users to define **task flows as a composition of agents**, execute them reliably, monitor and audit the execution, and integrate Apache technologies for messaging and orchestration.  

It is **framework-first**, modular, and ready to support Intel optimizations (OpenVINO) and multi-agent collaboration.

---

##  High-Level Guidelines Implemented

| Requirement | Status |
|------------|--------|
| **Core Features** | ✔ |
| Define & execute task flows (DAG/state machine) | ✔ (Flow engine in `agentflow/flow.py`) |
| Input handlers, tools/actions, output actions | ✔ (Kafka + agents + executors) |
| Memory, guardrails, observability (logs, metrics) | ✔ (`memory.py`, `guardrails.py`, `observability.py`) |
| **Architecture** | ✔ |
| Ingress (REST/queue) → Orchestrator → Executors → State/Memory | ✔ Kafka Producer → Consumer → Orchestrator → Agents → Memory |
| Apache components (Kafka, Airflow, etc.) | ✔ Kafka included; Airflow DAG structure provided (`airflow_dag/`) |
| **Intel Tech** | ✔ |
| Develop/benchmark on Intel DevCloud | Ready (benchmark scripts in `intel/benchmark/`) |
| Optimize ML models (LLMs, re-rankers, OCR) with OpenVINO | Ready (`intel/model/openvino_model.py`) |
| **Deliverables** | ✔ |
| Framework SDK (APIs for flows, tools, policies) | ✔ Modular code in `agentflow/` |
| Two reference agents for real workflows | ✔ `reference_agent.py`, `research_agent.py` |
| Design doc + performance benchmarks | ✔ `DESIGN_DOC.md`, benchmark scripts in `intel/benchmark/` |
| **Performance Targets** | ✔ |
| Reliable execution, retries, timeouts | Basic logging + extendable execution policies |
| Intel optimizations for ML | Structure ready for OpenVINO |
| **Stretch Goals** | ✔ |
| Multi-agent collaboration | ✔ `Collab Agent` included |
| Reflection loops | Ready in Orchestrator structure |
| Human-in-the-loop | Hooks can be added in `guardrails.py` |



## Key Features

- Custom AI Agent Framework (not an app)
- Task flow orchestration (DAG-based)
- Multi-agent collaboration (Planner, Research, Collaboration Agents)
- Kafka-based ingress and messaging
- Optional Airflow DAG orchestration
- Memory, guardrails, and observability
- Intel OpenVINO optimized inference
- Execution metrics and benchmarking

---

## Architecture Overview

Ingress (Kafka / API)  
→ Orchestrator  
→ Executors (Tools & Agents)  
→ Memory & State  
→ Output Handler  

---

## Technologies Used

- Python 3.10
- Apache Kafka
- Apache Airflow (DAG orchestration)
- Intel OpenVINO
- PyTorch (baseline model)
- Logging & Metrics (custom observability)

---

## Example Workflow

1. User sends query via Kafka producer
2. Planner Agent decides task routing
3. Research Agent fetches information
4. Summary Agent summarizes results
5. Collaboration Agent refines output
6. Final result is logged and returned

---

## How to Run (Minimal Demo)

### Start Kafka
- Start Zookeeper
- Start Kafka Broker
- Create topic `agentflow-input`

### Start Consumer
```bash
python kafka/consumer.py
python kafka/producer.py


# Output Example
output1.jpeg
