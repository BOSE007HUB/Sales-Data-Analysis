
# Sales Data Analysis - Using Uploaded Sample CSV

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Display first few rows
print("First few rows of the dataset:")
print(data.head())

# Step 1: Clean & inspect data
print("\nColumn Info:")
print(data.info())

# Drop rows with missing Order Date or Product
data.dropna(subset=['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERDATE', 'CITY'], inplace=True)

# Step 2: Feature Engineering
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors='coerce')
data['Sales'] = data['QUANTITYORDERED'] * data['PRICEEACH']
data['Month'] = data['ORDERDATE'].dt.month
data['Year'] = data['ORDERDATE'].dt.year

# Step 3: Monthly Sales Trend
monthly_sales = data.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Year')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Sales by City
city_sales = data.groupby('CITY')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=city_sales.values, y=city_sales.index)
plt.title('Total Sales by City')
plt.xlabel('Total Sales')
plt.ylabel('City')
plt.tight_layout()
plt.show()

# Step 5: Top Products by Quantity Ordered
top_products = data.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Quantity Ordered')
plt.xlabel('Total Quantity Ordered')
plt.ylabel('Product Code')
plt.tight_layout()
plt.show()

# Step 6: Price vs Quantity Ordered (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PRICEEACH', y='QUANTITYORDERED', data=data, alpha=0.6)
plt.title('Price vs Quantity Ordered')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
plt.grid(True)
plt.tight_layout()
plt.show()
