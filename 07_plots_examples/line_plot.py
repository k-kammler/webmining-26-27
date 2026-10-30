import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)
values1 = np.cumsum(np.random.randint(-10, 20, size=len(years)))    # Kumulativer Anstieg
values2 = np.cumsum(np.random.randint(-8, 25, size=len(years))) 

plt.plot(years, values1, marker='o', label='Liste 1')
plt.plot(years, values2, marker='x', label='Liste 2')
plt.title("Liniendiagramm")
plt.xlabel("Jahre")
plt.ylabel("Wert")
plt.grid()
plt.legend()
plt.savefig("line_plot.png")
plt.show()