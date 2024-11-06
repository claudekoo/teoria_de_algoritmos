'''
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

Se debe devolver una lista con los valores de los grupos a ubicar, en el orden original en el que se encontraban en el vector P.
'''

def bodegon_dinamico(P, W):
    OPT = [[0 for _ in range(W+1)] for _ in range(len(P)+1)]
        
    for w in range(1, W+1):
        OPT[0][w] = 0
        for n in range(1, len(P)+1):
            if P[n-1] <= w:
                if OPT[n-1][w-P[n-1]] + P[n-1] > OPT[n-1][w]:
                    OPT[n][w] = OPT[n-1][w-P[n-1]] + P[n-1]
                else:
                    OPT[n][w] = OPT[n-1][w]
            else:
                OPT[n][w] = OPT[n-1][w]

    n = len(P)
    resultado = []
    current_w = W
    for i in range(n, 0, -1):
        if P[i-1] <= current_w:
            if OPT[i][current_w] == P[i-1] + OPT[i-1][current_w-P[i-1]]:
                resultado.insert(0, P[i-1])
                current_w -= P[i-1]

    return resultado

'''
Ecuación de recurrencia para w arbitrario y n = número de elementos a considerar:
OPT[n, w] =  OPT[0,w] = [] caso base
             si P[n-1] <= w:
               OPT[n, w] = max(P[n-1]+OPT[n-1, w-P[n-1]],
                               OPT[n-1, w])
             sino:
               OPT[n, w] = OPT[n-1, w]

La complejidad del algoritmo implementado es O(n*W), determinado por el doble for loop a la hora de crear la matriz y a la hora de determinar los óptimos.
'''