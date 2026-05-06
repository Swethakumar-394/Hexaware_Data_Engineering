import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="bronze_patient_visits",
    comment="Raw patient visit data"
)
def bronze_patient_visits():
    data = [
        (1, "Aarav Khan", "Hyderabad", "Cardiology", "Dr Sameer Sharma", 2, 1200, 5200, "Completed", "Paid"),
        (2, "Priya Reddy", "Bengaluru", "Dermatology", "Dr Kavita Iyer", 1, 800, 2800, "Completed", "Paid"),
        (3, "Rahul Mehta", "Mumbai", "Orthopedics", "Dr Imran Khan", 3, 1500, 7500, "Completed", "Paid"),
        (4, "Sneha Kapoor", "Delhi", "Pediatrics", "Dr Ramesh Reddy", 1, 900, 2900, "Pending", "Pending"),
        (5, "Kiran Patel", "Ahmedabad", "Cardiology", "Dr Joseph Mathew", 2, 1300, 5300, "Completed", "Paid"),
        (6, "Ananya Das", "Kolkata", "Neurology", "Dr Anita Mehta", 4, 2000, 10000, "Completed", "Paid"),
        (7, "Vikram Singh", "Chennai", "Dermatology", "Dr Fatima Ali", 1, 850, 2850, "Cancelled", "Cancelled")
    ]

    columns = [
        "visit_id", "patient_name", "city", "specialization",
        "doctor_name", "tests_count", "consultation_fee",
        "bill_amount", "visit_status", "payment_status"
    ]

    return spark.createDataFrame(data, columns)


@dlt.table(
    name="silver_patient_visits",
    comment="Cleaned patient visit data"
)
def silver_patient_visits():
    bronze_df = dlt.read("bronze_patient_visits")

    return bronze_df \
        .filter(col("visit_id").isNotNull()) \
        .filter(col("patient_name").isNotNull()) \
        .filter(col("bill_amount") > 0) \
        .filter(col("visit_status") != "Cancelled") \
        .withColumn("test_cost", col("tests_count") * lit(500)) \
        .withColumn("total_bill", col("consultation_fee") + col("test_cost")) \
        .withColumn("patient_name", trim(col("patient_name"))) \
        .withColumn("city", trim(col("city"))) \
        .withColumn("specialization", trim(col("specialization")))


@dlt.table(
    name="gold_city_revenue",
    comment="Revenue summary by city"
)
def gold_city_revenue():
    silver_df = dlt.read("silver_patient_visits")

    return silver_df.groupBy("city") \
        .agg(
            count("visit_id").alias("total_visits"),
            sum("bill_amount").alias("total_revenue"),
            avg("bill_amount").alias("average_bill")
        )


@dlt.table(
    name="gold_specialization_revenue",
    comment="Revenue summary by specialization"
)
def gold_specialization_revenue():
    silver_df = dlt.read("silver_patient_visits")

    return silver_df.groupBy("specialization") \
        .agg(
            count("visit_id").alias("total_visits"),
            sum("bill_amount").alias("total_revenue"),
            avg("bill_amount").alias("average_bill")
        )