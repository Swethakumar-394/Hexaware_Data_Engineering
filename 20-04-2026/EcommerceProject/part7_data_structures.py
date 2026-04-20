def get_product_revenue_tuples(product_revenue):
    revenue_tuples = []
    for product, revenue in product_revenue.items():
        revenue_tuples.append((product, revenue))
    return revenue_tuples


def visitors_who_never_ordered(visits, orders):
    visitors_set = set(visits)
    customers_set = set()

    for order in orders:
        customers_set.add(order["customer"])

    return visitors_set - customers_set


def customers_ordered_but_visited_once_or_less(visits, orders):
    visit_count = {}
    for visitor in visits:
        visit_count[visitor] = visit_count.get(visitor, 0) + 1

    customers_set = set()
    for order in orders:
        customers_set.add(order["customer"])

    result = []
    for customer in customers_set:
        if visit_count.get(customer, 0) <= 1:
            result.append(customer)

    return result