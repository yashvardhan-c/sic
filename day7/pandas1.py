# PIE CHART
# Problem Statement: Representing the market share of different brands.
# Question: Which brand has the largest market share?
import matplotlib.pyplot as plt
# Define sizes and labels for pie chart
sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()