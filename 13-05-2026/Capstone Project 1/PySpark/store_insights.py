from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName('RetailSalesAnalysis') \
    .getOrCreate()

sales_df = spark.read.csv(
    '../outputs/cleaned_sales.csv',
    header=True,
    inferSchema=True
)

underperforming = sales_df.filter(
    (col('revenue') < 10000) |
    (col('returns') > 2)
)

monthly_revenue = sales_df.groupBy(
    'store_id'
).agg(
    avg('revenue').alias('avg_monthly_revenue')
)

underperforming.show()
monthly_revenue.show()

underperforming.toPandas().to_csv(
    '../outputs/underperforming_products.csv',
    index=False
)
