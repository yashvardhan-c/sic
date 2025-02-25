import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'E:\Python_Learning\yash\Hackathon_dataset.csv')

df = df.head(20)

category_counts = df['Category'].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')

plt.title('Product ID vs Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Number of Products', fontsize=14)

plt.xticks(rotation=45) 
plt.tight_layout()  
plt.show()
