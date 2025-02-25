import pandas as pd
import matplotlib.pyplot as plt

# Load the retail dataset
df = pd.read_csv(r'E:\Python_Learning\yash\Hackathon_dataset.csv')

df = df.head(20)

# Assume the dataset contains 'Product ID' and 'Category' columns
# Let's count how many products exist for each category
category_counts = df['Category'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')

# Adding titles and labels
plt.title('Product ID vs Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Number of Products', fontsize=14)

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to avoid label clipping
plt.show()
