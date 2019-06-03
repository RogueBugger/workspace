import pandas as pd
from statistics import mean
import numpy as np

def least_square_error(x,y):
    sum,deno=0,0
    for xi,yi in zip(x,y):
        sum=sum+((xi-mean(x))*(yi-mean(y)))
    for xi in x:
        deno=deno+(xi-mean(x))**2
    return sum/deno





dataset=pd.read_csv('dataset.csv')
x=dataset['Head Size']
y=dataset['Brain Weight']
n=len(x)
m=least_square_error(x,y)
b=mean(y)-(m*mean(x))


root_mean_square_error=0
for x,y in zip(x,y):
    y_pred=m*x+b
    root_mean_square_error+=((y-y_pred)**2)
rmse=np.sqrt(root_mean_square_error/n)
#4442,1330
x=3267
y=m*x+b
print(rmse)
print(y)
sumofsquares = 0
sumofresiduals = 0
