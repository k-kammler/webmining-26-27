import matplotlib.pyplot as plt
import squarify

data = {
    "Technologie": {
        "Smartphones": 12,
        "Laptops": 8,
        "Tablets": 10
    },
    "Haushaltswaren": {
        "Küchengeräte": 10,
        "Reinigungsgeräte": 15,
        "Möbel": 5
    },
    "Mode": {
        "Herren": 10,
        "Damen": 20,
        "Kinder": 10
    }
}

category_colors = {
    "Technologie": "lightblue",
    "Haushaltswaren": "lightgreen",
    "Mode": "lightcoral"
}

categories = []
sizes = []
labels = []
colors = []
edge_colors = []

for category, subcategories in data.items():
    for subcategory, value in subcategories.items():
        categories.append(category)
        sizes.append(value)
        labels.append(f"{subcategory}\n{value}%")
        colors.append(category_colors[category])
        edge_colors.append('black') 

squarify.plot(sizes=sizes, label=labels, color=colors, edgecolor=edge_colors, linewidth=1.5)

plt.title("Treemap")
plt.axis("off")  
plt.savefig("treemap.png")
plt.show()
