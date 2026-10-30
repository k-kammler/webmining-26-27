import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(9, 9)

plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar(label="Werte")
plt.title("Heatmap")
plt.savefig("heatmap.png")
plt.show()
