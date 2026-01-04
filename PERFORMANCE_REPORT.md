# Performance Benchmarks – AgentFlow

## Benchmark Setup
- CPU-only execution (Intel CPU)
- Same model architecture used for Research/Summary tasks
- Baseline: PyTorch inference
- Optimized: Intel OpenVINO inference
- Measured: average latency per query and throughput relative to baseline

## Results

| Model    | Avg Latency (per query) | Throughput (relative) |
|---------|------------------------|---------------------|
| PyTorch | 125 ms                 | 1x                  |
| OpenVINO| 45 ms                  | 2.6x                |

## Conclusion
- Intel OpenVINO reduces latency by ~64% compared to PyTorch.
- Throughput improves ~2.6×, enabling faster agent responses.
- OpenVINO integration is seamless; no change to agent logic required.
