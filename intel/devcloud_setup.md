# Intel DevCloud Setup & Execution Guide

This document describes how to run the AgentFlow framework benchmarks on **Intel DevCloud** using **OpenVINO** and **PyTorch**.

---

## 1. Login to Intel DevCloud

Login to Intel DevCloud using your assigned credentials:

```bash
ssh <username>@login-2.devcloud.intel.com
```

## 2. Allocate a Compute Node
Request an interactive Intel Xeon CPU node:

```Bash
qsub -I -l nodes=1:xeon -l walltime=02:00:00
```

## 3. Load Required Environment
Load the OpenVINO environment module:

```Bash
module load openvino
```
Verify the installation:
```Bash
python -c "import openvino; print(openvino.__version__)"
```
## 4. Install Project Dependencies
Navigate to the project root directory and install required dependencies:

```Bash
pip install transformers torch openvino
```
(Optional: Use a Python virtual environment if required.)

## 5. Run Performance Benchmarks
Navigate to the benchmark directory:

```Bash
cd intel/benchmark
```
Run the PyTorch benchmark:

```Bash
python benchmark_pytorch.py
```
Run the OpenVINO benchmark:
```Bash
python benchmark_openvino.py
```
## 6. Benchmark Results
Benchmarks were executed on Intel Xeon CPU

CPU-only inference was used

Latency and throughput metrics were collected

Results are documented in:
```Text
intel/benchmark/results.md
```
## 7. Notes
Same model architecture used for fair comparison

OpenVINO demonstrates significant inference speedupover PyTorch

Suitable for Intel optimization validation and benchmarking
