from part1_visits import analyze_visits
from part2_products import analyze_products
from part3_orders import analyze_orders
from part4_sales import calculate_revenue, highest_selling_product
from part5_customers import calculate_customer_spending, top_customer, customers_above_50000
from part6_functions import load_visits, load_products, load_orders
from part7_data_structures import (
    get_product_revenue_tuples,
    visitors_who_never_ordered,
    customers_ordered_but_visited_once_or_less
)
from part8_report import generate_report


def main():
    visits = load_visits("website_visits.txt")
    products = load_products("products.json")
    orders = load_orders("orders.csv")

    # Part 1
    total_visits, unique_visitors, visit_count, most_frequent_visitor = analyze_visits(visits)
    print("\nTotal Website Visits:", total_visits)
    print("Unique Visitors:", unique_visitors)
    print("Visit Count:", visit_count)
    print("Most Frequent Visitor:", most_frequent_visitor)

    # Part 2
    most_expensive, least_expensive = analyze_products(products)
    print("\nMost Expensive Product:", most_expensive[1]["name"], "-", most_expensive[1]["price"])
    print("Least Expensive Product:", least_expensive[1]["name"], "-", least_expensive[1]["price"])

    # Part 3
    quantity_per_product, orders_per_customer = analyze_orders(orders)
    print("\nTotal Quantity Sold Per Product:", quantity_per_product)
    print("Total Orders Per Customer:", orders_per_customer)

    # Part 4
    order_revenues, total_revenue, product_revenue = calculate_revenue(orders, products)
    print("\nRevenue for Each Order:")
    for order_id, revenue in order_revenues:
        print(f"Order {order_id} -> ₹{revenue}")

    print("\nTotal Revenue:", total_revenue)
    print("Revenue Per Product:", product_revenue)

    highest_product = highest_selling_product(product_revenue)
    print("Highest Selling Product by Revenue:", highest_product)

    # Part 5
    customer_spending = calculate_customer_spending(orders, products)
    print("\nCustomer Spending:", customer_spending)

    highest_spending_customer = top_customer(customer_spending)
    print("Highest Spending Customer:", highest_spending_customer)

    above_50000 = customers_above_50000(customer_spending)
    print("Customers Who Spent More Than ₹50,000:", above_50000)

    # Part 7 + Final Challenge
    revenue_tuples = get_product_revenue_tuples(product_revenue)
    print("\n(Product, Revenue) Tuples:", revenue_tuples)

    never_ordered = visitors_who_never_ordered(visits, orders)
    print("Visitors Who Visited But Never Ordered Anything:", never_ordered)

    low_visit_customers = customers_ordered_but_visited_once_or_less(visits, orders)
    print("Customers Who Ordered But Never Visited More Than Once:", low_visit_customers)

    # Part 8
    generate_report(
        "sales_report.txt",
        total_visits,
        unique_visitors,
        total_revenue,
        highest_spending_customer,
        product_revenue
    )

    print("\nSales report generated successfully as sales_report.txt")


if __name__ == "__main__":
    main()