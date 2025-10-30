import torch

# 检查 MPS (Apple Silicon GPU) 是否可用
if torch.backends.mps.is_available():
    print("MPS is available! You can use the GPU on your Mac.")
else:
    print("MPS not available, you will be running on CPU only.")