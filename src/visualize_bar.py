import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('dataset/csv/labeled_testdata_v2.csv')

# Count the number of expensive and not expensive products
expensive_count = data[data['Predicted Label'] == 'expensive'].shape[0]
not_expensive_count = data[data['Predicted Label'] != 'expensive'].shape[0]

# Create the labels and counts
labels = ['Expensive', 'Not Expensive']
counts = [expensive_count, not_expensive_count]

# Create the bar chart
fig, ax = plt.subplots()
x = range(len(labels))
bars = ax.bar(x, counts)

# Set the x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Set the y-axis label
ax.set_ylabel('Count')

# Add a title to the chart
ax.set_title('Count of Expensive and Not Expensive Products')

# Add the counts as annotations on top of the bars
for i, bar in enumerate(bars):
    count = counts[i]
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count), ha='center', va='bottom')

# Adjust the layout to prevent overlapping of labels
plt.tight_layout()

# Save the plot as an image file
plt.savefig("bar_chart.png", dpi=300)

# Display a message once the file is saved
print("Bar chart saved as bar_chart.png")
