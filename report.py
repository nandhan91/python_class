'''
    Report Table to show the fluctuations in prices of inventory
'''

import csv

def read_prices(filename):
    prices = dict()
    with open(filename) as FH:
        data = csv.reader(FH)
        for row in data:
            try:
                prices[row[0]] = float(row[1])
            except IndexError as e:
                continue

    return prices


def read_inventory(filename):
    inventory = list()
    with open(filename) as FH:
        data = csv.reader(FH)
        headers = next(data)
        for row in data:
            record = dict(zip(headers, row))
            prod = {
                    'name'  : record['name'],
                    'quant' : int(record['quant']),
                    'price' : float(record['price']),
                }
            inventory.append(prod)

    return inventory

def make_report(inventory, prices):
    report = list()
    for prod in inventory:
        name = prod['name']
        quant = prod['quant']
        latest_price = prices[name]
        change = latest_price - prod['price']
        report.append( (name, quant, latest_price, change) )

    return report

def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)

    sep = ['-' * 10] * 4
    print('%10s %10s %10s %10s' % tuple(sep))

    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def inventory_report(inventory_filename, prices_filename):
    inventory = read_inventory(inventory_filename)
    latest_prices = read_prices(prices_filename)
    report = make_report(inventory, latest_prices)
    print_report(report)

# Main
inventory_report("../Data/inventory.csv", "../Data/prices.csv")
