# Agent Workflows – AgentFlow

This document describes the **main workflows** implemented in AgentFlow using the three agents: **Reference Agent, Research Agent, and Collab Agent**.

---

## Workflow 1: Research & Summarize

This workflow demonstrates a **single-query pipeline** executed by multiple agents.

### Steps:

1. **Input Received** – via Kafka or REST endpoint  
2. **Reference Agent** – selects and routes tasks, provides initial guidance  
3. **Research Agent** – gathers relevant information from sources  
4. **Collab Agent** – refines the output for clarity, coherence, and completeness  
5. **Final Response** – returned to the output handler  

### Sample Logs:

```text
Kafka Consumer started...
Received: {'query': 'AI Agent Framework'}
--- Agent Flow Started ---
Reference Agent: routing task
Research Agent: searching for information
Executed search in 0.02 sec
Collab Agent: refining output
Executed refinement in 0.01 sec
--- Agent Flow Completed ---
