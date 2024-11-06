'''
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;

(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'
'''

def operaciones(k):
    OPT = {0: 0}
    for i in range(1, k+1):
        if i % 2 == 1:
            OPT[i] = OPT[i-1]+1
        else:
            OPT[i] = min(OPT[i-1]+1, OPT[i//2]+1)
    n = k
    operaciones = []
    while n > 0:
        if n % 2 == 1:
             operaciones.insert(0, 'mas1')
             n = n-1
        else:
            if OPT[i//2] <= OPT[i-1]: # En realidad, este if es innecesario
                operaciones.insert(0, 'por2')
                n = n/2
            else:
                operaciones.insert(0, 'mas1')
                n = n-1

    return operaciones

'''
Ecuacion de recurrencia:
OPT[i] =    caso base   OPT[0] = 0
                si es impar  OPT[i-1]+1
                si es par    min(OPT[i-1]+1, OPT[i//2]+1) 

La complejidad del algoritmo es de O(k), existen ciclos simples de tamaño a lo sumo k.
'''