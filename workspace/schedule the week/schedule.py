import pandas as pd 

data=pd.read_csv('data.csv')



class job:
    def __init__(self,name,due_date,requirement):
        self.job_name=name
        self.job_due_date=due_date
        self.job_requirement=requirement


datas=[data['job_name'],data['due_date'],data['profit']]

jobs=[]

for i in range(len(data)):
    jobi=job(datas[0][i],datas[1][i],datas[2][i])
    jobs.append(jobi)
