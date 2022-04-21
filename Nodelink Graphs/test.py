import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("networkx.csv")
G = nx.from_pandas_edgelist(df,"G3", "Walc",'famsize')

nx.draw(G, node_color = 'black')
plt.show()

nx.draw_networkx(G,node_color='orange')
plt.show()

nx.draw_circular(G, node_color = 'blue')
plt.show()

nx.draw_random(G, node_color = 'yellow')
plt.show()
