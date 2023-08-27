import csv


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            nm = record['name']
            share = int(record['shares'])
            price_init = float(record['price'])
            holding = {'name': nm,
                       'shares': share,
                       'price': price_init
                       }
            portfolio.append(holding)

    return portfolio

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        price_now = prices[stock['name']]
        report_line = (
        stock['name'], stock['shares'], price_now, price_now - stock['price'],)
        report.append(report_line)
    return report


if __name__ == '__main__':
    prices = read_prices('Data/prices.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

