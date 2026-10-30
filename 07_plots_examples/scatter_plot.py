import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 100, size=25)
y = np.random.randint(0, 30, size=25)

plt.scatter(x, y, color='red')
plt.title("Streudiagramm")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.savefig("scatter_plot.png")
plt.show()
