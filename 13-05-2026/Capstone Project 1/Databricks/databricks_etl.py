from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName('DatabricksRetailETL') \
    .getOrCreate()

sales_df = spark.read.csv(
    '/FileStore/cleaned_sales.csv',
    header=True,
    inferSchema=True
)

products_df = spark.read.csv(
    '/FileStore/products.csv',
    header=True,
    inferSchema=True
)

final_df = sales_df.join(
    products_df,
    on='product_id',
    how='inner'
)

final_df = final_df.withColumn(
    'profit_margin',
    ((col('profit') / col('revenue')) * 100)
)

final_df.write.format('delta') \
    .mode('overwrite') \
    .save('/FileStore/final_metrics')

final_df.show()
