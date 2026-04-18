# Bonus Challenge — Product Sales Summary

import csv

summary = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = int(row["price"])
        revenue = quantity * price

        if product not in summary:
            summary[product] = {"qty": 0, "revenue": 0}

        summary[product]["qty"] += quantity
        summary[product]["revenue"] += revenue

print("Product Sales Summary")
for product, details in summary.items():
    print(f"{product} → Qty: {details['qty']} Revenue: {details['revenue']}")