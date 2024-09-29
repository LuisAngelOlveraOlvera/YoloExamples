import torch
import torch.nn as nn
import os
from ultralytics import YOLO
import ultralytics

# Verificar si la GPU está disponible
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Definir un modelo simple y moverlo a la GPU
model = nn.Linear(10, 1)
model.to(device)

# Crear datos de entrada
inputs = torch.randn(32, 10, device=device)
labels = torch.randn(32, 1, device=device)

# Verificar ultralytics
ultralytics.checks()

# Ruta para guardar la predicción
output_dir = r"C:\Users\User\Pictures\PREDICCIONES"

# Cargar el modelo YOLOv8
model = YOLO('yolov8s.pt')

# Ejecutar la predicción en la imagen y guardarla en la carpeta especificada
results = model.predict(source=r"C:\Users\User\Pictures\gato1.jpeg", device=device, save=True, project=output_dir, name="predict")


# Comprobar si la predicción se ejecutó en la GPU
print(f"Predicción ejecutada en: {device}")
