import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('superstore_sales.csv', encoding='latin1')

# Clean data
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

# Monthly sales trend
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='line', title='Monthly Sales Trend', ylabel='Sales', xlabel='Month', marker='o')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_sales_trend.png')
plt.clf()

# Sales by Sub-Category
top_subcategories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
top_subcategories.head(10).plot(kind='bar', title='Top Sub-Categories by Sales')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/sales_by_subcategory.png')
plt.clf()

# Region-wise sales (pie chart)
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/region_sales_pie.png')
plt.clf()

print("Charts saved in 'charts/' folder.")
