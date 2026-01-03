import time
from intel.model.pytorch_model import TextEmbeddingTorch

model = TextEmbeddingTorch()
text = "Intel OpenVINO optimization benchmark"

start = time.time()
for _ in range(10):
    model.infer(text)
end = time.time()

print("PyTorch Avg Latency:", (end - start) / 10)