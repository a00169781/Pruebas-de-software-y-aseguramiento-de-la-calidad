"""Este programa cuenta las occurrencias de cada palabra en un archivo
el programa ignora mayusculas y puntuación, sin embargo plurales y palabras
derivas las toma como diferentes.
"""

import sys
from time import time
import re
from collections import Counter

def main():
    """Rutina principal"""

    t1 = time()
    if len(sys.argv) != 2:
        usage = """\
    Este programa cuenta las occurrencias de cada palabra en un archivo
el programa ignora mayusculas y puntuación, sin embargo plurales y palabras
derivas las toma como diferentes.
    ./python3 word_count.py fileWithData.txt

    El programa generará el archivo WordCountResults.txt con los resultados 
    calculados
"""
        print(usage)
        sys.exit(0)
    else:
        _file = sys.argv[1]
        palabras = re.findall(r'\w+', open(_file, encoding="utf-8").read().lower())
        elementos = 0
        with open('WordCountResults.txt', 'w', encoding="utf-8") as f:
            for palabra, ocurrencias in Counter(palabras).most_common():
                elementos += ocurrencias
                _str = palabra + " " + str(ocurrencias)
                print(_str)
                f.write(_str + "\n")
            print('Total de palabras analizadas: ' + str(elementos))
            f.write('Total de palabras analizadas: ' + str(elementos) + "\n")
            t2 = time() - t1
            _tiempo = 'Tiempo de ejecución: ' + str(t2) + 's'
            print(_tiempo)
            f.write(_tiempo + "\n")


if __name__ == "__main__":
    main()
