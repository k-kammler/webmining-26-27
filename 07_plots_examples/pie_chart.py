import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
sizes = [40, 35, 25]
colors = ['red', 'green', 'blue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=90)
plt.title("Kreisdiagramm")
plt.savefig('pie_chart.png')
plt.show()
