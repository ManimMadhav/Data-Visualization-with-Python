#relational visualization

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib_venn import venn3

dataset = pd.read_csv('student-mat.csv')
fails = dataset['failures']
schoolsup = dataset['schoolsup']
absence = dataset['absences']


set1 = set(fails)
set2 = set(schoolsup)
set3 = set(absence)

venn3([set1, set2, set3], ('Failures', 'School Support\n (Academic)', 'Absences'))

plt.show()
