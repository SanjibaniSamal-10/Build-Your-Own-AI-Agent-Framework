## Intel DevCloud Execution Steps

1. Login to Intel DevCloud
2. Load environment: module load openvino
3. Install dependencies: pip install transformers torch openvino
4. Run benchmarks:
   python benchmark_pytorch.py
   python benchmark_openvino.py

Results were collected on Intel Xeon CPU.