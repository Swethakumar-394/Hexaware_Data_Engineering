def analyze_products(products):
    print("\nProduct Names and Prices:")
    for product_id, details in products.items():
        print(f"{details['name']} - ₹{details['price']}")

    most_expensive = max(products.items(), key=lambda x: x[1]["price"])
    least_expensive = min(products.items(), key=lambda x: x[1]["price"])

    return most_expensive, least_expensive