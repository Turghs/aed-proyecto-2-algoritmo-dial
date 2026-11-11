def dial(grafo, inicio):
    n = len(grafo)
    dist = [float("inf")] * n
    anterior = [-1] * n
    eventos = []

    dist[inicio] = 0
    buckets = [[inicio]]
    i = 0

    while i < len(buckets):
        if len(buckets[i]) == 0:
            i += 1
            continue

        u = buckets[i].pop(0)

        if dist[u] != i:
            continue

        eventos.append(("visitar", u, i))

        for v, peso in grafo[u]:
            eventos.append(("revisar", u, v, peso))
            nueva = dist[u] + peso

            if nueva < dist[v]:
                dist[v] = nueva
                anterior[v] = u

                while nueva >= len(buckets):
                    buckets.append([])

                buckets[nueva].append(v)
                eventos.append(("actualizar", v, nueva))

    return dist, anterior, eventos
