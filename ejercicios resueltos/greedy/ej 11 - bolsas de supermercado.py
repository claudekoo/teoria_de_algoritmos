'''
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.
'''

def bolsas(capacidad, productos):
    if not productos:
        return []
    productos.sort(reverse=True) # menor a mayor
    
    lista_bolsas = []
    # para que en la primera iteracion entre a else:
    bolsa_actual = -1
    peso_actual = capacidad +1

    for peso_producto in productos:
        if peso_actual + peso_producto <= capacidad:
            (lista_bolsas[bolsa_actual]).append(peso_producto)
            peso_actual += peso_producto
        else:
            lista_bolsas.append([])
            bolsa_actual += 1
            (lista_bolsas[bolsa_actual]).append(peso_producto)
            peso_actual = peso_producto
            
    return lista_bolsas

'''
El algoritmo no siempre encuentra la solución óptima:
En el ejemplo brindado, con la implementación hecha
bolsas(5, [4, 2, 1, 3, 5]) == [[1, 2],[3],[4],[5]] resultando en 4 bolsas
pero hay solución óptima con 3 bolsas: [[1, 4],[2, 3],[5]]
Complejidad
T(n) = O(n log n) ya que tiene que ordenar los productos
'''