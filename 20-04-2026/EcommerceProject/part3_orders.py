def analyze_orders(orders):
    print("\nEach Order:")
    for order in orders:
        print(order)

    quantity_per_product = {}
    orders_per_customer = {}

    for order in orders:
        product_id = order["product_id"]
        customer = order["customer"]
        quantity = order["quantity"]

        quantity_per_product[product_id] = quantity_per_product.get(product_id, 0) + quantity
        orders_per_customer[customer] = orders_per_customer.get(customer, 0) + 1

    return quantity_per_product, orders_per_customer