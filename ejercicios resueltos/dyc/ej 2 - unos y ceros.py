'''
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.

En este ejercicio se pide cumplir la tarea "en O(log(n))".
'''

def _indice_primer_cero(arr, izq, der):
    if izq>=der:
        return izq
    med = izq+((der-izq)//2)
    if arr[med] == 0 and arr[med-1] == 1:
        return med
    if arr[med] == 0 and arr[med-1] == 0:
        return _indice_primer_cero(arr, izq, med)
    if arr[med] == 1 and arr[med-1] == 1:
        return _indice_primer_cero(arr, med, der)

def indice_primer_cero(arr):
    if arr[len(arr)-1] == 1:
        return -1
    if arr[0] == 0:
        return 0
    return _indice_primer_cero(arr, 1, len(arr)-1)