def crear_grafo(n):
    return [[] for i in range(n)]

def agregar_arista(grafo, a, b, peso):
    grafo[a].append((b, peso))
