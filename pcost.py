# pcost.py
#


import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename) as a:
        rows = csv.reader(a)
        headers = next(rows)
        for rowno, row in enumerate(rows, start = 2):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price

        # To catch errors in the input file:

            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost
    
import sys    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)