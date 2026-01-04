## ⚠️ Limitations

- **Apache Airflow is not natively supported on Windows**  
  Airflow execution requires WSL2, Docker, or a Linux environment.

- **In-memory state and memory storage**  
  Agent memory is stored in-memory for demonstration purposes and is not persisted across runs.

- **Limited agent reasoning depth**  
  Agents follow predefined execution logic; advanced autonomous planning and long-horizon reasoning can be added in future work.

- **No distributed state backend**  
  The framework does not yet integrate Redis, Cassandra, or a distributed database for shared state management.

- **Basic retry and failure handling**  
  Retries and timeouts are implemented at a basic level and can be extended with advanced policies.

- **Single-node execution model**  
  Kafka is used for messaging, but agents currently execute on a single node.

- **ML models are lightweight demo models**  
  OpenVINO integration is demonstrated using simplified models rather than large-scale production LLMs.
