# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    from collections import Iterable
    if select and has_headers ==False:
            raise RuntimeError("select argument requires column headers")
    if isinstance(filename, str):
        f = open(filename, 'rt')
        rows = csv.reader(f, delimiter=delimiter)             
    else:

        for lines in filename:
            
            rows = csv.reader(list(filename), delimiter = delimiter)

    if select and not has_headers:
        raise RuntimeError("select requires column headers")
       
        # Read the file headers
    if has_headers:
        headers = next(rows)
    else:
        []

    records = []

    if select:
        records_sel = []
        for line in records:
            line_sel = {columnname: line[columnname] for columnname in select}
            records_sel.append(line_sel)
        records = records_sel
         
    
    
    for rowno, row in enumerate(rows,1):
        if not row:    # Skip rows with no data
            continue

        # Applying conversion type to the row  
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")               

        if has_headers:
            record= dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records