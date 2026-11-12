# Proyecto 2: Algoritmo de Dial

**Curso:** Algoritmos y Estructuras de Datos (AED)  
**Ciclo:** 2026-2

## Integrantes

- Itzel Yadira Arellys Luciani Dávila
- Nicolás Agustín Vásquez De Velasco Quintana

## Descripción

Dial encuentra caminos mínimos desde un nodo en grafos con pesos enteros no negativos, acotados por un valor C. Usa buckets para procesar los nodos según su distancia.

## Avance

Tenemos un prototipo del algoritmo en Python y una animación en Manim. La animación muestra un grafo de cuatro nodos, sus pesos, las distancias desde A y los primeros movimientos entre buckets. Los pasos se obtienen de la ejecución del algoritmo.

[Ver o descargar el video parcial](videos/avance_dial.mp4)

El video se detiene después de procesar A y C. Quedan pendientes la implementación en C++, la animación completa, un caso de borde y la explicación de complejidad.

## Requisitos

- Python 3.12 (versión usada para el avance).
- Manim y sus dependencias, indicados en `requirements.txt`.

## Ejecutar en Windows

Desde la carpeta del proyecto:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Para ejecutar las pruebas básicas:

```powershell
.venv\Scripts\python.exe -m tests.test_grafo
.venv\Scripts\python.exe -m tests.test_dial
```

Para generar el video en 1080p:

```powershell
.venv\Scripts\python.exe -m manim -qh main.py VideoDial
```

El resultado se guarda en `media/videos/main/1080p60/VideoDial.mp4`. La carpeta `media` no se sube a Git. Para actualizar la copia del avance incluida en el repositorio:

```powershell
Copy-Item media/videos/main/1080p60/VideoDial.mp4 videos/avance_dial.mp4
```

Para una revisión rápida se puede usar `-ql` en lugar de `-qh`; esa versión se guarda en `media/videos/main/480p15/`.
