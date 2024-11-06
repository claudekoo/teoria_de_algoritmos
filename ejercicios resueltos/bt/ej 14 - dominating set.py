'''
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

(i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.
'''

def dominating_set_min(grafo):
    return list(_dominating_set_min(grafo, grafo.obtener_vertices(), 0, set(grafo.obtener_vertices()), set(grafo.obtener_vertices())))

def _dominating_set_min(grafo, vertices, indice_vertice_actual, conjunto_actual, conjunto_optimo):
    if indice_vertice_actual == len(grafo):
        if len(conjunto_actual) < len(conjunto_optimo):
            return set(conjunto_actual)
        else:
            return conjunto_optimo
    
    conjunto_actual.remove(vertices[indice_vertice_actual])
    if es_ds(grafo,conjunto_actual):
        conjunto_optimo = _dominating_set_min(grafo, vertices, indice_vertice_actual + 1, conjunto_actual, conjunto_optimo)
    conjunto_actual.add(vertices[indice_vertice_actual])
    return _dominating_set_min(grafo, vertices, indice_vertice_actual + 1, conjunto_actual, conjunto_optimo)

def es_ds(grafo, conjunto):
    for v in grafo:
        if v in conjunto:
            continue
        alguno_esta = False
        if not any(w in conjunto for w in grafo.adyacentes(v)):
            return False
    return True
