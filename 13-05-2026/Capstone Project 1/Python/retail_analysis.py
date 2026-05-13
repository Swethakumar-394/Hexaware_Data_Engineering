import pandas as pd
import numpy as np

sales_df = pd.read_csv('../data/sales.csv')
products_df = pd.read_csv('../data/products.csv')
stores_df = pd.read_csv('../data/stores.csv')

sales_df.fillna(0, inplace=True)

sales_df['quantity'] = sales_df['quantity'].astype(int)
sales_df['price'] = sales_df['price'].astype(float)
sales_df['cost'] = sales_df['cost'].astype(float)

sales_df['revenue'] = sales_df['quantity'] * sales_df['price']
sales_df['profit'] = sales_df['revenue'] - (sales_df['quantity'] * sales_df['cost'])
sales_df['discount_amount'] = sales_df['revenue'] * sales_df['discount'] / 100

sales_df['profit_margin'] = np.where(
    sales_df['revenue'] > 0,
    (sales_df['profit'] / sales_df['revenue']) * 100,
    0
)

store_summary = sales_df.groupby('store_id')[['revenue', 'profit']].sum().reset_index()
product_summary = sales_df.groupby('product_id')[['revenue', 'profit']].sum().reset_index()

print(store_summary)
print(product_summary)

sales_df.to_csv('../outputs/cleaned_sales.csv', index=False)
store_summary.to_csv('../outputs/store_summary.csv', index=False)
