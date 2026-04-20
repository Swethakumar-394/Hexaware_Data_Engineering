def calculate_revenue(orders, products):
    order_revenues = []
    total_revenue = 0
    product_revenue = {}

    for order in orders:
        order_id = order["order_id"]
        product_id = order["product_id"]
        quantity = order["quantity"]

        product_name = products[product_id]["name"]
        price = products[product_id]["price"]

        revenue = price * quantity
        order_revenues.append((order_id, revenue))
        total_revenue += revenue

        product_revenue[product_name] = product_revenue.get(product_name, 0) + revenue

    return order_revenues, total_revenue, product_revenue


def highest_selling_product(product_revenue):
    return max(product_revenue.items(), key=lambda x: x[1])