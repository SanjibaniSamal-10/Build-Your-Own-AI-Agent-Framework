import time
import numpy as np
from intel.model.openvino_model import TextEmbeddingOpenVINO

model = TextEmbeddingOpenVINO()

dummy_ids = np.random.randint(0, 1000, (1, 16))
dummy_mask = np.ones((1, 16))

start = time.time()
for _ in range(10):
    model.infer(dummy_ids, dummy_mask)
end = time.time()

print("OpenVINO Avg Latency:", (end - start) / 10)