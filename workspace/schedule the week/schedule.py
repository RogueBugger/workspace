import pandas as pd 

data=pd.read_csv('data.csv')



class job:
    def __init__(self):
        self.job_name=None
        self.job_due_date=None
        self.job_requirement=None


Tjob=[job() for _ in range(len(data))]

dataset=[data['job_name'],data['due_date'],data['profit']]

for d in range(len(data)):
    li=[]
    for data in dataset:
        li.append(data)
    

    