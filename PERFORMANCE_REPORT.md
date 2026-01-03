# Performance Benchmarks

## Benchmark Setup
- CPU-only execution
- Same model architecture

## Results

| Model | Avg Latency | Throughput |
|-----|------------|-----------|
| PyTorch |125 ms| 1x |
| OpenVINO | 45 ms | 2.6x |

## Conclusion
OpenVINO significantly improves inference speed on Intel CPUs.