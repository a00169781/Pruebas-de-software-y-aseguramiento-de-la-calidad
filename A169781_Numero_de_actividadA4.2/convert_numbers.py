"""Este programa convierte base numero base 10 a binario y hexadecimal
"""

import fileinput
import sys
from time import time


def main():
    """Rutina principal"""

    t1 = time()
    if len(sys.argv) != 2:
        usage = """\
    Este programa convierte una lista de números base 10 a
    base 2 (binario) y base 16 (hexadecimal)
    ./python3 convert_numbers.py fileWithData.txt

    El programa generará el archivo ConvertionResults.txt con los resultados 
    calculados
"""
        print(usage)
        sys.exit(0)
    else:
        with open('ConvertionResults.txt', 'w', encoding="utf-8") as f:
            for line in fileinput.input():
                if line.strip().isnumeric():
                    _int = int(line.strip())
                    _bin = f"{_int:08b}"
                    _hex = str(hex(_int))
                    _str = str(_int) + ' ' + _bin + ' ' + _hex[2:]
                    print(_str)
                    f.write(_str)
                else:
                    print("Elemento no es válido y será ignorado: " + line.strip())

            t2 = time() - t1
            _tiempo = 'Tiempo de ejecución: ' + str(t2) + 's'
            print(_tiempo)
            f.write(_tiempo)



if __name__ == "__main__":
    main()
