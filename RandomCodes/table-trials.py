import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("table-dataset.csv")
famSize = dataset['famsize']
walc = dataset['Walc']
g3 = dataset['G3']

df = pd.DataFrame(dataset,columns=['famsize','walc','G3'])
lst=['famsize','walc','G3']
rowlabels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
fig, ax = plt.subplots() 
ax.set_axis_off()
table = ax.table(cellText= df.values,
                  colLabels = lst,
                  rowLabels= rowlabels,
                  rowColours =["blue"] * len(g3),  
                  colColours =["green"] * len(g3),
                  )

plt.show()