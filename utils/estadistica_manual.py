# utils/estadistica_manual.py

from collections import Counter
import math

def media(lista):
    return sum(lista) / len(lista) if lista else None

def mediana(lista):
    n = len(lista)
    if n == 0:
        return None
    lista_ordenada = sorted(lista)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

def moda(lista):
    if not lista:
        return None
    conteo = Counter(lista)
    max_freq = max(conteo.values())
    modas = [k for k, v in conteo.items() if v == max_freq]
    return modas if len(modas) > 1 else modas[0]

def varianza(lista):
    if len(lista) < 2:
        return None
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / (len(lista) - 1)

def desviacion_estandar(lista):
    v = varianza(lista)
    return math.sqrt(v) if v is not None else None

def rango(lista):
    return max(lista) - min(lista) if lista else None

def cuartiles(lista):
    if not lista:
        return None, None, None
    lista_ordenada = sorted(lista)
    n = len(lista)
    Q2 = mediana(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        Q1 = mediana(lista_ordenada[:mitad])
        Q3 = mediana(lista_ordenada[mitad:])
    else:
        Q1 = mediana(lista_ordenada[:mitad])
        Q3 = mediana(lista_ordenada[mitad+1:])
    return Q1, Q2, Q3

def rango_intercuartilico(lista):
    Q1, _, Q3 = cuartiles(lista)
    return Q3 - Q1 if Q1 is not None and Q3 is not None else None

def detectar_outliers_iqr(lista):
    Q1, _, Q3 = cuartiles(lista)
    iqr = Q3 - Q1
    lim_inf = Q1 - 1.5 * iqr
    lim_sup = Q3 + 1.5 * iqr
    return [x for x in lista if x < lim_inf or x > lim_sup]

def detectar_outliers_zscore(lista, umbral=3):
    m = media(lista)
    s = desviacion_estandar(lista)
    if s == 0 or s is None:
        return []
    return [x for x in lista if abs((x - m) / s) > umbral]
