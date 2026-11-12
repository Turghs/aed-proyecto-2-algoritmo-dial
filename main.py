from manim import *
from codigo.animaciones.ejecucion import mostrar_ejecucion


class VideoDial(Scene):
    def construct(self):
        portada = VGroup(
            Text("Algoritmo de Dial", font_size=44),
            Text("Avance del proyecto 2 · AED", font_size=26),
            Text("Itzel Yadira Arellys Luciani Dávila", font_size=23),
            Text("Nicolás Agustín Vásquez De Velasco Quintana", font_size=23),
        ).arrange(DOWN, buff=0.4)
        self.play(FadeIn(portada))
        self.wait(5)
        self.play(FadeOut(portada))
        introduccion = VGroup(
            Text("¿Cómo encontrar las rutas más cortas desde A?", font_size=30),
            Text("Dial agrupa los nodos por distancia en buckets.", font_size=27),
            Text("Usa pesos enteros no negativos, acotados por C.", font_size=25),
        ).arrange(DOWN, buff=0.5)
        self.play(FadeIn(introduccion))
        self.wait(6)
        self.play(FadeOut(introduccion))
        mostrar_ejecucion(self)
        self.play(FadeOut(*self.mobjects))
        cierre = VGroup(
            Text("Hasta aquí llega el avance", font_size=34),
            Text("Mostramos las primeras actualizaciones desde A.", font_size=26),
            Text("Falta completar el recorrido y explicar la complejidad.", font_size=25),
        ).arrange(DOWN, buff=0.5)
        self.play(FadeIn(cierre))
        self.wait(5)
