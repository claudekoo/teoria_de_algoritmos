'''
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.
'''

def charlas(horarios):
    horarios_ordenados = sorted(horarios, key=lambda x: x[1])
    lista_charlas = []
    for horario in horarios_ordenados:
        if len(lista_charlas) == 0 or not hay_interseccion(lista_charlas[-1], horario):
            lista_charlas.append(horario)
    return lista_charlas

def hay_interseccion(anterior, nueva):
    return anterior[1] > nueva[0]

'''
Complejidad
T(n) = O(n log n)
ya que para ordenar tarda O(n log n) y luego recorre la lista, O(n)
'''