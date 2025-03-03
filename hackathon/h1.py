import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'E:\Python_Learning\yash\Hackathon_dataset.csv')

df = df.head(20)


sku_stock_data = df.groupby('SKU')['Sales_Amount'].sum()

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sku_stock_data, labels=sku_stock_data.index, autopct='%1.1f%%', startangle=140)
plt.title('SKU vs Sales amount')
plt.axis('equal')
plt.show()
