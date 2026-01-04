# Performance Benchmarks – AgentFlow

## Benchmark Setup (Planned)

The following benchmark setup is **designed and documented** for execution on
Intel® DevCloud or Intel® Xeon–based systems.

- CPU-only execution (Intel CPU – planned)
- Same model architecture used for Research and Summarization agents
- Baseline: PyTorch CPU inference
- Optimized: Intel OpenVINO inference
- Metrics:
  - Average inference latency per query
  - Relative throughput compared to baseline

>  **Note:**  
> Due to lack of access to Intel DevCloud or Intel Xeon hardware, the benchmarks
> were **not executed** as part of this submission.  
> The results below are **indicative / expected performance**, based on Intel
> OpenVINO reference documentation and prior benchmarks.

---

## Indicative Results (Expected)

| Model     | Avg Latency (per query) | Throughput (relative) |
|----------|--------------------------|-----------------------|
| PyTorch  | ~125 ms                  | 1×                    |
| OpenVINO | ~45 ms                   | ~2.6×                 |

---

## Expected Performance Impact

- ~60–65% reduction in inference latency using Intel OpenVINO
- ~2–3× improvement in throughput on Intel CPUs
- Faster agent responses and improved workflow execution speed
- No changes required to agent logic when switching inference backend

---

## Reproducibility

Benchmark scripts are provided in:
intel/benchmark/
├── benchmark_pytorch.py
├── benchmark_openvino.py

These scripts can be executed on Intel DevCloud or Intel Xeon systems to
reproduce and validate the above indicative results.

---

## Conclusion

AgentFlow is **performance-optimization ready** and designed to leverage
Intel® OpenVINO™ for accelerated ML inference.

While benchmarks are not executed in this submission, the framework,
integration, and evaluation pipeline are fully implemented and reproducible.
