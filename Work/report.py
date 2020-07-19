# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Read holdings from the portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':(row[0]), 
                        'shares':int(row[1]), 
                        'price':float(row[2])
                      }
            portfolio.append(holding)    
    return portfolio

# Exercise 2.6

def read_prices (filename):
    prices = {}

    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass
    return prices

# Exercise 2.7

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices ('Data/prices.csv')

total_cost = 0.00
current_value = 0.00
for s in portfolio:
    total_cost += s['shares'] * s['price']
    current_value += s['shares'] * prices[s['name']]

print ('Total cost:', total_cost)
print ('Current Value:', current_value)
print (f'Gain/Loss: {(current_value-total_cost):.2f}')