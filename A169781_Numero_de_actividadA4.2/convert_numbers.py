"""Este programa convierte base numero base 10 a binario y hexadecimal
"""

import fileinput
import sys
from time import time

def is_int(s):
    """Función que revisa si el string es entero incluyendo negativos"""
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

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
                _num = line.strip()
                if is_int(_num):
                    _int = int(_num)
                    if _int < 0:
                        _bin = str(bin(_int & 0b1111111111111111111111111111111111111111))
                        _hex = str(hex(_int & 0b1111111111111111111111111111111111111111))
                    else:
                        _bin = str(bin(_int))
                        _hex = str(hex(_int))
                    _str = str(_int) + ' ' + _bin[2:] + ' ' + _hex[2:]
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
