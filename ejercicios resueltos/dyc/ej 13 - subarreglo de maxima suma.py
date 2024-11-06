'''
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo. Ejemplos:

[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
'''

def max_subarray(arr):
    if len(arr) <= 1:
        return arr
    optimo_ini, optimo_fin, maximo = _max_subarray(arr, 0, len(arr)-1)
    return arr[optimo_ini:optimo_fin+1]

def _max_subarray(arr, ini, fin):
    if ini == fin:
        return ini, fin, arr[ini]

    med = (ini+fin)//2

    optimo_izq_ini, optimo_izq_fin, maximo_izq = _max_subarray(arr, ini, med)
    optimo_der_ini, optimo_der_fin, maximo_der = _max_subarray(arr, med+1, fin)

    optimo_cen_ini, optimo_cen_fin, maximo_cen = med, med+1, arr[med]+arr[med+1]
    maximo_cen_izq, maximo_cen_der = arr[med], arr[med+1]

    maximo_provisorio = arr[med]
    for i in range(0, med-ini):
        maximo_provisorio += arr[med-1-i]
        if maximo_provisorio > maximo_cen_izq:
            maximo_cen_izq = maximo_provisorio
            optimo_cen_ini = med-i-1
    
    maximo_provisorio = arr[med+1]
    for i in range(med+2, fin+1):
        maximo_provisorio += arr[i]
        if maximo_provisorio > maximo_cen_der:
            maximo_cen_der = maximo_provisorio
            optimo_cen_fin = i

    maximo_cen = maximo_cen_izq + maximo_cen_der

    maximo_local = max(maximo_izq, maximo_cen, maximo_der)

    if maximo_local == maximo_izq:
        return optimo_izq_ini, optimo_izq_fin, maximo_izq
    if maximo_local == maximo_cen:
        return optimo_cen_ini, optimo_cen_fin, maximo_cen
    if maximo_local == maximo_der:
        return optimo_der_ini, optimo_der_fin, maximo_der

'''
Teorema maestro
A = 2, B = 2, C = 1 (calcular maximo_cen tarda O(n))
Como log_B A = C, O(n log n)
'''