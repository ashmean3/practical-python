# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        

        records = []
        
        for rowno, row in enumerate(rows,1):
            if not row:    # Skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices]

            if indices:
                row = [ row[index] for index in indices]

          # Applying conversion type to the row  
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            if has_headers:
                record= dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

records= parse_csv('Data/portfolio.csv', types= [str, int, float])
print(records)
records= parse_csv('Data/portfolio.csv', types= [str, int], select = ['name', 'shares'])
print(records)
#records= parse_csv('Data/prices.csv', select = ['name', 'price'], has_headers=False)
#print(records)
records= parse_csv('Data/portfolio.dat', types= [str, int, float], delimiter=' ')
print(records)
portfolio=parse_csv('Data/missing.csv', types=[str, int, float])
print(portfolio)