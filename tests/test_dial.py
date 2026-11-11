from codigo.algoritmo.grafo import crear_grafo, agregar_arista
from codigo.algoritmo.dial import dial

def test_dial():
    grafo = crear_grafo(4)

    agregar_arista(grafo, 0, 1, 2)
    agregar_arista(grafo, 0, 2, 1)
    agregar_arista(grafo, 1, 3, 3)
    agregar_arista(grafo, 2, 3, 2)

    dist, anterior, eventos = dial(grafo, 0)

    assert dist == [0, 2, 1, 3]
    print("Dial correcto:", dist)

test_dial()
