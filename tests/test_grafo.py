from codigo.algoritmo.grafo import crear_grafo, agregar_arista

def test_grafo():
    grafo = crear_grafo(3)
    agregar_arista(grafo, 0, 1, 2)
    assert grafo[0] == [(1, 2)]
    print("Grafo correcto")

test_grafo()
