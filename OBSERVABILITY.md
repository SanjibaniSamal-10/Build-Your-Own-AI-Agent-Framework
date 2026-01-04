## Observability

AgentFlow includes built-in observability to enable **monitoring, debugging, and auditing** of agentic workflows.

### Metrics Collected
- Execution time per task (per agent and executor)
- Total end-to-end workflow latency
- Task success and failure counts

### Logging
- Task and agent execution start/end events
- Agent routing and decision-making steps
- Errors, exceptions, retries, and timeouts

### Sample Logs
- Executed search in 0.02 sec
- Executed summary in 0.00 sec

### Auditability
- Each workflow execution is logged with timestamps
- Agent actions can be replayed from logs for debugging
- Logs provide a clear execution trace across agents

### Extensibility
- Observability is implemented using Python logging utilities
- Can be extended to integrate with external monitoring systems such as Prometheus, ELK, or OpenTelemetry
