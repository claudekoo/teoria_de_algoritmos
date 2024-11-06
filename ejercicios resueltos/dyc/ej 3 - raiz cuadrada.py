'''
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.
'''

def parte_entera_raiz(n):
    if n <= 0:
        return 0
    if n <= 3:
        return 1
    # encontrar el primer numero entero x donde x^2 >= n
    return _parte_entera_raiz(n, 0, n)

def _parte_entera_raiz(n, piso, techo):
    actual = piso+((techo-piso)//2)
    actual_al_cuadrado = actual*actual
    if actual_al_cuadrado == n:
        return actual
    if actual_al_cuadrado < n:
        if (actual+1)*(actual+1) > n:
            return actual
        else:
            return _parte_entera_raiz(n, actual, techo)
    else:
        return _parte_entera_raiz(n, piso, actual)
    