import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr

dataset = pd.read_csv("colormap-dataset.csv")
G3 = dataset['G3']
absences = dataset['absences'] 
z = np.linspace(-1,1,25)

print(z)

figure, (axes1, axes2) = plt.subplots(ncols=2)
axes1.set_title("Default Colormap Setting")
colors1 = ['red','green','orange','blue','yellow']
cmap = clr.ListedColormap(colors1)

axes1.scatter(G3,absences,c=z)
scatter = axes2.scatter(G3,absences,c=z,cmap = cmap)
figure.colorbar(scatter)
plt.show()