'''
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

    Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico: func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.

    Justificar el orden del algoritmo mediante el teorema maestro.

En este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))"
'''

def _posicion_pico(v, ini, fin):
    med = fin - ((fin-ini)//2)
    if v[med] > v[med-1] and v[med] > v[med+1]:
        return med
    if v[med] > v[med-1]:
        return _posicion_pico(v, med, fin)
    else:
        return _posicion_pico(v, ini, med)

'''
Teorema maestro:
A: 1 B: 2 C: 0
Como log_B(A) = C, O(log(O^c*n)) = O(log(n))
'''