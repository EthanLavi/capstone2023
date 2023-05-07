import torch
print("CUDA Availability:", torch.cuda.is_available())
print("CUDA Device Count:", torch.cuda.device_count())
print("CUDA Information:", torch.cuda.current_device())
