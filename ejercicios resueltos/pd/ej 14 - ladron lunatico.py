'''
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

Devolver una lista con las posiciones de las casas a robar.
'''

def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if ganancias[0] > ganancias[1]:
            return [0]
        else:
            return [1]

    OPTNC = [0 for i in range(n)]

    OPTNC[0] = 0
    OPTNC[1] = ganancias[1]

    for i in range(1, n-1):
        if i <= 1:
            OPTNC[i] = max(ganancias[i], OPTNC[i-1])
        else:
            OPTNC[i] = max(ganancias[i]+OPTNC[i-2], OPTNC[i-1])

    OPTC = [0 for i in range(n)]

    OPTC[0] = ganancias[0]

    for i in range(1, n):
        if i == n-1:
            if i <=1:
                OPTC[i] = max(ganancias[i], OPTC[i-1])
            else:
                OPTC[i] = max(ganancias[i]+OPTNC[i-2], OPTC[i-1])
        else:
            if i<= 1:
                OPTC[i] = max(ganancias[i], OPTC[i-1])
            else:
                OPTC[i] = max(ganancias[i]+OPTC[i-2], OPTC[i-1])

    ganancia_restante = OPTC[n-1]
    incluye_ultimo = not (OPTC[n-1] == OPTC[n-2])
    solucion = []

    if incluye_ultimo:
        i = n-1
        while i > 0:
            if i == 1:
                if ganancias[i] == ganancia_restante:
                    solucion.insert(0, i)
                    i -= 1
            else:
                if ganancias[i]+OPTNC[i-2] == ganancia_restante:
                    solucion.insert(0, i)
                    ganancia_restante -= ganancias[i]
                    i -= 2
                else:
                    i -= 1
    else:
        i = n-2
        while i >= 0:
            if i <= 1:
                if ganancias[i] == ganancia_restante:
                    solucion.insert(0, i)
                    break
                else:
                    i -= 1
            else:
                if ganancias[i]+OPTC[i-2] == ganancia_restante:
                    solucion.insert(0, i)
                    ganancia_restante -= ganancias[i]
                    i -= 2
                else:
                    i -= 1

    return solucion

print(lunatico([100, 20, 1, 500, 10]))

'''
Lista no circular usando i de 1 a n-2
OPTNC[i] =  para i=1:
                (ganancias[1],[1])
            si pongo i no puedo usar i-1:
                (ganancias[i]+OPTNC[i-2][0], [i]+OPTNC[i-2][1]
            si no lo pongo:
                OPTNC[i-1]
            elijo max entre los dos

Lista circular usando i de 0 a n-1
OPTC[i] =   para i=0:
                (ganancias[0],[0])
            si pongo i no puedo usar i-1 / si i es n-1, tampoco 0:
                (ganancias[i]+OPTC[i-2][0], [i]+OPTC[i-2][1]
                (ganancias[i]+OPTNC[i-2][0], [i]+OPTNC[i-2][1]
            si no lo pongo:
                OPTC[i-1]
            elijo max entre los dos
'''