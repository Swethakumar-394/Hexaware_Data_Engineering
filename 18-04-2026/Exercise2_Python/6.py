# Exercise 6 — CSV File (Sales Dataset)

import csv

sales = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = int(row["price"])
        sales.append(row)

total_sales_revenue = 0
for item in sales:
    total_sales_revenue += item["quantity"] * item["price"]

print("Total sales revenue:", total_sales_revenue)

quantity_per_product = {}
for item in sales:
    product = item["product"]
    quantity_per_product[product] = quantity_per_product.get(product, 0) + item["quantity"]

print("\nTotal quantity sold per product:")
print(quantity_per_product)

revenue_per_product = {}
for item in sales:
    product = item["product"]
    revenue = item["quantity"] * item["price"]
    revenue_per_product[product] = revenue_per_product.get(product, 0) + revenue

print("\nTotal revenue per product:")
print(revenue_per_product)

highest_sales_product = max(revenue_per_product, key=revenue_per_product.get)
print("\nProduct with highest sales:", highest_sales_product)

print("\nProducts with sales above 50,000:")
for product, revenue in revenue_per_product.items():
    if revenue > 50000:
        print(product, "→", revenue)