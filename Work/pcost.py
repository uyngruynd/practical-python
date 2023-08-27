import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for i, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            shares = int(record['shares'])
            price = float(record['price'])
            total_cost += shares * price
            print(row)
        except ValueError:
            print(f"Row {i}: Couldn't parse: {row}")

    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)