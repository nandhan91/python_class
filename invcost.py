'''
    Find the total cost of inventory
    Using inventory_cost function
'''
import sys
import csv

def inventory_cost(filename):
    total = 0.0
    with open(filename) as FH:
        data = csv.reader(FH)
        headers = next(data)
        for rowno, row in enumerate(data, start=1):
            prod = dict(zip(headers, row))
            print(prod)
            try:
                quant = int(prod['quant'])
                price = float(prod['price'])
                total += quant * price
            except ValueError as e:
                print("Row", rowno, "Couldn't convert:", row)
                continue

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "../Data/inventory.csv"

cost = inventory_cost(filename)
print("Total cost", cost)
