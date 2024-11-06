'''
Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    med = len(arr) // 2
    izq = arr[:med]
    der = arr[med:]

    izq = merge_sort(izq)
    der = merge_sort(der)

    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i_izq = 0
    i_der = 0

    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq] <= der[i_der]:
            resultado.append(izq[i_izq])
            i_izq += 1
        else:
            resultado.append(der[i_der])
            i_der += 1

    resultado = resultado+izq[i_izq:]
    resultado = resultado+der[i_der:]

    return resultado

'''
Teorema maestro:
A: 2 B: 2 C: 1
Como log_B(A)=C, O(N^C*log(N)) = O(N*log(N))
'''