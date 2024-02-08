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
        # We read the first file, the json prices file
        with open(_prices, 'r', encoding="utf-8") as _prices_file:
            _prices_json = json.load(_prices_file)
        # We read the second file, the json seles file
        with open(_sales, 'r', encoding="utf-8") as _sales_file:
            _sales_json = json.load(_sales_file)
        # We inspect the prices json and pickup the members that have the relevant
        # information
        for element in _prices_json:
            if element['title'] in prices:
                print('Product: ' + element['title'] + ' was already defined ignoring duplicates')
            else:
                prices[element['title']] = element['price']
        # We inspect the sales json and pickup the members that have the relevant
        # information
        for element in _sales_json:
            if element['Product'] not in sales:
                sales[element['Product']] = 0
            sales[element['Product']] += float(element['Quantity'])
        # We walk all the sales and multiply the number of sold items by it price
        for product, quantity in sales.items():
            if product in prices:
                total_sales += prices[product] * quantity
            else:
                print('Price for ' + product + ' is not defined... SKIPING')

        # We print in STDOUT the information
        print('Tiempo de ejecución: ' + str(time() - t1) + 's')
        print('Total: ' + f"{total_sales:0.2f}")
        # We write the same information tp
        with open('SalesResults.txt', 'w', encoding="utf-8") as f:
            f.write('Tiempo de ejecución: ' + str(time() - t1) + 's' + "\n")
            f.write('Total: ' + f"{total_sales:0.2f}" + "\n")

if __name__ == "__main__":
    main()
