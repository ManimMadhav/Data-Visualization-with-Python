import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#comparing based on number of failures and internet access
dataset = pd.read_csv("student-mat.csv")
failures = dataset['failures']
internetAccess = dataset['internet']

internetAccessWith0Fails = []
for i in range(0,len(failures)):
    if failures[i]==0:
        ch = internetAccess[i]
        internetAccessWith0Fails.append(ch)

#returns the array with students who have 0 failures 
#and yes/no on whether they have internet access or not
print(internetAccessWith0Fails)

noOfYes = 0
noOfNo = 0

Fails0Array = [] 
for i in internetAccessWith0Fails:
    if i == 'yes':
        noOfYes += 1
    else:
        noOfNo += 1

print(noOfNo)
print(noOfYes)
lst=[]
lst.append(noOfNo)
lst.append(noOfYes)

plt.pie(lst,autopct="%.2f",labels=["Don't Have\n internet access","Have\n internet access"])
plt.show()
