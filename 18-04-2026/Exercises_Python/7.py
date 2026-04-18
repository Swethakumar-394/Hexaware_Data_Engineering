products = {
    "Laptop": 75000,
    "Mobile": 30000,
    "Tablet": 25000
}

for product in products:
    products[product] = products[product] * 1.10

print("Updated prices:")
for product, price in products.items():
    print(product, "-", price)
