import pandas as pd
import matplotlib.pyplot as plt

# Load the retail dataset
df = pd.read_csv(r'E:\Python_Learning\yash\Hackathon_dataset.csv')

df = df.head(20)

# Assume the dataset contains 'Product ID' and 'Units Sold' columns
# Let's sum the units sold for each product
product_sales = df.groupby('Product ID')['Units Sold'].sum()

# Plot the histogram (bar chart)
plt.figure(figsize=(12, 6))
product_sales.plot(kind='bar', color='lightgreen')

# Adding titles and labels
plt.title('Product ID vs Units Sold', fontsize=16)
plt.xlabel('Product ID', fontsize=14)
plt.ylabel('Total Units Sold', fontsize=14)

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to avoid label clipping
plt.show()
