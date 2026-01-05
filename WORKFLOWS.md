## Agent Workflows – AgentFlow

This document describes the main workflows implemented in AgentFlow using the three agents: Reference Agent, Research Agent, and Collab Agent.


---

## Workflow 1: Research & Summarize

This workflow demonstrates a single-query pipeline executed by multiple agents.

Steps:

1. Input Received – via Kafka or REST endpoint


2. Reference Agent – selects and routes tasks, provides initial guidance


3. Research Agent – gathers relevant information from sources


4. Collab Agent – refines the output for clarity, coherence, and completeness


5. Final Response – returned to the output handler



## Sample Logs:
``` Text
Kafka Consumer started...
Received: {'query': 'AI Agent Framework'}
--- Agent Flow Started ---
Reference Agent: routing task
Research Agent: searching for information Executed search in 0.02 sec
Collab Agent: refining output
Executed refinement in 0.01 sec
--- Agent Flow Completed ---

```
---

## Workflow 2: Multi-Agent Collaboration

This workflow demonstrates iterative and collaborative reasoning among agents.

Features:

Agents share memory and state to maintain context

Outputs are refined iteratively across agents

Supports reflection loops

Ready for human-in-the-loop interventions via guardrails


## Example:

1. Reference Agent receives a complex query and assigns subtasks


2. Research Agent fetches detailed information


3. Collab Agent iteratively improves the content based on previous outputs


4. Final coherent response is produced




---

## ✅ Notes

The workflows are fully modular and extensible

Agents are decoupled: Reference Agent, Research Agent, Collab Agent

Can be triggered via Kafka input or scheduled with Airflow DAG

Observability (logging and metrics) is available for all workflows



---
