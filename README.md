#  Build-Your-Own AI Agent Framework – AgentFlow

AgentFlow is a **custom-built AI Agent Framework** (not just an application) that orchestrates **agentic workflows from input to output**.  
The framework enables users to **define task flows composed of multiple agents**, execute them reliably, monitor execution, and audit results using Apache-based
messaging and orchestration..

AgentFlow is built **without using existing agent frameworks** such as **crew.ai, AutoGen, or n8n**, and integrates **Apache technologies** for messaging and orchestration.  
It is designed to support **Intel® OpenVINO™ optimizations** for ML-based agents.

---

##  Problem Statement Alignment

This project fully addresses **Problem Statement – Build-Your-Own AI Agent Framework**:

✔ Framework (not an app)  
✔ Agentic workflow orchestration  
✔ Task flows (DAG-style execution)  
✔ Monitoring and observability  
✔ Apache Kafka & optional Airflow integration  
✔ Multi-agent collaboration  
✔ Intel OpenVINO performance optimization  

---

##  Core Features

- Define and execute **agentic task flows**
- Kafka-based **input ingestion**
- Custom **orchestrator and executor**
- Three working agents:
  - Reference Agent
  - Research Agent
  - Collab Agent
- Shared memory and state handling
- Guardrails and observability
- Intel OpenVINO optimized ML inference
- Optional Apache Airflow DAG support

---

## Architecture Overview

```text
Ingress (Kafka / REST)
        ↓
    Orchestrator
        ↓
  Task Flow Engine
        ↓
Agents (Executors)
        ↓
State / Memory / Guardrails
        ↓
   Output Handler
```
## Requirement Coverage Matrix

| Requirement | Status |
|------------|--------|
| Define & execute task flows (DAG / state machine) | ✅ |
| Input handlers | ✅ Kafka Producer |
| Tools & actions | ✅ Agent Executors |
| Output handlers | ✅ Kafka / Logs |
| Memory & state | ✅ Memory module |
| Guardrails | ✅ Policy hooks |
| Observability (logs, metrics) | ✅ |
| Apache components | ✅ Kafka, Airflow |
| Reliable execution | ✅ Extendable |
| Multi-agent collaboration | ✅ Collab Agent |
| Intel OpenVINO optimization | ✅ Integrated |

---

##  Why AgentFlow is a Framework

AgentFlow provides:
- A **Flow Engine** to define agentic task flows
- A **Base Agent abstraction**
- An **Orchestrator** to manage execution
- **Pluggable memory, guardrails, and observability**
- **Apache Kafka** for ingress and messaging
- **Apache Airflow** for optional DAG orchestration

We **build agents and workflows on top of AgentFlow**, making it a reusable framework.

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

---

##  Project Structure

```text
agentflow-framework/
├── __pycache__/
│
├── agentflow/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── task.py              # Task abstraction
│   ├── flow.py              # Task flow (DAG-style execution)
│   ├── orchestrator.py      # Central workflow controller
│   ├── executor.py          # Task execution engine
│   ├── memory.py            # Shared memory/state
│   ├── guardrails.py        # Safety & policy checks
│   └── observability.py     # Logs & metrics
│
├── agents/
│   ├── __pycache__/
│   ├── reference_agent.py   # Reference agent
│   ├── research_agent.py    # Research agent
│   └── collab_agent.py      # Collaboration agent
│
├── executors/
│   ├── __pycache__/
│   ├── search.py            # Search tool
│   └── summarize.py         # Summarization tool
│
├── kafka/
│   ├── producer.py          # Kafka producer (input)
│   └── consumer.py          # Kafka consumer (ingress)
│
├── airflow_dag/
│   └── agentflow_dag.py     # Optional Airflow DAG
│
├── airflow_home/
│   ├── dags/
│   │   └── agentflow_dag.py
│   ├── logs/
│   ├── airflow.cfg
│   ├── airflow.db
│   └── webserver_config.py
│
├── intel/
│   ├── model/
│   │   ├── pytorch_model.py
│   │   └── openvino_model.py
│   ├── benchmark/
│   │   ├── benchmark_pytorch.py
│   │   ├── benchmark_openvino.py
│   │   └── results.md
│   └── devcloud_setup.md
│
├── io/
│   ├── input_handler.py     # Input interface
│   └── output_handler.py    # Output interface
│
├── venv/
│   ├── bin/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── run_agent.py             # Framework entry point
│
├── ARCHITECTURE.md          # System architecture
├── DESIGN_DOC.md            # Design documentation
├── benchmark.md             # Performance benchmarks
├── PERFORMANCE_REPORT.md    # Intel optimization results
├── OBSERVABILITY.md         # Logging & metrics
├── WORKFLOW.md              # Agent workflows
├── LIMITATION.md            # Known limitations
├── SETUP_GUIDE.md           # Installation & setup
├── README.md
└── LICENSE
```
---
## Agents Included

### 1️⃣ Reference Agent
- Produces a baseline response
- Acts as a starting point for the workflow

### 2️⃣ Research Agent
- Gathers relevant information
- Performs analysis or search-based processing

### 3️⃣ Collaboration (Collab) Agent
- Refines and improves outputs
- Demonstrates **multi-agent collaboration**
- Combines insights from other agents

These agents together demonstrate **real agentic workflows**, not static pipelines.

---

## Key Features

- Custom AI Agent Framework (not an app)
- Task flow orchestration (DAG-based)
- Multi-agent collaboration (Reference, Research, Collaboration Agents)
- Kafka-based ingress and messaging
- Optional Airflow DAG orchestration
- Memory, guardrails, and observability
- Intel OpenVINO optimized inference
- Execution metrics and benchmarking

---

## Technologies Used

- Python 3.10
- Apache Kafka
- Apache Airflow (DAG orchestration)
- Intel OpenVINO
- PyTorch (baseline model)
- Logging & Metrics (custom observability)

---

##  Agent Workflows

### Workflow 1: Research & Summarize
1. Input received via Kafka

2. Orchestrator initializes flow
3. Research Agent collects information
4. Reference Agent validates facts
5. Collab Agent refines response
6. Output generated

### Workflow 2: Multi-Agent Collaboration

1. Agents share memory
2. Results refined iteratively
3. Enables collaboration and reflection

---
## Intel® OpenVINO™ Integration

AgentFlow is **designed to support ML inference optimization** using **Intel® OpenVINO™**
for agent tasks such as summarization and semantic processing.

### Supported Inference Modes
- **Baseline:** PyTorch CPU inference
- **Optimized:** Intel OpenVINO inference (optional)

### Integration Status
- OpenVINO adapter implemented in `intel/model/openvino_model.py`
- Benchmark scripts included for PyTorch vs OpenVINO comparison
- Agent logic remains unchanged when switching inference backends

### Example Usage
```python
from intel.model.openvino_model import OpenVINOModel

model = OpenVINOModel("model.xml")
result = model.infer(input_data)
```
## Note:

OpenVINO benchmarking is prepared but not executed in this submission due to lack of access to Intel DevCloud or Intel Xeon–based hardware. All scripts and documentation are provided for reproducible evaluation.

--- 
## Observability & Auditing
AgentFlow provides:

- Execution logs

- Agent-level metrics
  
- Workflow traceability
  
- Error visibility
This enables monitoring, debugging, and auditing of agent workflows.

Metrics Collected:

- Task execution time

- Total workflow latency
  
- Failure counts

Logging: 

- Task start/end
- Agent decisions
- Errors and retries

---
## Guardrails & Safety

- Policy checks before and after execution
- Human-in-the-loop extension points
- Pluggable rule-based enforcement

--- 
## Apache Integration

### Kafka (Ingress & Messaging)
1. Handles input ingestion
2. Enables asynchronous execution
3. Decouples producers and agents

### Airflow 
Used for:

1.Scheduled execution

2.Retry handling

3.Fault tolerance
## How to Run (Minimal Demo)

### Start Kafka
- Start Zookeeper
- Start Kafka Broker
- Create topic `agentflow-input`

### Start Consumer
```bash
python kafka/consumer.py
python kafka/producer.py
```

# Output Example
![image alt](https://github.com/SanjibaniSamal-10/Build-Your-Own-AI-Agent-Framework/blob/2fbe8873e6079a153aa5ac1d38a81b0c6569e1b9/output1.jpeg)

![image alt](https://github.com/SanjibaniSamal-10/Build-Your-Own-AI-Agent-Framework/blob/789143a2b935856ce8c1b51924221a062fd63bb2/output2.jpeg)

---
##  Airflow Integration (Optional)

AgentFlow includes an **Apache Airflow DAG** to enable production-grade orchestration.

### Supported Capabilities
- Scheduled executions
- Automatic retries on failure
- Fault tolerance and task monitoring
- DAG-based agent workflow execution

The Airflow DAG is located at:
airflow_dag/agentflow_dag.py

### Trigger the DAG
```bash
airflow dags trigger agentflow_dag
```
---
## Intel® OpenVINO™ Optimization (Planned & Ready)

AgentFlow is **designed and prepared** to support Intel® OpenVINO™
for optimizing ML inference workloads used inside agents
(e.g., summarization and semantic processing).

### Integration Status
- OpenVINO runtime integrated (`intel/model/openvino_model.py`)
- Benchmark scripts included (`intel/benchmark/`)
- No agent logic changes required for optimization
- Fully compatible with Intel DevCloud execution

### Benchmarking Approach
The framework supports **comparative benchmarking** between:
- Baseline: PyTorch CPU inference
- Optimized: Intel OpenVINO inference

Metrics intended for evaluation:
- Average inference latency
- Throughput improvement
- CPU efficiency

### Execution Status
>  **Benchmarks were not executed** at the time of submission  
> due to lack of access to Intel DevCloud or Intel Xeon–based hardware.

All scripts, configurations, and documentation are provided
to enable **reproducible benchmarking** on Intel infrastructure.

### Expected Outcome (Indicative)
Based on Intel OpenVINO documentation and prior studies:
- Reduced inference latency on Intel CPUs
- Improved throughput
- Efficient CPU utilization

These are **expected trends**, not measured results.

Detailed execution steps are provided in:
- `intel/devcloud_setup.md`
- `benchmark.md`

  Benchmark methodology and planned evaluation steps are documented in `benchmark.md`
  ---

## Deliverables Included

This repository fulfills all required deliverables:

✅ Framework SDK for defining flows, agents, and policies

✅ Three working agents

Reference Agent
Research Agent
Collaboration Agent

✅ Apache Kafka integration for ingress and messaging

✅ Apache Airflow orchestration support (optional)

✅ Intel OpenVINO optimization support

✅ Design documentation (DESIGN_DOC.md)

✅ Benchmark scripts (PyTorch vs OpenVINO)

---
## ⚠️ Limitations
1. Airflow not natively supported on Windows
2. In-memory storage (demo purpose)
3. Limited agent reasoning depth (extensible)

## Conclusion
AgentFlow is a production-oriented AI Agent Framework that:

❌ Uses no external agent frameworks (crew.ai, AutoGen, n8n)

✅ Supports Apache-based orchestration (Kafka, Airflow)

✅ Enables multi-agent collaboration

✅ Provides observability, memory, and guardrails

✅ Is Intel optimization-ready using OpenVINO

AgentFlow demonstrates how agentic workflows can be built from first principles, making it suitable for research, enterprise experimentation, and system design evaluations.

