import pandas as pd
import numpy as np 


data=pd.read_csv('data.csv')


class job:
    def __init__(self,name,due_date,requirement):
        self.job_name=name
        self.job_due_date=due_date
        self.job_requirement=requirement

class week:
    def __init__(self):
        self.free_time=None
        self.monday=None
        self.tuesday=None
        self.wednesday=None
        self.thursday=None
        self.friday=None
        self.saturday=None
        self.sunday=None
        
week_days={
    0:'monday',
    1:'tuesday',
    2:'wednesday',
    3:'thursday',
    4:'friday',
    5:'saturday',
    6:'sunday'
}




datas=[data['job_name'],data['due_date'],data['profit']]

jobs=[]

for i in range(len(data)):
    jobi=job(datas[0][i],datas[1][i],datas[2][i])
    jobs.append(jobi)

week1=week()

daya=[week_days[i] for i in range(7)]

for day in range(len(data)):
    week1.=jobs[day].job_name
    print(week1.monday)


'''for i in range(len(data)):
    k=f"{week_days[i]}"
    print(week1.k)'''

print(week1.monday,week1.tuesday)