import matplotlib.pyplot as plt

labels = ['Gruppe 1', 'Gruppe 2']
values = [29, 900]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
fig.subplots_adjust(hspace=0.05)


ax1.bar(labels, values)
ax2.bar(labels, values)

ax1.set_ylim(800, 1100) 
ax2.set_ylim(0, 30) 

ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False) 
ax2.xaxis.tick_bottom()

d = .5  
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

plt.savefig('cut_bar_plot.png')
plt.show()
