import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="bronze_orders",
    comment="Raw retail order data"
)
def bronze_orders():
    data = [
        (301, "Rice Bag", "Groceries", "Hyderabad", "Reddy Traders", "Hyderabad", 20, 1200, 24000, "Delivered", "Paid"),
        (302, "Wheat Flour", "Groceries", "Bengaluru", "Reddy Traders", "Hyderabad", 35, 900, 31500, "Delivered", "Paid"),
        (303, "LED TV", "Electronics", "Delhi", "Elite Electronics", "Delhi", 2, 45000, 90000, "Delivered", "Paid"),
        (304, "Mobile Phone", "Electronics", "Hyderabad", "Smart Electronics", "Kolkata", 5, 25000, 125000, "Pending", "Pending"),
        (305, "Laptop", "Electronics", "Pune", "Elite Electronics", "Delhi", 3, 62000, 186000, "Delivered", "Paid"),
        (306, "Milk Pack", "Dairy", "Chennai", "Fresh Dairy Ltd", "Chennai", 50, 60, 3000, "Delivered", "Paid"),
        (307, "Cheese Block", "Dairy", "Delhi", "Fresh Dairy Ltd", "Chennai", 18, 450, 8100, "Cancelled", "Cancelled"),
        (308, "Mixer Grinder", "Home Appliances", "Kolkata", "HomeNeeds Pvt Ltd", "Pune", 7, 3500, 24500, "Delivered", "Paid"),
        (309, "Water Purifier", "Home Appliances", "Delhi", "Kitchen World", "Chennai", 4, 12000, 48000, "Pending", "Pending"),
        (310, "Ceiling Fan", "Home Appliances", "Ahmedabad", "HomeNeeds Pvt Ltd", "Pune", 12, 2800, 33600, "Delivered", "Paid")
    ]

    columns = [
        "order_id", "product_name", "category", "warehouse_city",
        "supplier_name", "supplier_city", "quantity", "price",
        "bill_amount", "order_status", "payment_status"
    ]

    return spark.createDataFrame(data, columns)


@dlt.table(
    name="silver_orders",
    comment="Cleaned retail order data with total revenue calculation"
)
def silver_orders():
    bronze_df = dlt.read("bronze_orders")

    return bronze_df \
        .filter(col("order_id").isNotNull()) \
        .filter(col("product_name").isNotNull()) \
        .filter(col("quantity") > 0) \
        .filter(col("price") > 0) \
        .filter(col("order_status") != "Cancelled") \
        .withColumn("category", upper(trim(col("category")))) \
        .withColumn("product_name", trim(col("product_name"))) \
        .withColumn("warehouse_city", trim(col("warehouse_city"))) \
        .withColumn("total_revenue", col("quantity") * col("price"))


@dlt.table(
    name="gold_city_revenue",
    comment="Gold table showing revenue by city"
)
def gold_city_revenue():
    silver_df = dlt.read("silver_orders")

    return silver_df.groupBy("warehouse_city") \
        .agg(
            count("order_id").alias("total_orders"),
            sum("total_revenue").alias("total_revenue"),
            avg("total_revenue").alias("average_revenue")
        )


@dlt.table(
    name="gold_category_revenue",
    comment="Gold table showing revenue by category"
)
def gold_category_revenue():
    silver_df = dlt.read("silver_orders")

    return silver_df.groupBy("category") \
        .agg(
            count("order_id").alias("total_orders"),
            sum("total_revenue").alias("total_revenue"),
            avg("total_revenue").alias("average_revenue")
        )
