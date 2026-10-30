import matplotlib.pyplot as plt

labels = ['Bar 1', 'Bar 2']
values = [1, 1000]

plt.figure(figsize=(6, 4))
plt.bar(labels, values)

plt.yscale('log')

plt.title('Beispiel 1: Logarithmische Y-Achse')
plt.xlabel('Kategorien')
plt.ylabel('Werte (MIT log)')

plt.savefig('log_bar_plot.png')
plt.show()
