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
│   └── best.pt             # Modelo final entrenado
│  
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

# Ejecución

## Entrenar el modelo

```bash
python scripts/entrenar.py
```

## Detectar objetos en imágenes o videos

```bash
python scripts/predecir.py
```

## Ejecutar pruebas

```bash
python scripts/test.py
```

---

# Resultados

El modelo obtuvo un rendimiento sobresaliente durante la evaluación.

## Métricas Globales

| Métrica | Resultado |
|----------|----------:|
| Precision | 98.96 % |
| Recall | 98.96 % |
| F1-Score | 98.96 % |
| mAP50 | 98.97 % |
| mAP50-95 | 78.80 % |

Estos resultados indican que el modelo detecta correctamente los enemigos con una alta precisión y una baja tasa de falsos positivos.

---

# Ejemplo de Inferencia

A continuación se muestra un ejemplo del funcionamiento del modelo sobre una imagen del juego.

> **Inserte aquí una captura de `demo_results/prueba1.jpg`**

Por ejemplo, en GitHub puedes escribir:

```markdown
![Ejemplo de inferencia](demo_results/prueba1.jpg)
```

Si prefieres otra imagen, puedes utilizar:

- demo_results/prueba2.jpg
- demo_results/prueba3.jpg

---

# Posibles Mejoras

Como trabajo futuro se propone:

- Incorporar nuevas clases de enemigos.
- Aumentar la diversidad del dataset.
- Mejorar el rendimiento de mAP50-95 mediante un ajuste de hiperparámetros.
- Implementar técnicas avanzadas de Data Augmentation.
- Optimizar el modelo para inferencia en tiempo real.

---

# Aplicaciones

Aunque el proyecto se desarrolla sobre un videojuego, las técnicas utilizadas son equivalentes a las empleadas actualmente en:

- Robótica.
- Vehículos autónomos.
- Sistemas de vigilancia.
- Automatización industrial.
- Detección de objetos mediante inteligencia artificial.

---

# Autores

Proyecto desarrollado para la asignatura **Taller de Introducción a Visión por Computadora** de la **Universidad del Bío-Bío**.

Integrantes:
Javier Villena 
Carlos Urzua

