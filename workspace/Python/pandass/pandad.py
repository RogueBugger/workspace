import pandas as pd
from random import shuffle
import numpy as np
dataset=pd.read_csv('dataset.csv')
x1=dataset['x1']
x2=dataset['x2']
x3=dataset['x3']
x4=dataset['x4']
data=[x1,x2,x3,x4]
t=dataset['target']
for d in range(len(dataset)):
    xi=[]
    for i in data:
        xi.append(i[d])
    xi=np.array(xi).reshape(4,1)
    tt=np.array(t[d])
    print(xi," " ,tt,end=" ")
    print('\n')
