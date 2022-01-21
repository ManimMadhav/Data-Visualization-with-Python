import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#absences vs final grade (comparative)

dataset = pd.read_csv(r"student-mat.csv")
absences = dataset['absences']
finalgrade = dataset['G3']


plt.bar(absences,finalgrade,color='red',width=0.7)
plt.xlabel("Absences")
plt.ylabel("Marks")
plt.title("Absences vs Marks Bar Graph for Students")
plt.show()
