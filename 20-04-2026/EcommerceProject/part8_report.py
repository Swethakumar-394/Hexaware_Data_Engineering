def generate_report(filename, total_visits, unique_visitors, total_revenue, top_customer, product_revenue):
    with open(filename, "w") as file:
        file.write("E-Commerce Sales Report\n")
        file.write("========================\n")
        file.write(f"Total Website Visits: {total_visits}\n")
        file.write(f"Unique Visitors: {len(unique_visitors)}\n")
        file.write(f"Total Revenue: Rs.{total_revenue}\n")
        file.write(f"Top Customer: {top_customer[0]} (Rs.{top_customer[1]})\n")
        file.write("\nProduct Sales\n")
        file.write("-------------\n")

        for product, revenue in product_revenue.items():
            file.write(f"{product} -> Rs.{revenue}\n")