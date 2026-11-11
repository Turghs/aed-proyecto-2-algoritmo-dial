from manim import *
from codigo.animaciones.ejecucion import mostrar_ejecucion

class VideoDial(Scene):
    def construct(self):
        titulo = Text("Algoritmo de Dial", font_size=44)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        mostrar_ejecucion(self)

        self.play(
            FadeOut(*self.mobjects)
        )

        texto = Text("Complejidad: O(E + C*V)", font_size=30)
        self.play(Write(texto))
        self.wait(2)
