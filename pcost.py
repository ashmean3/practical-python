# pcost.py
#
# Exercise 1.30 to 1.33

import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename) as a:
        rows = csv.reader(a)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            try:
                shares = int(row[1])
                price = float(row[2])
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