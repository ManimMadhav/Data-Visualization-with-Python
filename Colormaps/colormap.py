import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr

dataset = pd.read_csv("colormapDataset.csv")
G3 = dataset['G3']
G1 = dataset['G1']
absences = dataset['absences'] 
z = np.linspace(-1,1,25)

print(z)

figure, (axes1, axes2) = plt.subplots(ncols=2)
axes1.set_title("Default Colormap Setting")
colors1 = ['red','green','orange','blue','yellow']
cmap = clr.ListedColormap(colors1)

axes1.scatter(G3,absences,G1,c=z)
scatter = axes2.scatter(G3,absences,G1,c=z,cmap = cmap)
axes2.set_title("User defined Colormap setting")
figure.colorbar(scatter)
plt.show()