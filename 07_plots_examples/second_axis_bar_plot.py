import matplotlib.pyplot as plt
import numpy as np

labels = ['Bar 1', 'Bar 2']
values = [9, 1000]

fig, ax1 = plt.subplots(figsize=(6, 4))

ax1.bar(labels, values, alpha=0.7)
ax1.set_xlabel('Kategorien')
ax1.set_ylabel('Werte (linke Säule)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_ylim(0, 10) 

ax2 = ax1.twinx()
ax2.set_ylabel('Werte (rechte Säule)', color='black')
ax2.set_ylim(990, 1010)  
ax2.set_yticks(np.arange(990, 1011, 5))  
ax2.tick_params(axis='y', labelcolor='black')

plt.tight_layout()
plt.savefig('second_axis_bar_plot.png')
plt.show()

