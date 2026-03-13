import torchxrayvision as xrv
import torch

# Load a pre-trained DenseNet model
model = xrv.models.DenseNet(weights="densenet121-res224-all")

print("Model loaded successfully!")
print(f"Number of parameters: {sum(p.numel() for p in model.parameters()):,}")