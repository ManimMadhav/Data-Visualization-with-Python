#distributional visualization
#using density plots

import pandas as pd
import matplotlib.pyplot as plt
  
# loading the dataset
dataset = pd.read_csv('student-mat.csv')

dataset.G1.plot.density(color='blue')
dataset.G2.plot.density(color='red')
dataset.G3.plot.density(color='green')
plt.title('Density plot for Final Grade')
plt.show()
