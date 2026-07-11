# Detección de Enemigos en Super Mario 64 utilizando YOLOv11

## Descripción del proyecto
Este proyecto corresponde al trabajo final del curso **Taller de Introducción a Visión por Computadora** de la **Universidad del Bío-Bío**. El objetivo principal es la implementación de un modelo de Deep Learning basado en **YOLOv11** orientado a la detección y clasificación de enemigos dentro del entorno tridimensional del videojuego Super Mario 64.

El sistema enfrenta desafíos clásicos de visión artificial como la baja resolución de polígonos (característica de la consola N64), variaciones de iluminación en distintos niveles y fondos complejos que comparten paleta de colores con los enemigos.

## Tecnologías Utilizadas
* **Python 3.10**
* **YOLOv11 (Ultralytics)**: Versión Nano (YOLOv11n) para optimización de inferencia.
* **PyTorch & OpenCV**: Con soporte CUDA para aceleración por GPU.
* **Roboflow**: Utilizado para la gestión del dataset, etiquetado y aplicación de técnicas de *Data Augmentation*.
* **Hardware**: Entrenamiento local realizado en **ASUS Vivobook 16** con GPU **NVIDIA RTX 4050**.

## Enemigos Detectados
El modelo fue entrenado para reconocer y diferenciar las siguientes entidades:
* **Boos**: Fantasmas con desafíos de transparencia.
* **Goomba**: Enemigos básicos con texturas similares al suelo.
* **Koopa**: Tortugas con colores vibrantes y alta tasa de detección.

## Estructura del Repositorio
```text
Vision_SM64_Yolo/
│
├── models/
│   ├── best.pt             # Modelo final entrenado
│   └── yolo11n.pt          # Pesos base de YOLO
│
├── scripts/
│   ├── entrenar.py         # Script de entrenamiento local
│   ├── predecir.py         # Inferencia en imágenes y videos
│   └── test.py             # Verificación de entorno y CUDA
│
├── demo_results/
│   └── *.jpg / *.webm      # Evidencias de detección (Bounding Boxes)
│
├── requirements.txt        # Librerías y dependencias
├── README.md               # Documentación del proyecto
└── .gitignore              # Archivos excluidos (entornos y datasets pesados)

