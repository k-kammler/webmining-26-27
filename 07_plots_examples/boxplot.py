import matplotlib.pyplot as plt
import numpy as np

np.random.seed(43)
data1 = np.random.normal(50, 10, 30)    # Mean, STD, Number of samples
data2 = np.random.normal(50, 10, 6)  

print(data2)

plt.boxplot(
    [data1, data2], 
    notch=True,           
    patch_artist=True,    # To enable color filling
    showmeans=True, 
    meanline=True,
    tick_labels=["Daten 1", "Daten 2"],
    boxprops=dict(facecolor="lightblue", color="blue"),
    medianprops=dict(color="red", linewidth=2),
    widths=((len(data1) / (len(data1) + len(data2))), (len(data2) / (len(data1) + len(data2))))
)

plt.title("Boxplot-Variationen", fontsize=14)
plt.ylabel("Werte", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.7)

plt.savefig("boxplot.png")
plt.show()