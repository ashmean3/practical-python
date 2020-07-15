# pcost.py
#
# Exercise 1.31

import csv
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    a = open('Data/portfolio.csv', 'rt')
    rows = csv.reader(a)
    headers = next(rows)
    for row in rows:
        try:
            shares = int(row[1])
            price = float(row[2])
            total_cost += shares * price

        # To catch errors in the input file:

        except ValueError:
            print('Bad row:', row)

    return total_cost
    a.close()
    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)