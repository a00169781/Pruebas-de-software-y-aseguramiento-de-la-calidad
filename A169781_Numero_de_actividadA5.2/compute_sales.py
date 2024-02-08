"""This program computes the total cost
for all sales included in the second JSON archive.
"""

import sys
import json
from time import time

def main():
    """Rutina principal"""

    t1 = time()
    if len(sys.argv) != 3:
        usage = """\
    This program computes the total cost
    for all sales included in the second JSON archive.
    
    The program should be invoked the as follows:
    ./python3 compute_sales.py priceCatalogue.json salesRecord.json
    
    The result will be printed on a screen and on a
    file named SalesResults.txt. The total cost
    includes all items in the sale considering
    the cost for every item in the first file. 
"""
        print(usage)
        sys.exit(0)
    else:
        _prices = sys.argv[1]
        _sales = sys.argv[2]
        prices = {}
        sales = {}
        total_sales = 0
        with open(_prices, 'r', encoding="utf-8") as _prices_file:
            _prices_json = json.load(_prices_file)
        with open(_sales, 'r', encoding="utf-8") as _sales_file:
            _sales_json = json.load(_sales_file)

        for element in _prices_json:
            title = element['title']
            price = element['price']
            if title in prices:
                print('Product: ' + title + ' was already defined ignoring duplicates')
            else:
                prices[title] = price

        for element in _sales_json:
            product = element['Product']
            quantity = element['Quantity']
            if product not in sales:
                sales[product] = 0
            sales[product] += float(quantity)

        for product, quantity in sales.items():
            if product in prices:
                total_sales += prices[product] * quantity
            else:
                print('Price for ' + product + ' is not defined... SKIPING')


        t2 = time() - t1
        _tiempo = 'Tiempo de ejecución: ' + str(t2) + 's'
        _total = 'Total: ' + f"{total_sales:0.2f}"
        print(_tiempo)
        print(_total)

        with open('SalesResults.txt', 'w', encoding="utf-8") as f:
            f.write(_tiempo + "\n")
            f.write(_total)

if __name__ == "__main__":
    main()
