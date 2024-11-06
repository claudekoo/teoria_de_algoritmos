'''
Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún lugar a dos mafias diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?
'''

# pedidos: lista de tuplas con (km inicio, km fin)

def asignar_mafias(pedidos):
    pedidos_ordenados = sorted(pedidos, key=lambda x: x[1])
    lista_pedidos = []
    for pedido in pedidos_ordenados:
        if len(lista_pedidos) == 0 or not hay_interseccion(lista_pedidos[-1], pedido):
            lista_pedidos.append(pedido)
    return lista_pedidos

def hay_interseccion(anterior, nueva):
    return anterior[1] > nueva[0]

'''
Complejidad
T(n) = O(n log n)
ya que para ordenar tarda O(n log n) y luego recorre la lista, O(n)

El algoritmo es Greedy porque en cada paso elige el pedido que termina antes, sin importar el resto de los pedidos.
El algoritmo no siempre da la solución óptima, por ejemplo si se tienen los pedidos [(1, 3), (2, 4), (3, 5)] el algoritmo devolverá [(1, 3), (3, 5)] cuando la solución óptima es [(1, 3), (3, 5)].
'''