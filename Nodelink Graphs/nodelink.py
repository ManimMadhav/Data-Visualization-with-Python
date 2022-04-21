import networkx as nx
from pyparsing import with_attribute
from pyvis.network import Network
import matplotlib.pyplot as plt
import pandas as pd

G1 = nx.Graph()
G1.add_node(1,weight=5)
G1.add_node(2,weight=2)
G1.add_node(3,weight=7)
G1.add_node(4,weight=3)
G1.add_edge(1,2,flux = 10)
G1.add_edge(2,3,flux = 12)
G1.add_edge(1,4,flux = 7)
G1.add_edge(4,2,flux = 8)
G1.add_edge(3,4,flux = 2)
nx.draw(G1,node_color='red',with_labels = True)
plt.show()

G2 = nx.Graph()
G2.add_node(2,weight=2)
G2.add_node(6,weight=5)
G2.add_node(3,weight=7)
G2.add_node(7,weight=10)
G2.add_edge(3,6,flux = 3)
G2.add_edge(2,7,flux = 17)
G2.add_edge(2,3,flux = 4)
G2.add_edge(6,7,flux = 2)
G2.add_edge(2,6,flux = 9)
G2.add_edge(3,7,flux = 1)
G2.add_edge(6,3,flux = 11)

nx.draw(G2,node_color='blue',with_labels = True)
plt.show()

F = nx.Graph()
F = nx.compose(G1,G2)
labels = nx.get_edge_attributes(F, 'flux')
nx.draw(F,with_labels = True, node_color = 'green')
plt.show()

print("The shortest distance is ",nx.shortest_path_length(F,3,6))