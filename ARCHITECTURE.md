# Architecture – AgentFlow

## High-Level Architecture

Ingress → Orchestrator → Executors → Memory → Output

---

## Components

### Ingress
- Kafka Producer / REST Input

### Orchestrator
- Task scheduling
- Flow execution
- Error handling

### Executors
- Search Executor
- Summary Executor

### Agents
- Reference Agent
- Research Agent
- Collaboration Agent

### Storage
- In-memory state
- Logs and metrics

---

## Apache Components

- Kafka: Messaging
- Airflow: DAG orchestration (optional)

---

## Intel Stack

- PyTorch baseline models
- OpenVINO optimized models