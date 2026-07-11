import torch

print("PyTorch versión:", torch.__version__)
print("¿CUDA está disponible?:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Tarjeta gráfica detectada:", torch.cuda.get_device_name(0))
else:
    print("¡ALERTA! PyTorch no detecta la GPU.")