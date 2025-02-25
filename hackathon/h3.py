import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'E:\Python_Learning\yash\Hackathon_dataset.csv')

df = df.head(20)


product_sales = df.groupby('Product ID')['Units Sold'].sum()


plt.figure(figsize=(12, 6))
product_sales.plot(kind='bar', color='lightgreen')


plt.title('Product ID vs Units Sold', fontsize=16)
plt.xlabel('Product ID', fontsize=14)
plt.ylabel('Total Units Sold', fontsize=14)

plt.xticks(rotation=45) 
plt.tight_layout()  
plt.show()
