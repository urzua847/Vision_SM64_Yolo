from ultralytics import YOLO

# 1. Cargar tu modelo entrenado
model = YOLO("best.pt")

# 2. Tu lista de archivos
archivos = [
    "prueba1.jpg",
    "prueba2.jpg",
    "prueba3.jpg",
    "prueba1.webm",
    "prueba2.webm",
    "prueba3.webm"
]

# 3. Hacer la predicción archivo por archivo
for archivo in archivos:
    print(f"\n Procesando: {archivo}...")
    # YOLO detectará automáticamente si usa PIL (para fotos) u OpenCV (para videos)
    model.predict(source=archivo, save=True, conf=0.5)

print("\n ¡Procesamiento terminado!")
print("Revisa la carpeta 'runs/detect/predict' para ver las evidencias.")
