import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 2),
    ('A', 'C', 6),
    ('A', 'D', 4),
    ('B', 'C', 3),
    ('B', 'D', 5),
    ('C', 'D', 1)
])

pos = {'A': (0, 1), 'B': (-1, 0), 'C': (1, 0), 'D': (0, -1)}
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, labels)
plt.title("Граф варианта 15: Бухарест)")
plt.show()