import json
import csv


def load_visits(filename):
    with open(filename, "r") as file:
        visits = [line.strip() for line in file if line.strip()]
    return visits


def load_products(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    products = {}
    for product in data["products"]:
        products[product["product_id"]] = {
            "name": product["name"],
            "price": product["price"]
        }

    return products


def load_orders(filename):
    orders = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["order_id"] = int(row["order_id"])
            row["product_id"] = int(row["product_id"])
            row["quantity"] = int(row["quantity"])
            orders.append(row)

    return orders