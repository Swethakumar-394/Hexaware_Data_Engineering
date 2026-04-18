#E-commerce Order Analysis

orders = [
    {"order_id": 1, "customer": "Rahul", "amount": 2500},
    {"order_id": 2, "customer": "Sneha", "amount": 1800},
    {"order_id": 3, "customer": "Rahul", "amount": 3200},
    {"order_id": 4, "customer": "Amit", "amount": 1500}
]

total_spending = {}
order_count = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in total_spending:
        total_spending[customer] += amount
        order_count[customer] += 1
    else:
        total_spending[customer] = amount
        order_count[customer] = 1

highest_spender = max(total_spending, key=total_spending.get)

print("Total spending per customer:", total_spending)
print("Highest spending customer:", highest_spender, "-", total_spending[highest_spender])
print("Total orders per customer:", order_count)