from ultralytics import YOLO

# Cargar el modelo base
model = YOLO("yolo11n.pt") 

# El bloque if __name__ == '__main__': es obligatorio en Windows 
# para que la tarjeta gráfica no colapse al usar múltiples procesadores
if __name__ == '__main__':
    
    print("Iniciando entrenamiento local a máxima potencia...")
    
    train_results = model.train(
        data="SM64/data.yaml",  # Ruta apuntando a la carpeta que descomprimiste
        epochs=200,             # Tus 200 épocas máximas
        patience=50,            # Early stopping si no mejora
        imgsz=640,
        device=0                # Forzamos el uso de la RTX 4050
    )