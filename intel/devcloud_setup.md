# Intel DevCloud – Planned Execution & Benchmark Readiness

This document describes how **AgentFlow is prepared to be executed and benchmarked**
on **Intel® DevCloud** using Intel® OpenVINO™.

> ⚠️ **Disclaimer**
> The benchmarks described below were **not executed** due to lack of access to
> Intel DevCloud and Intel Xeon–based hardware at the time of submission.
>  
> This document demonstrates **benchmark readiness**, **correct integration**,
> and **reproducible steps** for execution on Intel infrastructure.

---

## Purpose

- Demonstrate that AgentFlow is **compatible with Intel DevCloud**
- Provide **clear and reproducible steps** for execution
- Show correct **OpenVINO integration** for ML optimization
- Align with Intel benchmarking expectations

---

## Intended Execution Environment

| Component | Expected Setup |
|---------|----------------|
| CPU | Intel® Xeon® Processor |
| OS | Linux (Ubuntu recommended) |
| Python | 3.9 / 3.10 |
| Acceleration | CPU (OpenVINO) |

---

## Planned DevCloud Execution Steps

### 1. Access Intel DevCloud
- Log in to Intel® DevCloud
- Allocate a CPU compute node

---

### 2. Load OpenVINO Environment
```bash
module load openvino
```
Verify OpenVINO:
```Bash
benchmark_app --help
```
## 3. Install Dependencies
   
```Bash
pip install torch transformers openvino openvino-dev numpy
```
## 4. Navigate to Benchmark Directory
```Bash
cd intel/benchmark
```
## 5. Planned Baseline Benchmark (PyTorch)
```
Bash
python benchmark_pytorch.py
```
Executes ML inference using PyTorch (CPU)
Measures average inference latency

## 6. Planned Optimized Benchmark (OpenVINO)

```Bash
python benchmark_openvino.py
```
Converts model to OpenVINO IR

Runs inference using OpenVINO Runtime

Measures optimized inference latency

### Benchmark Scope
Inference-only benchmarking

Same model architecture for both runs

CPU-only execution

Latency comparison

### Expected Outcome
Based on Intel OpenVINO documentation and prior studies:

Reduced inference latency on Intel CPUs

Improved throughput

No changes required in agent logic

These are expected trends, not measured results.

### Reproducibility
All benchmark scripts are:

Included in the repository

Framework-agnostic

Hardware-independent

Ready to execute on Intel DevCloud or equivalent Intel CPU systems

## Conclusion
Although execution was not performed due to hardware access limitations, AgentFlow:

Fully integrates Intel OpenVINO

Includes complete benchmark scripts

Is ready for execution on Intel DevCloud

Demonstrates correct architectural alignment with Intel optimization workflows
