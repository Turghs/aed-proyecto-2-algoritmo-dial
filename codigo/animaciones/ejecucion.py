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

    titulo = Text("Primeros pasos desde A", font_size=32).to_edge(UP)
    nodos = crear_nodos().scale(0.8).shift(LEFT * 1.7 + UP * 0.5)
    aristas = {}
    dibujos = VGroup()
    for u in range(len(grafo)):
        for v, peso in grafo[u]:
            flecha = Arrow(nodos[u].get_center(), nodos[v].get_center(), buff=0.35)
            etiqueta = Text(str(peso), font_size=23)
            etiqueta.move_to(flecha.get_center() + UP * 0.3)
            aristas[(u, v)] = flecha
            dibujos.add(flecha, etiqueta)

    distancias = [0, float("inf"), float("inf"), float("inf")]
    # Solo los buckets usados en este fragmento del ejemplo.
    buckets = [[0], [], [], []]

    def panel_distancias():
        filas = VGroup(Text("Distancia desde A", font_size=23))
        for v, distancia in enumerate(distancias):
            valor = "∞" if distancia == float("inf") else str(distancia)
            filas.add(Text(f"{chr(65 + v)}: {valor}", font_size=25))
        return filas.arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(RIGHT * 4 + UP * 0.5)

    def panel_buckets():
        cajas = VGroup()
        for i, contenido in enumerate(buckets):
            caja = Rectangle(width=1.8, height=0.65)
            letras = ", ".join(chr(65 + v) for v in contenido) or "—"
            texto = Text(letras, font_size=23).move_to(caja)
            indice = Text(f"bucket {i}", font_size=20).next_to(caja, DOWN, buff=0.12)
            cajas.add(VGroup(caja, texto, indice))
        return cajas.arrange(RIGHT, buff=0.3).move_to(DOWN * 2)

    tabla = panel_distancias()
    cajas = panel_buckets()
    mensaje = Text("A empieza con distancia 0, dentro del bucket 0.", font_size=24).to_edge(DOWN)
    escena.play(Write(titulo), Create(dibujos), Create(nodos))
    escena.play(FadeIn(tabla), FadeIn(cajas), Write(mensaje))
    escena.wait(4)

    visitas = 0
    for evento in eventos:
        if evento[0] == "visitar":
            if visitas == 2:
                break
            visitas += 1
            u, distancia = evento[1:]
            buckets[distancia].remove(u)
            texto = f"Sacamos {chr(65 + u)} del bucket {distancia}."
            escena.play(nodos[u][0].animate.set_color(YELLOW))
        elif evento[0] == "revisar":
            u, v, peso = evento[1:]
            texto = f"Revisamos {chr(65 + u)} → {chr(65 + v)}, de peso {peso}."
            escena.play(aristas[(u, v)].animate.set_color(YELLOW))
        elif evento[0] == "actualizar":
            v, nueva = evento[1:]
            distancias[v] = nueva
            buckets[nueva].append(v)
            texto = f"La distancia a {chr(65 + v)} mejora a {nueva}: va al bucket {nueva}."
        else:
            continue
        escena.play(
            Transform(mensaje, Text(texto, font_size=24).to_edge(DOWN)),
            Transform(tabla, panel_distancias()),
            Transform(cajas, panel_buckets()),
        )
        escena.wait(2)

    texto = "El siguiente nodo sería B, en el bucket 2. Continuará…"
    escena.play(Transform(mensaje, Text(texto, font_size=24).to_edge(DOWN)))
    escena.wait(4)
