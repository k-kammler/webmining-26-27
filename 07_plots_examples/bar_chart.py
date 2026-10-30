import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [4, 7, 3]

plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title("Balkendiagramm")
plt.xlabel("Kategorien")
plt.ylabel("Werte")
plt.grid()
plt.savefig("bar_chart.png")
plt.show()