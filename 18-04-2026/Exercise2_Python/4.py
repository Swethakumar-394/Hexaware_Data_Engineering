# Exercise 4 — JSON File (E-commerce Orders)

import json

with open("orders.json", "r") as file:
    data = json.load(file)

orders = data["orders"]

print("All orders:")
for order in orders:
    print(order)

total_revenue = 0
for order in orders:
    total_revenue += order["amount"]

print("\nTotal revenue:", total_revenue)

spending_per_customer = {}
for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    spending_per_customer[customer] = spending_per_customer.get(customer, 0) + amount

print("\nTotal spending per customer:")
print(spending_per_customer)

highest_spending_customer = max(spending_per_customer, key=spending_per_customer.get)
print("\nHighest spending customer:", highest_spending_customer)

orders_per_customer = {}
for order in orders:
    customer = order["customer"]
    orders_per_customer[customer] = orders_per_customer.get(customer, 0) + 1

print("\nTotal orders per customer:")
print(orders_per_customer)