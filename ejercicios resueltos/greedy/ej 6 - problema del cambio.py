'''
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar
'''

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    monto_restante = monto
    lista_monedas = []
    for moneda in monedas:
        cant_moneda = monto_restante // moneda
        if cant_moneda > 0:
            monto_restante -= cant_moneda * moneda
            for i in range(cant_moneda):
                lista_monedas.append(moneda)
    return lista_monedas

'''
El algoritmo propuesto encuentra la solución óptima en la mayoría de los casos de sistemas monetarios reales, pero no en todos. Por ejemplo, si se tiene el sistema monetario [1, 3, 4] y se pide dar cambio de 6, el algoritmo devolverá [4, 1, 1] (3 monedas), cuando la solución óptima es [3, 3] (2 monedas). El algoritmo es Greedy porque en cada paso elige la moneda de mayor valor que pueda ser utilizada, sin importar el resto de las monedas.
'''