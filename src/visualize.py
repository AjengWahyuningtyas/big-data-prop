import matplotlib.pyplot as plt

# Define the sets
expensive = set()
not_expensive = set()

# Define the prediction scores
prediction_scores = []

# Process the data and populate the sets and prediction scores
data = [
    {
        "Title": "KOST 650ribu (Gratis Listrik, Air) Kampus Mahendradata SMK Bali Dewata",
        "Price": 650000,
        "Predicted Label": "expensive",
        "Predicted Score": 0.629176676273346
    },
    {
        "Title": "Dijual di bawah NJOP, Rp 675 jt, di Jimbaran, Bali",
        "Price": 675000000,
        "Predicted Label": "expensive",
        "Predicted Score": 0.6444523930549622
    },
    {
        "Title": "Tanah dekat JALAN UTAMA SEDAP MALAM",
        "Price": 600000000,
        "Predicted Label": "expensive",
        "Predicted Score": 0.7912328839302063
    },
    # Add more data here...
]

for item in data:
    if item["Predicted Label"] == "expensive":
        expensive.add(item["Title"])
    else:
        not_expensive.add(item["Title"])
    prediction_scores.append(item["Predicted Score"])

# Calculate the total count for each category
expensive_count = len(expensive)
not_expensive_count = len(not_expensive)

# Create the donut chart
labels = ["Expensive", "Not Expensive"]
sizes = [expensive_count, not_expensive_count]
colors = ["red", "blue"]
explode = (0.1, 0)  # Explode the first slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a white circle at the center to create a donut chart
center_circle = plt.Circle((0, 0), 0.7, color='white')
plt.gca().add_artist(center_circle)

# Set plot attributes
plt.title("Expensive vs Not Expensive Products")

# Save the plot as an image file
plt.savefig("donut_chart.png", dpi=300)

# Display a message once the file is saved
print("Donut chart saved as donut_chart.png")
