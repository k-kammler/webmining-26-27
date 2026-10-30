import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey

Sankey(
    flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10], 
    labels=['', '', '', 'Erstes', 'Zweites', 'Drittes', 'Viertes', 'Fünftes'], 
    orientations=[-1, 1, 0, 1, 1, 1, 0, -1]
).finish()

plt.savefig("sankey.png")
plt.show()