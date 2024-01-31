"""Este programa calcula las estadisticas básicas de 
una lista de números
"""

from collections import Counter
import math
import fileinput
import sys
from time import time


def media(nums):
    """Calcula el promedio de una lista"""
    return sum(nums) / len(nums)

def mediana(nums):
    """Calcula la mediana de una lista"""
    nums.sort()
    n = len(nums)
    m = n // 2

    if n % 2 == 0:
        return (nums[m - 1] + nums[m]) / 2

    return nums[m]

def moda(nums):
    """Calcula la moda de una lista, regresando una lista, esta lista podrá contener
    varios valores los que aparecen con la frecuencia más alta"""
    c = Counter(nums)
    return[k for k, v in c.items() if v == c.most_common(1)[0][1]]

def dev_std(nums):
    """Calcula la desviación estandar de una muestra"""
    return(math.sqrt(varianza(nums)))

def varianza(nums):
    """Calcula la varianza de una muestra"""
    promedio = media(nums)
    helper_sum = 0

    for num in nums:
        helper_sum+=(num - promedio)**2

    _varianza = helper_sum/(len(nums) - 1)
    return _varianza

def is_float(string):
    """Revisa si un valor se puede tomar como número"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def main():
    """Rutina principal"""

    t1 = time()
    if len(sys.argv) != 2:
        usage = """\
    Este programa calcula las estadísticas básicas de una lista de números
    El programa lee los números de un archivo que se pasa como argumento

    El programa espera que cada número venga separado por un brinco de linea
    ejemplo de uso:
    ./python3 compute_statistics.py fileWithData.txt

    El programa generará el archivo StatisticsResults.txt con los resultados 
    calculados
"""
        print(usage)
        sys.exit(0)
    else:
        numeros = []
        for line in fileinput.input():
            if is_float(line.strip()):
                numeros.append(float(line.strip()))
            else:
                print("Elemento no es válido y será ignorado: " + line.strip())

    _total = 'Número de elementos: ' + str(len(numeros))
    _media = 'Media: ' + str(media(numeros))
    _mediana = 'Mediana: ' + str(mediana(numeros))
    _moda = 'Moda: ' + str(moda(numeros)[0:5]) # solamente vamos a imprimir los primeros 5 elementos
    _dev_std = 'Desviación Estandar: ' + str(dev_std(numeros))
    _varianza = 'Varianza: ' + str(varianza(numeros))
    t2 = time() - t1
    _tiempo = 'Tiempo de ejecución: ' + str(t2) + 's'

    print(_total)
    print(_media)
    print(_mediana)
    print(_moda)
    print(_dev_std)
    print(_varianza)
    print(_tiempo)

    with open('StatisticsResults.txt', 'w', encoding="utf-8") as f:
        sys.stdout = f
        print(_total)
        print(_media)
        print(_mediana)
        print(_moda)
        print(_dev_std)
        print(_varianza)
        print(_tiempo)



if __name__ == "__main__":
    main()
