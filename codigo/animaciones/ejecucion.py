from manim import *
from codigo.algoritmo.grafo import crear_grafo, agregar_arista
from codigo.algoritmo.dial import dial
from codigo.animaciones.componentes import crear_nodos

def mostrar_ejecucion(escena):
    grafo = crear_grafo(4)

    agregar_arista(grafo, 0, 1, 2)
    agregar_arista(grafo, 0, 2, 1)
    agregar_arista(grafo, 1, 3, 3)
    agregar_arista(grafo, 2, 3, 2)

    dist, anterior, eventos = dial(grafo, 0)

    nodos = crear_nodos()
    escena.play(Create(nodos))

    for evento in eventos:
        if evento[0] == "visitar":
            u = evento[1]
            escena.play(nodos[u][0].animate.set_color(YELLOW))

        if evento[0] == "actualizar":
            v = evento[1]
            nueva = evento[2]

            texto = Text(
                f"{chr(65 + v)} = {nueva}",
                font_size=28
            ).to_edge(DOWN)

            escena.play(Write(texto))
            escena.wait(0.3)
            escena.play(FadeOut(texto))

    escena.wait(1)
