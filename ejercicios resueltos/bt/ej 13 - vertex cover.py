'''
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.
'''

from grafo import Grafo

def vertex_cover_min(grafo):
    return list(_vertex_cover_min(grafo, grafo.obtener_vertices(), 0 , set(grafo.obtener_vertices()),set(grafo.obtener_vertices())))

def _vertex_cover_min(grafo, vertices, indice_vertice_actual, conjunto_actual, conjunto_optimo):
    if indice_vertice_actual == len(grafo.obtener_vertices()):
        if len(conjunto_actual) < len(conjunto_optimo):
            return set(conjunto_actual)
        else:
            return conjunto_optimo
    
    conjunto_actual.remove(vertices[indice_vertice_actual])
    if es_vc(grafo,conjunto_actual):
        conjunto_optimo = _vertex_cover_min(grafo, vertices, indice_vertice_actual + 1, conjunto_actual, conjunto_optimo)
    conjunto_actual.add(vertices[indice_vertice_actual])
    return _vertex_cover_min(grafo, vertices, indice_vertice_actual + 1, conjunto_actual, conjunto_optimo)

def es_vc(grafo, conjunto):
    for v in grafo.obtener_vertices():
        if v not in conjunto:
            for w in grafo.adyacentes(v):
                if w not in conjunto:
                    return False
    return True
