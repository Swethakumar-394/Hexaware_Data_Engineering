def calculate_customer_spending(orders, products):
    customer_spending = {}

    for order in orders:
        customer = order["customer"]
        product_id = order["product_id"]
        quantity = order["quantity"]

        amount = products[product_id]["price"] * quantity
        customer_spending[customer] = customer_spending.get(customer, 0) + amount

    return customer_spending


def top_customer(customer_spending):
    return max(customer_spending.items(), key=lambda x: x[1])


def customers_above_50000(customer_spending):
    result = {}
    for customer, amount in customer_spending.items():
        if amount > 50000:
            result[customer] = amount
    return result