import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv("py-symbol-chart.csv")
age = dataset['age']
finalGrade = dataset['G3']

fig,axes1=plt.subplots(1)
axes1.set_title("Student Age vs Final Grade")
axes1.set_xlabel("Age")
axes1.set_ylabel("Final grade")

axes1.scatter(age,finalGrade,marker='o',s=10,c="red")
axes1.legend(loc=8,framealpha=1, fontsize=8)

plt.show()
