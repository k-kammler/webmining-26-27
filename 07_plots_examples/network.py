import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()    # nur nx.Graph() für ungerichteten Graphen
edges = [(1, 2, 0.5), (1, 3, 1.2), (2, 4, 0.8), (3, 4, 2.1), (4, 5, 1.5)]
G.add_weighted_edges_from(edges)  

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500, font_size=10)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.savefig("network.png")
plt.show()
