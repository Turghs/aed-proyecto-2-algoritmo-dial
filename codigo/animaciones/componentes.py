from manim import *

def crear_nodos():
    nodos = VGroup()

    posiciones = [
        LEFT * 3,
        UP * 1.5,
        DOWN * 1.5,
        RIGHT * 3
    ]

    for i in range(4):
        circulo = Circle(radius=0.35)
        letra = Text(chr(65 + i), font_size=24)
        nodo = VGroup(circulo, letra)
        nodo.move_to(posiciones[i])
        nodos.add(nodo)

    return nodos
