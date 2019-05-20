import pandas as pd


data=pd.read_csv('data.csv')
datas=[data['job_name'],data['due_date'],data['priority']]


class job:
    def __init__(self,name,due_date,priority):
        self.job_name=name
        self.job_due_date=due_date
        self.job_priority=priority


class day:
    def __init__(self,date,job):
        self.day_name=date
        self.free_hours=None
        self.job=job
        self.event=None
jobs=[]
for i in range(len(data)):
    jobi=job(datas[0][i],datas[1][i],datas[2][i])
    jobs.append(jobi)




for i in range(len(jobs)):
    for j in range(len(jobs)):
        if jobs[j].job_priority > jobs[i].job_priority:
            jobs[i],jobs[j]=jobs[j],jobs[i]

for i in range(len(jobs)):
    for j in range(len(jobs)):
        if jobs[j].job_due_date > jobs[i].job_due_date:
            jobs[i],jobs[j]=jobs[j],jobs[i]

days=[]
for d in range(len(jobs)):
    dayy=day(jobs[d].job_due_date,jobs[d].job_name)
    days.append(dayy)

for d in days:
    print(d.job,d.day_name)